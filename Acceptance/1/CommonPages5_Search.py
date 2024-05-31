from selenium import selenium
import unittest, time, re

from env import *
import CommonElements

class CCommonPages(CommonElements.CCommonElements):


	# ========================================================================================================
	# 	Search Plan/Case/Run pages related functions
	# ========================================================================================================


	#----------------------------------------------------------------------
	#---------------------- (1) 'Search Plan' page ------------------------
	#----------------------------------------------------------------------

	def verifySearchPlanPageIsReady(self,myself,sel,planName="<default>",author="<default>",owner="<default>",\
			planType="<default>",tag="<default>",caseDefaultTester="<default>",product="<default>",\
			prodversion="<default>",envgroup="<default>",createdAfter="<default>",createdBefore="<default>",\
			active="<default>",testplanIdNames="<default>"):
		''' Verify Search Plan page is ready. The value of the para 'active' includes: 'on', 'off'. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Test plans")
		self.verifyTargetText(myself,sel,"Search Plan","css=h2")
		self.verifyLink(myself,sel,"View All Plans")

		if planName!="<default>": self.verifyValue(myself,sel,planName,"id_name__icontains")
		if author!="<default>": self.verifyValue(myself,sel,author,"id_author__email__startswith")
		if owner!="<default>": self.verifyValue(myself,sel,owner,"id_owner__username__startswith")
		if tag!="<default>": self.verifyValue(myself,sel,tag,"id_tag__name__in")
		if caseDefaultTester!="<default>": self.verifyValue(myself,sel,caseDefaultTester,"id_case__default_tester__username__startswith")
		if createdAfter!="<default>": self.verifyValue(myself,sel,createdAfter,"id_create_date__gte")
		if createdBefore!="<default>": self.verifyValue(myself,sel,createdBefore,"id_create_date__lte")

		if planType!="<default>": self.verifySelectedLabel(myself,sel,planType,"id_type")
		if product!="<default>": self.verifySelectedLabel(myself,sel,product,"id_product")
		if prodversion!="<default>": self.verifySelectedLabel(myself,sel,prodversion,"id_default_product_version")
		if envgroup!="<default>": self.verifySelectedLabel(myself,sel,envgroup,"id_env_group")

		#Note: the value of the para 'active' includes: 'on', 'off'.
		if active!="<default>": self.verifyCheckBox(myself,sel,active,"id_is_active","")

		if testplanIdNames!="<default>":
			
			if testplanIdNames!="":
				for tId,tName in testplanIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: self.verifyTargetText(myself,sel,"No test plans found.","css=td")

	def verifyMyPlanFromSearch(self,myself,sel,testplanId):
		''' verify my test plan exists from search page. '''

		myplanexists = False

		if self.isLink(myself,sel,testplanId): myplanexists = True
		else:
			nextexists = self.isElement(myself,sel,"//form[@id='plans_form']/div[2]/a[@class='next']")
			while nextexists:

				self.clickElementAndWait(myself,sel,"//form[@id='plans_form']/div[2]/a[@class='next']")
				time.sleep(env.t)

				if self.isLink(myself,sel,testplanId): myplanexists = True; nextexists = False
				else: nextexists = self.isElement(myself,sel,"//form[@id='plans_form']/div[2]/a[@class='next']")

		try: myself.assertEqual(True, myplanexists)
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def fillDataForSearchPlan(self,myself,sel,planName="<default>",author="<default>",owner="<default>",\
			planType="<default>",tag="<default>",caseDefaultTester="<default>",product="<default>",\
			prodversion="<default>",envgroup="<default>",createdAfter="<default>",createdBefore="<default>",\
			active="<default>"):
		''' Fill data in Search Plan page. The value of the para 'active' includes: 'on', 'off'. '''

		if planName!="<default>": self.inputText(myself,sel,"id_name__icontains",planName)
		if author!="<default>": self.inputText(myself,sel,"id_author__email__startswith",author)
		if owner!="<default>": self.inputText(myself,sel,"id_owner__username__startswith",owner)
		if tag!="<default>": self.inputText(myself,sel,"id_tag__name__in",tag)
		if caseDefaultTester!="<default>": self.inputText(myself,sel,"id_case__default_tester__username__startswith",caseDefaultTester)
		if createdAfter!="<default>": self.inputText(myself,sel,"id_create_date__gte",createdAfter)
		if createdBefore!="<default>": self.inputText(myself,sel,"id_create_date__lte",createdBefore)

		#select plan type
		if planType!="<default>": 
			if not self.isSelectedLabel(myself,sel,planType,"id_type"):
				self.selectOptionInDropDownList(myself,sel,"id_type",planType)

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"id_product"):
				self.selectOptionInDropDownList(myself,sel,"id_product",product)

		#select product version
		if prodversion!="<default>": 
			if not self.isSelectedLabel(myself,sel,prodversion,"id_default_product_version"):
				self.selectOptionInDropDownList(myself,sel,"id_default_product_version",prodversion)

		#select env group
		if envgroup!="<default>": 
			if not self.isSelectedLabel(myself,sel,envgroup,"id_env_group"):
				self.selectOptionInDropDownList(myself,sel,"id_env_group",envgroup)

		#Note: the value of the para 'active' includes: 'on', 'off'.
		if active!="<default>": self.clickCheckBox(myself,sel,"id_is_active","",onoff=active)

	def selectTestPlanInSearchPlan(self,myself,sel,testplanIds):
		''' Select part of test plans in the Search Plan page. The data type of the para testplanIds is 'list' type.

		    An example of the value of testplanIds: [testplanId1,testplanId2]
		    Example of call: CCommonUtils().selectTestPlanInSearchPlan(self,sel,[env.testplanId])
		'''

		self.clickCheckBox(myself,sel,"id_check_all_plans","",onoff="on")
		self.clickCheckBox(myself,sel,"id_check_all_plans","",onoff="off")
		if testplanIds != "":
			for i in range(len(testplanIds)):
				self.clickCheckBox(myself,sel,"plan",testplanIds[i],onoff="on")

	def clickActionInSearchPlan(self,myself,sel,ActionName):
		''' Click Action in Search Plan Page including button or link. '''

		if ActionName == "Search": self.clickBtnAndWait(myself,sel,"submit","Search")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")
		elif ActionName == "New Test Plan": self.clickBtnAndWait(myself,sel,"button","New Test Plan")
		elif ActionName == "Clone": self.clickBtnAndWait(myself,sel,"button","Clone")
		elif ActionName == "Printable copy": self.clickBtnAndWait(myself,sel,"button","Printable copy")
		elif ActionName == "Export": self.clickBtn(myself,sel,"button","Export")

	def clickEditInSearchPlanResult(self,myself,sel,testplanId):
		''' Click Edit Action in Search Plan Result Page. '''

		self.clickElement(myself,sel,"//a[contains(@href, '/plan/"+testplanId+"/edit/')]")


	#----------------------------------------------------------------------
	#---------------------- (2) 'Search Case' page ------------------------
	#----------------------------------------------------------------------

	def verifySearchCasePageIsReady(self,myself,sel,componentAll="<default>",testcaseIdNames="<default>"):
		''' Verify Search Case page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Test cases")
		self.verifyTargetText(myself,sel,"Search Case","css=h2")
		self.verifyElement(myself,sel,"//input[@name='a' and @value='search' and @type='submit']")

		if componentAll!="<default>":
			self.verifyTargetText(myself,sel,componentAll,"id_component")

		if testcaseIdNames!="<default>":
			
			if testcaseIdNames!="":
				for tId,tName in testcaseIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: self.verifyTargetText(myself,sel,"No test case found","css=center")

	def verifySearchCasePageDefaultSetting(self,myself,sel):
		''' Verify the Default Setting of Search Case page is correct. '''

		self.verifyValue(myself,sel,"","id_summary")
		self.verifyValue(myself,sel,"","id_author")
		self.verifyValue(myself,sel,"","id_plan")
		self.verifyValue(myself,sel,"","id_bug_id")
		self.verifyValue(myself,sel,"","id_tag__name__in")

		self.verifySelectedLabel(myself,sel,"---------","id_product")
		self.verifySelectedLabel(myself,sel,"----------","id_is_automated")
		self.verifySelectedLabel(myself,sel,"---------","id_category")
		self.verifySelectedLabel(myself,sel,"---------","id_component")

		for i in range(5):
			self.verifyCheckBox(myself,sel,"off","priority",str(i+1))

		self.verifyCheckBox(myself,sel,"off","id_is_automated_proposed","")

		for i in range(4):
			self.verifyCheckBox(myself,sel,"on","case_status",str(i+1))

	def fillDataForSearchCase(self,myself,sel,summary="<default>",author="<default>",product="<default>",plan="<default>",\
			priority="<default>",automated="<default>",autoproposed="<default>",category="<default>",\
			status="<default>",component="<default>",bugID="<default>",tag="<default>"):
		''' Fill data in Search Case page. '''

		if summary!="<default>": self.inputText(myself,sel,"id_summary",summary)
		if author!="<default>": self.inputText(myself,sel,"id_author",author)
		if plan!="<default>": self.inputText(myself,sel,"id_plan",plan)
		if bugID!="<default>": self.inputText(myself,sel,"id_bug_id",bugID)
		if tag!="<default>": self.inputText(myself,sel,"id_tag__name__in",tag)

		if product!="<default>": 
			if not product == sel.get_selected_label("//select[@id='id_product']"):
				self.selectOptionInDropDownList(myself,sel,"id_product",product)

		if automated!="<default>":
			if not product == sel.get_selected_label("//select[@id='id_is_automated']"):
				self.selectOptionInDropDownList(myself,sel,"id_is_automated",automated)

		if category!="<default>": 
			if not product == sel.get_selected_label("//select[@id='id_category']"):
				self.selectOptionInDropDownList(myself,sel,"id_category",category)

		if component!="<default>": 
			if not product == sel.get_selected_label("//select[@id='id_component']"):
				self.selectOptionInDropDownList(myself,sel,"id_component",component)

		if priority != "<default>": #Example to set this para: priority=[1,2,3,5]
			for i in range(5):
				self.clickCheckBox(myself,sel,"priority",str(i+1),onoff="off")

			for i in range(len(priority)):
				self.clickCheckBox(myself,sel,"priority",str(priority[i]),onoff="on")

		if autoproposed != "<default>": #Example to set this para: autoproposed="on" or autoproposed="off"
			self.clickCheckBox(myself,sel,"id_is_automated_proposed","",onoff=autoproposed)

		if status != "<default>": #Example to set this para: status=[1,2,4]
			for i in range(4):
				self.clickCheckBox(myself,sel,"case_status",str(i+1),onoff="off")

			for i in range(len(status)):
				self.clickCheckBox(myself,sel,"case_status",str(status[i]),onoff="on")

	def clickActionInSearchCase(self,myself,sel,ActionName):
		''' Click Action in Search Case Page including button or link. '''

		if ActionName == "Search": self.clickBtnAndWait(myself,sel,"submit","search")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")


	#----------------------------------------------------------------------
	#---------------------- (3) 'Search Run' page -------------------------
	#----------------------------------------------------------------------

	def verifySearchRunPageIsReady(self,myself,sel,summary="<default>",plan="<default>",product="<default>",prodversion="<default>",\
			build="<default>",envgroup="<default>",status="<default>",ownertype="<default>",owner="<default>",\
			caserunassignee="<default>",tag="<default>",testrunIdNames="<default>"):
		''' Verify Search Run page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Test runs")
		self.verifyTargetText(myself,sel,"Search Run","css=h2")
		self.verifyLink(myself,sel,"View All Runs")

		if summary!="<default>": self.verifyValue(myself,sel,summary,"id_summary")
		if plan!="<default>": self.verifyValue(myself,sel,plan,"id_plan")
		if owner!="<default>": self.verifyValue(myself,sel,owner,"id_search_people")
		if caserunassignee!="<default>": self.verifyValue(myself,sel,caserunassignee,"id_case_run__assignee")
		if tag!="<default>": self.verifyValue(myself,sel,tag,"id_tag__name__in")

		if product!="<default>": self.verifySelectedLabel(myself,sel,product,"id_product")
		if prodversion!="<default>": self.verifySelectedLabel(myself,sel,prodversion,"id_product_version")
		if build!="<default>": self.verifySelectedLabel(myself,sel,build,"id_build")

		#ownertype's value involves: 'Manager | Tester', 'Manager', 'Defaut tester'
		if ownertype!="<default>": self.verifySelectedLabel(myself,sel,ownertype,"id_people_type")

		if status!="<default>": self.verifySelectedLabel(myself,sel,status,"id_status")
		if envgroup!="<default>": self.verifySelectedLabel(myself,sel,envgroup,"id_env_group")

		if testrunIdNames!="<default>":
			
			if testrunIdNames!="":
				for tId,tName in testrunIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: self.verifyTargetText(myself,sel,"No test runs found","css=center")

	def verifyMyRunFromSearch(self,myself,sel,testrunId):
		''' verify my test run exists from search page. '''

		myrunexists = False

		if self.isLink(myself,sel,testrunId): myrunexists = True
		else:
			nextexists = self.isElement(myself,sel,"//form[@id='runs_form']/div[2]/a[@class='next']")
			while nextexists:

				self.clickElementAndWait(myself,sel,"//form[@id='runs_form']/div[2]/a[@class='next']")
				time.sleep(env.ts)

				if self.isLink(myself,sel,testrunId): myrunexists = True; nextexists = False
				else: nextexists = self.isElement(myself,sel,"//form[@id='runs_form']/div[2]/a[@class='next']")

		try: myself.assertEqual(True, myrunexists)
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def fillDataForSearchRun(self,myself,sel,summary="<default>",plan="<default>",product="<default>",prodversion="<default>",\
			build="<default>",envgroup="<default>",status="<default>",ownertype="<default>",owner="<default>",\
			caserunassignee="<default>",tag="<default>"):
		''' Fill data in Search Run page. '''

		if summary!="<default>": self.inputText(myself,sel,"id_summary",summary)
		if plan!="<default>": self.inputText(myself,sel,"id_plan",plan)
		if owner!="<default>": self.inputText(myself,sel,"id_search_people",owner)
		if caserunassignee!="<default>": self.inputText(myself,sel,"id_case_run__assignee",caserunassignee)
		if tag!="<default>": self.inputText(myself,sel,"id_tag__name__in",tag)

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"id_product"):
				self.selectOptionInDropDownList(myself,sel,"id_product",product)

		#select product version
		if prodversion!="<default>": 
			if not self.isSelectedLabel(myself,sel,prodversion,"id_product_version"):
				self.selectOptionInDropDownList(myself,sel,"id_product_version",prodversion)

		#add Build
		if build!="<default>": 
			if not self.isSelectedLabel(myself,sel,build,"id_build"):
				self.selectOptionInDropDownList(myself,sel,"id_build",build)

		#select owner type
		if ownertype!="<default>": #ownertype's value involves: 'Manager | Tester', 'Manager', 'Defaut tester'
			if not self.isSelectedLabel(myself,sel,ownertype,"id_people_type"):
				self.selectOptionInDropDownList(myself,sel,"id_people_type",ownertype)

		#select status
		if status!="<default>": 
			if not self.isSelectedLabel(myself,sel,status,"id_status"):
				self.selectOptionInDropDownList(myself,sel,"id_status",status)

		#select env group
		if envgroup!="<default>": 
			if not self.isSelectedLabel(myself,sel,envgroup,"id_env_group"):
				self.selectOptionInDropDownList(myself,sel,"id_env_group",envgroup)

	def selectTestRunsInSearchRun(self,myself,sel,testrunIds):
		''' Select part of test runs in the Search Run page. The data type of the para 'testrunIds' is 'list' type.

		    An example of the value of testrunIds: [testrunId1,testrunId2]
		    Example of call: CCommonUtils().selectTestRunsInSearchRun(self,sel,[env.testrunId])
		'''

		self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="on")
		self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="off") #Uncheck all runs
		if testrunIds != "":
			for i in range(len(testrunIds)):
				self.clickCheckBox(myself,sel,"run",testrunIds[i],onoff="on")

	def clickActionInSearchRun(self,myself,sel,ActionName):
		''' Click Action in Search Run Page including button or link. '''

		if ActionName == "Search": self.clickBtnAndWait(myself,sel,"submit","Search")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")
		elif ActionName == "Clone": self.clickBtnAndWait(myself,sel,"button","Clone")


	# ========================================================================================================
	# 	Advanced Search pages related functions
	# ========================================================================================================


	#----------------------------------------------------------------------
	#------------------- (1) 'Advanced Search' page -----------------------
	#----------------------------------------------------------------------

	def verifyAdvancedSearchPageIsReady(self,myself,sel):
		''' Verify advanced search page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel, "Advanced Search")
		self.verifyElement(myself,sel,"css=input[type=reset]")

	def clickActionInAdvancedSearch(self,myself,sel,ActionName):
		''' Click Action in Advanced Search Page including button or link. '''

		if ActionName == "Search Plan": self.clickBtnAndWait(myself,sel,"button","Search Plan")
		elif ActionName == "Search Case": self.clickBtnAndWait(myself,sel,"button","Search Case")
		elif ActionName == "Search Run": self.clickBtnAndWait(myself,sel,"button","Search Run")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")


	#----------------------------------------------------------------------
	#----------------- (2) 'Advanced Search Plan' page --------------------
	#----------------------------------------------------------------------

	def verifyAdvancedSearchPlanResultIsReady(self,myself,sel,tIdNames="<default>",tNoIdNames="<default>"):
		''' Verify advanced search result for plan page is ready. The data type of the para 'tIdNames' & 'tNoIdNames' is 'dict', but 'tIds' is 'list'. '''

		time.sleep(env.tl)
		self.verifyPageTitle(myself,sel, "Advanced Search Results")
		self.verifyText(myself,sel,"Target:")
		self.verifyText(myself,sel,"plan;")
		self.verifyText(myself,sel,"Search Results")

		if tIdNames!="<default>":
			if tIdNames!="":
				self.verifyBtn(myself,sel,"button","New Test Plan")
				self.verifyBtn(myself,sel,"button","Clone")

				for tId,tName in tIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: #if tIdNames=="", it indicates there will be no result searched out
				self.verifyBtnNotPresent(myself,sel,"button","New Test Plan")
				self.verifyBtnNotPresent(myself,sel,"button","Clone")

		if tNoIdNames!="<default>":
			for tId,tName in tNoIdNames.items():
				self.verifyLinkNotPresent(myself,sel,tId)
				self.verifyLinkNotPresent(myself,sel,tName)

	def fillDataForPlanItemsInASearch(self,myself,sel,productList="<default>",componentList="<default>",\
		prodversionList="<default>",planId="<default>",summary="<default>",planTypeList="<default>",\
		author="<default>",owner="<default>",tag="<default>",tagOption="<default>",active="<default>",\
		createdAfter="<default>",createdBefore="<default>"):
		''' Fill data For Plan Items In Advanced Search page. '''

		#select product
		if productList!="<default>": 
			for i in range(len(productList)):
				self.selectOptionInList(myself,sel,"pl_product",productList[i])

		#select component
		if componentList!="<default>": 
			for i in range(len(componentList)):
				self.selectOptionInList(myself,sel,"pl_component",componentList[i])

		#select version
		if prodversionList!="<default>": 
			for i in range(len(prodversionList)):
				self.selectOptionInList(myself,sel,"pl_version",prodversionList[i])

		if planId!="<default>": self.inputText(myself,sel,"pl_id",planId)
		if summary!="<default>": self.inputText(myself,sel,"pl_summary",summary)

		#select plan type
		if planTypeList!="<default>": 
			for i in range(len(planTypeList)):
				self.selectOptionInList(myself,sel,"pl_type",planTypeList[i])

		if author!="<default>": self.inputText(myself,sel,"pl_authors",author)
		if owner!="<default>": self.inputText(myself,sel,"pl_owners",owner)
		if tag!="<default>": self.inputText(myself,sel,"pl_tags",tag)

		#select tag options - Note: include 2 options: 'Contains', 'Not Contains'
		if tagOption!="<default>":
			if not self.isSelectedLabel(myself,sel,tagOption,"pl_tags_exclude"):
				self.selectOptionInDropDownList(myself,sel,"pl_tags_exclude",tagOption)

		#select active status - Note: the value of the para 'active' includes: '--', 'Active', 'Inactive'
		if active!="<default>":
			if not self.isSelectedLabel(myself,sel,active,"pl_active"):
				self.selectOptionInDropDownList(myself,sel,"pl_active",active)

		if createdAfter!="<default>": self.inputText(myself,sel,"pl_created_since",createdAfter)
		if createdBefore!="<default>": self.inputText(myself,sel,"pl_created_before",createdBefore)

	def selectPlanInASearchPlanResult(self,myself,sel,testplanIds):
		''' Select part of test plans in the Search Plan Result page. The data type of the para testplanIds is 'list' type. '''

		if testplanIds == "All":
			self.clickCheckBox(myself,sel,"id_check_all_plans","",onoff="off")
			self.clickCheckBox(myself,sel,"id_check_all_plans","",onoff="on")
		else:
			self.clickCheckBox(myself,sel,"id_check_all_plans","",onoff="on")
			self.clickCheckBox(myself,sel,"id_check_all_plans","",onoff="off")
			if testplanIds != "":
				for i in range(len(testplanIds)):
					self.clickCheckBox(myself,sel,"plan",testplanIds[i],onoff="on")

	def clickActionInASearchPlanResult(self,myself,sel,ActionName):
		''' Click Action in Search Plan Page including button or link. '''

		if  ActionName == "New Test Plan": self.clickBtnAndWait(myself,sel,"button","New Test Plan")

		elif ActionName == "Clone": self.clickBtnAndWait(myself,sel,"button","Clone")
		elif ActionName == "Printable copy": self.clickBtnAndWait(myself,sel,"button","Printable copy")
		elif ActionName == "Export": self.clickBtn(myself,sel,"button","Export")

	def clickOtherActionInSearchPlanResult(self,myself,sel,actionName,actionValue="<default>"):
		''' Click Other Actions in Advanced Search Result Page including button or link. '''

		if actionName == "Case Number": self.clickElement(myself,sel,"css=a[title="+actionValue+" test cases]")
		elif actionName == "Run Number": self.clickElement(myself,sel,"css=a[title="+actionValue+" test runs]")

	def verifyPrintTestPlanPageIsReady(self,myself,sel,testplanIdNames,testcaseIdNames="<default>",testcaseNotShowIdNames="<default>"):
		''' Verify print test plan page is ready. 'testplanIdNames' and 'testcaseIdNames' and 'testcaseNotShowIdNames' are 'dict' type para. '''

		time.sleep(env.ts)

		#************************************************************************************************************************************************************************
		#There is error exists here, the right title should be "Printable copy for test plans",
		#After the error get fixed, the code here shoul be changed accordingly. Related test case: tc_ID84340_PrintPlan.py
		self.verifyPageTitle(myself,sel, "Printable copy for test cases")
		#************************************************************************************************************************************************************************

		for tId,tName in testplanIdNames.items():
			self.verifyText(myself,sel,"["+tId+"] "+tName)
	
		self.verifyTargetText(myself,sel,"Test Plan Document","//h2[@id='plan_document']")
		self.verifyTargetText(myself,sel,"Test Cases","//h2[@id='plan_cases']")

		if testcaseIdNames!="<default>":
			for tcId,tcName in testcaseIdNames.items():
				self.verifyText(myself,sel,"["+tcId+"] "+tcName)

		if testcaseNotShowIdNames!="<default>":
			for tcId,tcName in testcaseNotShowIdNames.items():
				self.verifyTextNotPresent(myself,sel,"["+tcId+"] "+tcName)

	def verifyPrintNoTestPlanWarningFromSearchPageIsReady(self,myself,sel):
		''' Verify the warning page is ready and shown correctly when click 'Printable copy' button in advanced search plan result without a test plan selected. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel, "INFO - At least one plan is required.")
		self.verifyText(myself,sel,"At least one plan is required.")

		self.verifyElement(myself,sel,"//input[@value='Return']")


	#----------------------------------------------------------------------
	#----------------- (3) 'Advanced Search Case' page --------------------
	#----------------------------------------------------------------------

	def verifyAdvancedSearchCaseResultIsReady(self,myself,sel,tIdNames="<default>",tNoIdNames="<default>"):
		''' Verify advanced search result for case page is ready. The data type of the para 'tIdNames' & 'tNoIdNames' is 'dict', but 'tIds' is 'list'. '''

		time.sleep(env.tl)
		self.verifyPageTitle(myself,sel, "Advanced Search Results")
		self.verifyText(myself,sel,"Target:")
		self.verifyText(myself,sel,"case;")
		self.verifyText(myself,sel,"Search Results")

		if tIdNames!="<default>":
			if tIdNames!="":
				self.verifyBtn(myself,sel,"submit","Clone")

				for tId,tName in tIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: #if tIdNames=="", it indicates there will be no result searched out
				self.verifyBtnNotPresent(myself,sel,"submit","Clone")

		if tNoIdNames!="<default>":
			for tId,tName in tNoIdNames.items():
				self.verifyLinkNotPresent(myself,sel,tId)
				self.verifyLinkNotPresent(myself,sel,tName)

	def fillDataForCaseItemsInASearch(self,myself,sel,productList="<default>",componentList="<default>",\
		categoryList="<default>",caseId="<default>",summary="<default>",author="<default>",\
		defaultTester="<default>",tag="<default>",tagOption="<default>",bugID="<default>",\
		statusList="<default>",automated="<default>",autoproposed="<default>",priorityList="<default>",\
		script="<default>",createdAfter="<default>",createdBefore="<default>"):
		''' Fill data For Case Items In Advanced Search page. '''

		#select product
		if productList!="<default>": 
			for i in range(len(productList)):
				self.selectOptionInList(myself,sel,"cs_product",productList[i])

		#select component
		if componentList!="<default>": 
			for i in range(len(componentList)):
				self.selectOptionInList(myself,sel,"cs_component",componentList[i])

		#select category
		if categoryList!="<default>": 
			for i in range(len(categoryList)):
				self.selectOptionInList(myself,sel,"cs_category",categoryList[i])

		if caseId!="<default>": self.inputText(myself,sel,"cs_id",caseId)
		if summary!="<default>": self.inputText(myself,sel,"cs_summary",summary)
		if author!="<default>": self.inputText(myself,sel,"cs_authors",author)
		if defaultTester!="<default>": self.inputText(myself,sel,"cs_tester",defaultTester)
		if tag!="<default>": self.inputText(myself,sel,"cs_tags",tag)

		#select tag options - Note: include 2 options: 'Contains', 'Not Contains'
		if tagOption!="<default>":
			if not self.isSelectedLabel(myself,sel,tagOption,"cs_tags_exclude"):
				self.selectOptionInDropDownList(myself,sel,"cs_tags_exclude",tagOption)

		if bugID!="<default>": self.inputText(myself,sel,"cs_bugs",bugID)

		#Value of this para 'statusList' included: 1,2,3,4, an example to set this para: status=[1,2,3,4]
		if statusList != "<default>":
			for i in range(len(statusList)):
				self.clickCheckBox(myself,sel,"cs_status",str(statusList[i]),onoff="on")

		#Value of this para 'automated' included: '--', 'Automated', 'Manual'
		if automated!="<default>":
			if not self.isSelectedLabel(myself,sel,automated,"cs_auto"):
				self.selectOptionInDropDownList(myself,sel,"cs_auto",automated)

		#Value of this para 'autoproposed' included: '--', 'Auto Proposed', 'Non Auto Proposed'
		if autoproposed != "<default>":
			if not self.isSelectedLabel(myself,sel,automated,"cs_proposed"):
				self.selectOptionInDropDownList(myself,sel,"cs_proposed",autoproposed)

		#Value of this para 'priorityList' included: 1,2,3,4,5, an example to set this para: priority=[1,2,3,4,5]
		if priorityList != "<default>":
			for i in range(len(priorityList)):
				self.clickCheckBox(myself,sel,"cs_priority",str(priorityList[i]),onoff="on")

		if script!="<default>": self.inputText(myself,sel,"cs_script",script)
		if createdAfter!="<default>": self.inputText(myself,sel,"cs_created_since",createdAfter)
		if createdBefore!="<default>": self.inputText(myself,sel,"cs_created_before",createdBefore)

	def selectCaseInASearchCaseResult(self,myself,sel,testcaseIds):
		''' Select part of test cases in the Search Case Result page. The data type of the para testcaseIds is 'list' type. '''

		if testcaseIds == "All":
			self.clickCheckBox(myself,sel,"id_checkbox_all_case","",onoff="off")
			self.clickCheckBox(myself,sel,"id_checkbox_all_case","",onoff="on")
		else:
			self.clickCheckBox(myself,sel,"id_checkbox_all_case","",onoff="on")
			self.clickCheckBox(myself,sel,"id_checkbox_all_case","",onoff="off")
			if testcaseIds != "":
				for i in range(len(testcaseIds)):
					self.clickCheckBox(myself,sel,"case",testcaseIds[i],onoff="on")

	def clickActionInASearchCaseResult(self,myself,sel,ActionName):
		''' Click Action in Search Case Page including button or link. '''

		if  ActionName == "New Test Plan": self.clickBtnAndWait(myself,sel,"button","New Test Plan")

		elif ActionName == "Clone": self.clickBtnAndWait(myself,sel,"submit","Clone")
		elif ActionName == "Printable copy": self.clickBtnAndWait(myself,sel,"button","Printable copy")
		elif ActionName == "Export": self.clickBtn(myself,sel,"button","Export")

	def expcolCaseInASearchCaseResult(self,myself,sel,whichCase,expcolType):
		''' Expand or collapse Case In Advanced Search Case Result. Some examples of the value of 'whichCase': 'All', '1', '2', '3', etc. '''

		if whichCase == "All":
			if expcolType == "Expand":
				self.clickElement(myself,sel,"css=img.collapse-all")
				time.sleep(env.ts)
				self.verifyElement(myself,sel,"css=img.expand-all")
			elif expcolType == "Collapse":
				self.clickElement(myself,sel,"css=img.expand-all")
				time.sleep(2)
				self.verifyElement(myself,sel,"css=img.collapse-all")

			return ""

		else:
			if expcolType == "Expand":
				whichCase=str(int(whichCase)*2-1)
				self.clickElement(myself,sel,"//table[@id='testcases_table']/tbody/tr["+whichCase+"]/td/img")
				time.sleep(env.ts)
				self.verifyElement(myself,sel,"//table[@id='testcases_table']/tbody/tr["+whichCase+"]/td/img[@class='blind_icon collapse']")

				testcaseId = sel.get_text("//table[@id='testcases_table']/tbody/tr["+whichCase+"]/td[3]")
				return testcaseId

			elif expcolType == "Collapse":
				self.clickElement(myself,sel,"//table[@id='testcases_table']/tbody/tr["+whichCase+"]/td/img")
				time.sleep(2)
				self.verifyElement(myself,sel,"//table[@id='testcases_table']/tbody/tr["+whichCase+"]/td/img[@class='blind_icon expand']")

				return ""

	def verifyPrintTestCasePageIsReady(self,myself,sel,testcaseIdNames):
		''' Verify print test case page is ready. 'testcaseIdNames' is a 'dict' type para. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel, "Printable copy for test cases")

		for tId,tName in testcaseIdNames.items():
			self.verifyText(myself,sel,"["+tId+"] "+tName)
	
	def verifyPrintNoTestCaseWarningFromSearchPageIsReady(self,myself,sel):
		''' Verify the warning page is ready and shown correctly when click 'Printable copy' button in advanced search case result without a test case selected. '''

		time.sleep(env.ts)
		#************************************************************************************************************************************************************************
		#There is error exists here, the right title should be "INFO - At least one case is required." and the right message should be "At least one case is required.".
		#After the error get fixed, the code here shoul be changed accordingly. Related test case: tc_ID87533_PrintCopyInASearchCaseResult.py
		self.verifyPageTitle(myself,sel, "INFO - At least one plan is required.")
		self.verifyText(myself,sel,"At least one plan is required.")
		#************************************************************************************************************************************************************************

		self.verifyElement(myself,sel,"//input[@value='Return']")


	#----------------------------------------------------------------------
	#------------------ (4) 'Advanced Search Run' page --------------------
	#----------------------------------------------------------------------

	def verifyAdvancedSearchRunResultIsReady(self,myself,sel,tIdNames="<default>",tNoIdNames="<default>"):
		''' Verify advanced search result for run page is ready. The data type of the para 'tIdNames' & 'tNoIdNames' is 'dict', but 'tIds' is 'list'. '''

		time.sleep(env.tl)
		self.verifyPageTitle(myself,sel, "Advanced Search Results")
		self.verifyText(myself,sel,"Target:")
		self.verifyText(myself,sel,"run;")
		self.verifyText(myself,sel,"Search Results")

		if tIdNames!="<default>":
			if tIdNames!="":
				self.verifyLink(myself,sel,"View My Assigned Runs")
				self.verifyBtn(myself,sel,"button","Clone")

				for tId,tName in tIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: #if tIdNames=="", it indicates there will be no result searched out
				self.verifyLinkNotPresent(myself,sel,"View My Assigned Runs")
				self.verifyBtnNotPresent(myself,sel,"button","Clone")

		if tNoIdNames!="<default>":
			for tId,tName in tNoIdNames.items():
				self.verifyLinkNotPresent(myself,sel,tId)
				self.verifyLinkNotPresent(myself,sel,tName)

	def fillDataForRunItemsInASearch(self,myself,sel,productList="<default>",prodversionList="<default>",\
		buildList="<default>",runId="<default>",summary="<default>",manager="<default>",\
		defaultTester="<default>",actualTester="<default>",tag="<default>",tagOption="<default>",\
		status="<default>",runAfter="<default>",runBefore="<default>"):
		''' Fill data For Run Items In Advanced Search page. '''

		#select product
		if productList!="<default>": 
			for i in range(len(productList)):
				self.selectOptionInList(myself,sel,"r_product",productList[i])

		#select version
		if prodversionList!="<default>": 
			for i in range(len(prodversionList)):
				self.selectOptionInList(myself,sel,"r_version",prodversionList[i])

		#select build
		if buildList!="<default>": 
			for i in range(len(buildList)):
				self.selectOptionInList(myself,sel,"r_build",buildList[i])

		if runId!="<default>": self.inputText(myself,sel,"r_id",runId)
		if summary!="<default>": self.inputText(myself,sel,"r_summary",summary)
		if manager!="<default>": self.inputText(myself,sel,"r_manager",manager)
		if defaultTester!="<default>": self.inputText(myself,sel,"r_tester",defaultTester)
		if actualTester!="<default>": self.inputText(myself,sel,"r_real_tester",actualTester)
		if tag!="<default>": self.inputText(myself,sel,"r_tags",tag)

		#select tag options - Note: include 2 options: 'Contains', 'Not Contains'
		if tagOption!="<default>":
			if not self.isSelectedLabel(myself,sel,tagOption,"r_tags_exclude"):
				self.selectOptionInDropDownList(myself,sel,"r_tags_exclude",tagOption)

		#Value of this para 'status' included: 'All', 'Finished', 'Running'
		if status!="<default>":
			if not self.isSelectedLabel(myself,sel,status,"r_running"):
				self.selectOptionInDropDownList(myself,sel,"r_running",status)

		if runAfter!="<default>": self.inputText(myself,sel,"r_created_since",runAfter)
		if runBefore!="<default>": self.inputText(myself,sel,"r_created_before",runBefore)

	def selectRunInASearchRunResult(self,myself,sel,testrunIds):
		''' Select part of test runs in the Search Run Result page. The data type of the para testrunIds is 'list' type. '''

		if testrunIds == "All":
			self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="off")
			self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="on")
		else:
			self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="on")
			self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="off")
			if testrunIds != "":
				for i in range(len(testrunIds)):
					self.clickCheckBox(myself,sel,"run",testrunIds[i],onoff="on")

	def clickActionInASearchRunResult(self,myself,sel,ActionName):
		''' Click Action in Search Run Page including button or link. '''

		if ActionName == "Clone": self.clickBtnAndWait(myself,sel,"button","Clone")


