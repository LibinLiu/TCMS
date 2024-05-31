from selenium import selenium
import unittest, time, re

from env import *
import CommonElements

class CCommonPages(CommonElements.CCommonElements):


	# ========================================================================================================
	# 	Clone test plan/case/run & clone warning pages related functions
	# ========================================================================================================


	#----------------------------------------------------------------------
	#--------------------- (1) 'Clone Test Plan' page ---------------------
	#----------------------------------------------------------------------

	def verifyCloneTestPlanPageIsReady(self,myself,sel,testplanName):
		''' Verify clone one test plan page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Clone Plan")
		self.verifyTargetText(myself,sel,"Clone Test Plan","css=h2")

		self.verifyValue(myself,sel,"Copy of "+testplanName,"id_name")

		self.verifyElement(myself,sel,"//input[@value='Clone']")

	def verifyCloneMultiTestPlanPageIsReady(self,myself,sel,testplanIdNames):
		''' Verify clone multiple test plan page is ready. 'testplanIdNames' is a 'dict' type para. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Clone Plan")
		self.verifyTargetText(myself,sel,"Clone Test Plan","css=h2")

		for tId,tName in testplanIdNames.items():
			self.verifyText(myself,sel,tId)
			self.verifyLink(myself,sel,tName)

		self.verifyElement(myself,sel,"//input[@value='Clone']")

	def fillDataForCloneTestPlan(self,myself,sel,testplanName="<default>",product="<default>",prodversion="<default>",keepOriginalAuthor="<default>",\
			copyPlanDocument="<default>",copyPlanAttachments="<default>",copyEnvironmentGroup="<default>",copyAllTestCases="<default>",createACopyForCases="<default>",\
			maintainOriginalAuthorsForCases="<default>",keepDefaultTesterForCases="<default>"):
		''' Fill data in For Clone Single/Multiple Test Plan page. Note: 'testplanName' is just used for cloning 1 test plan. '''

		if testplanName !="<default>": self.inputText(myself,sel,"id_name",testplanName)

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"id_product"):
				self.selectOptionInDropDownList(myself,sel,"id_product",product)

		#select product version
		if prodversion!="<default>": 
			if not self.isSelectedLabel(myself,sel,prodversion,"id_default_product_version"):
				self.selectOptionInDropDownList(myself,sel,"id_default_product_version",prodversion)

		#Note: all below 8 paras' value just involves: 'on', 'off'
		if keepOriginalAuthor!="<default>": self.clickCheckBox(myself,sel,"id_keep_orignal_author","",onoff=keepOriginalAuthor)
		if copyPlanDocument!="<default>": self.clickCheckBox(myself,sel,"id_copy_texts","",onoff=copyPlanDocument)
		if copyPlanAttachments!="<default>": self.clickCheckBox(myself,sel,"id_copy_attachements","",onoff=copyPlanAttachments)
		if copyEnvironmentGroup!="<default>": self.clickCheckBox(myself,sel,"id_copy_environment_group","",onoff=copyEnvironmentGroup)
		if copyAllTestCases!="<default>": self.clickCheckBox(myself,sel,"id_link_testcases","",onoff=copyAllTestCases)
		if createACopyForCases!="<default>": self.clickCheckBox(myself,sel,"id_copy_testcases","",onoff=createACopyForCases)
		if maintainOriginalAuthorsForCases!="<default>": self.clickCheckBox(myself,sel,"id_maintain_case_orignal_author","",onoff=maintainOriginalAuthorsForCases)
		if keepDefaultTesterForCases!="<default>": self.clickCheckBox(myself,sel,"id_keep_case_default_tester","",onoff=keepDefaultTesterForCases)

	def clickActionInCloneTestPlan(self,myself,sel,ActionName):
		''' Click Action in Clone Test Plan Page including button or link. '''

		if ActionName == "Clone": self.clickBtnAndWait(myself,sel,"submit","Clone")
		elif ActionName == "Cancel": self.clickBtnAndWait(myself,sel,"button","Cancel")


	#----------------------------------------------------------------------
	#-------------------- (2) 'Clone Test Case' page ----------------------
	#----------------------------------------------------------------------

	def verifyCloneTestCasePageIsReady(self,myself,sel,testcaseIdNames):
		''' Verify clone single/multiple test case(s) page is ready. 'testcaseIdNames' is a 'dict' type para. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Clone Test Case")
		self.verifyTargetText(myself,sel,"Clone Test Case(s)","css=h2")

		for tId,tName in testcaseIdNames.items():
			self.verifyCheckBox(myself,sel,"on","case",tId)
			self.verifyText(myself,sel,tName)

		self.verifyElement(myself,sel,"//input[@value='Clone']")

	def fillDataForCloneTestCase(self,myself,sel,selectPlan="<default>",planId="<default>",product="<default>",prodversion="<default>",\
			planType="<default>",envGroup="<default>",planAuthor="<default>",tag="<default>",planSummary="<default>",active="<default>",\
			selectFilterPlanIds="<default>",selectCloneCaseIds="<default>",unSelectCloneCaseIds="<default>",createACopy="<default>",\
			keepOriginalAuthor="<default>",keepOriginalDefaultTester="<default>",copyComponentToNewProduct="<default>",\
			copyAttachmentsToNewProduct="<default>"):
		''' Fill data in For Clone Test Cases page. '''

		if selectPlan=="<default>": selectPlan="Use Filterplan"
		if selectPlan=="Use Sameplan":
			self.clickRadioBtn(myself,sel,"id_use_sameplan","",onoff="on")
		elif selectPlan=="Use Filterplan":
			self.clickRadioBtn(myself,sel,"id_use_filterplan","",onoff="on")
			
			if planId!="<default>": self.inputText(myself,sel,"id_pk__in",planId)

			#select product
			if product!="<default>": 
				if not self.isSelectedLabel(myself,sel,product,"id_product"):
					self.selectOptionInDropDownList(myself,sel,"id_product",product)

			#select product version
			if prodversion!="<default>": 
				if not self.isSelectedLabel(myself,sel,prodversion,"id_default_product_version"):
					self.selectOptionInDropDownList(myself,sel,"id_default_product_version",prodversion)

			#select product type
			if planType!="<default>": 
				if not self.isSelectedLabel(myself,sel,planType,"id_type"):
					self.selectOptionInDropDownList(myself,sel,"id_type",planType)

			#select Environment Group
			if envGroup!="<default>": 
				if not self.isSelectedLabel(myself,sel,envGroup,"id_env_group"):
					self.selectOptionInDropDownList(myself,sel,"id_env_group",envGroup)

			if planAuthor!="<default>": self.inputText(myself,sel,"id_author__email__startswith",planAuthor)
			if tag!="<default>": self.inputText(myself,sel,"id_tag__name__in",tag)
			if planSummary!="<default>": self.inputText(myself,sel,"id_name__icontains",planSummary)

			#Note: The value of the para 'active' just involves: 'on', 'off'
			if active!="<default>":
				self.clickCheckBox(myself,sel,"id_is_active","",onoff=active)

			self.clickActionInCloneTestCase(myself,sel,"Filter plan")

			if selectFilterPlanIds!="<default>":
				for i in range(len(selectFilterPlanIds)):
					self.clickCheckBox(myself,sel,"",selectFilterPlanIds[i],onoff="on")

		if selectCloneCaseIds!="<default>":
			for i in range(len(selectCloneCaseIds)):
				self.clickCheckBox(myself,sel,"",selectCloneCaseIds[i],onoff="on")

		if unSelectCloneCaseIds!="<default>":
			for i in range(len(unSelectCloneCaseIds)):
				self.clickCheckBox(myself,sel,"",unSelectCloneCaseIds[i],onoff="off")

		#Note: all below 5 paras' value just involves: 'on', 'off'
		if createACopy!="<default>": self.clickCheckBox(myself,sel,"id_copy_case","",onoff=createACopy)
		if keepOriginalAuthor!="<default>": self.clickCheckBox(myself,sel,"id_maintain_case_orignal_author","",onoff=keepOriginalAuthor)
		if keepOriginalDefaultTester!="<default>": self.clickCheckBox(myself,sel,"id_maintain_case_orignal_default_tester","",onoff=keepOriginalDefaultTester)
		if copyComponentToNewProduct!="<default>": self.clickCheckBox(myself,sel,"id_copy_component","",onoff=copyComponentToNewProduct)
		if copyAttachmentsToNewProduct!="<default>": self.clickCheckBox(myself,sel,"id_copy_attachment","",onoff=copyAttachmentsToNewProduct)

	def clickActionInCloneTestCase(self,myself,sel,ActionName):
		''' Click Action in Clone Test Case Page including button or link. '''

		if ActionName == "Filter plan": self.clickBtn(myself,sel,"submit","Filter plan")
		elif ActionName == "Clone": self.clickBtnAndWait(myself,sel,"submit","Clone")
		elif ActionName == "Cancel": self.clickBtnAndWait(myself,sel,"button","Cancel")

	def saveCloneTestCase(self,myself,sel,selectPlan="<default>",planId="<default>",product="<default>",prodversion="<default>",\
			planType="<default>",envGroup="<default>",planAuthor="<default>",tag="<default>",planSummary="<default>",active="<default>",\
			selectFilterPlanIds="<default>",selectCloneCaseIds="<default>",unSelectCloneCaseIds="<default>",createACopy="<default>",\
			keepOriginalAuthor="<default>",keepOriginalDefaultTester="<default>",copyComponentToNewProduct="<default>",\
			copyAttachmentsToNewProduct="<default>"):
		
		self.fillDataForCloneTestCase(myself,sel,selectPlan,planId,product,prodversion,\
			planType,envGroup,planAuthor,tag,planSummary,active,selectFilterPlanIds,\
			selectCloneCaseIds,unSelectCloneCaseIds,createACopy,keepOriginalAuthor,\
			keepOriginalDefaultTester,copyComponentToNewProduct,copyAttachmentsToNewProduct)

		self.clickActionInCloneTestCase(myself,sel,"Clone")


	#----------------------------------------------------------------------
	#----------------- (3) 'Clone Single Test Run' page -------------------
	#----------------------------------------------------------------------

	def verifyCloneTestRunPageIsReady(self,myself,sel,testrunName,testcaseIdNames="<default>",testcaseNoIdNames="<default>"):
		''' Verify clone test run page is ready. '''

		time.sleep(env.t)
		self.verifyTargetText(myself,sel,"Clone Test Run - "+testrunName,"css=h2")
		self.verifyElement(myself,sel,"//input[@value='Save']") #Bug: the Save button should be named as 'Clone'

		if testcaseIdNames!="<default>":
			if testcaseIdNames!="":
				for tId,tName in testcaseIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)
			else:
				#if testcaseIdNames=="", it indicates there should be no test case run exists
				self.verifyLinkNotPresent(myself,sel,"remove")

		if testcaseNoIdNames!="<default>":
			if testcaseNoIdNames!="":
				for tId,tName in testcaseNoIdNames.items():
					self.verifyLinkNotPresent(myself,sel,tId)
					self.verifyLinkNotPresent(myself,sel,tName)

	def fillDataForCloneSingleTestRun(self,myself,sel,summary="<default>",product="<default>",prodversion="<default>",\
		build="<default>",runmanager="<default>",defaulttester="<default>",estdays="<default>",\
		esthours="<default>",estmins="<default>",estsecs="<default>",notes="<default>",environment="<default>",\
		reserveStatus="<default>",reserveAssignee ="<default>"):
		''' Fill data in For Clone Single Test Run page. '''

		#input summary of new test run
		if summary!="<default>": self.inputText(myself,sel,"id_summary", summary)

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

		#add Run Manager
		if runmanager!="<default>": self.inputText(myself,sel,"id_manager", runmanager)

		#add Default Tester
		if defaulttester!="<default>": self.inputText(myself,sel,"id_default_tester", defaulttester)

		#add estimated days
		if estdays!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_days']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_days",estdays)
		#add estimated hours
		if esthours!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_hours']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_hours",esthours)
		#add estimated minutes
		if estmins!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_minutes']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_minutes",estmins)
		#add estimated seconds
		if estsecs!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_seconds']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_seconds",estsecs)

		#add notes
		if notes!="<default>": self.inputText(myself,sel,"id_notes", notes)

		#Select/unselect environment, the value of 'environment' should be: 'on', 'off'
		if environment!="<default>":
			self.clickCheckBox(myself,sel,"","",fieldTarget="//input[@class='lab-50']",onoff=environment)


		# Checked/unchecked 'Reserve Status' according to the value of 'reserveStatus': 'on', 'off'
		if reserveStatus!="<default>":
			self.clickCheckBox(myself,sel,"id_keep_status","",onoff=reserveStatus)

		# Checked/unchecked 'Reserve Assignee' according to the value of 'reserveAssignee': 'on', 'off'
		if reserveAssignee!="<default>":
			self.clickCheckBox(myself,sel,"id_keep_assignee","",onoff=reserveAssignee)

	def clickActionInCloneTestRun(self,myself,sel,ActionName):
		''' Click Action in Search Run Page including button or link. '''

		if ActionName == "Save": self.clickBtnAndWait(myself,sel,"submit","Save")
		elif ActionName == "Cancel": self.clickBtnAndWait(myself,sel,"button","cancel")

	def removeCaseInCloneTestRun(self,myself,sel,testcaseName):
		''' Remove a case in Clone Test Run. '''

		#Check the test cases list has been shown, that is, there should be at least one test case exists
		self.verifyElement(myself,sel,"link_1")

		#Remove test case in clone test run - the scope is just limited in the first 20 cases
		for r in range(1,20):
			try:
				if self.isTargetText(myself,sel,testcaseName,"link_"+str(r)):
				      self.clickElement(myself,sel,"//tr[@id='row_"+str(r)+"']/td[10]/a")
			except: pass


	#----------------------------------------------------------------------
	#---------------- (4) 'Clone Multiple Test Run' page ------------------
	#----------------------------------------------------------------------

	def verifyCloneMultiTestRunPageIsReady(self,myself,sel,testrunIdNames):
		''' Verify clone test run page is ready. 'testrunIdNames' is a 'dict' type para. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Clone test runs")
		self.verifyTargetText(myself,sel,"The runs you have choosed","css=div.boxtitle")
		self.verifyElement(myself,sel,"//input[@value='Clone']")

		for tId,tName in testrunIdNames.items():
			self.verifyCheckBox(myself,sel,"on","run",tId)
			self.verifyText(myself,sel,tName)

	def fillDataForCloneMultiTestRun(self,myself,sel,testrunIdOnoffs="<default>",product="<default>",prodversion="<default>",build="<default>",\
			runmanager="<default>",defaulttester="<default>",assignee="<default>",updatemanager="<default>",updatedefaulttester="<default>",\
			updateassignee="<default>",updatecasetext="<default>",clonecc="<default>",clonetag="<default>"):
		''' Fill data in Search Run page. 

		    An example of the value of testrunIdOnoffs: {testrunId1:"on",testrunId2:"off"}

		    The value of below paras just includes "on" and "off": updatemanager, updatedefaulttester, updateassignee, updatecasetext, clonecc, clonetag

		'''

		if testrunIdOnoffs!="<default>":
			for trId,trOnoff in testrunIdOnoffs.items():
				self.clickCheckBox(myself,sel,"run",trId,onoff=trOnoff)

		if runmanager !="<default>": self.inputText(myself,sel,"id_manager",runmanager)
		if defaulttester!="<default>": self.inputText(myself,sel,"id_default_tester",defaulttester)
		if assignee!="<default>": self.inputText(myself,sel,"id_assignee",assignee)

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

		if updatemanager!="<default>": self.clickCheckBox(myself,sel,"id_update_manager","",onoff=updatemanager)
		if updatedefaulttester!="<default>": self.clickCheckBox(myself,sel,"id_update_default_tester","",onoff=updatedefaulttester)
		if updateassignee!="<default>": self.clickCheckBox(myself,sel,"id_update_assignee","",onoff=updateassignee)
		if updatecasetext!="<default>": self.clickCheckBox(myself,sel,"id_update_case_text","",onoff=updatecasetext)
		if clonecc!="<default>": self.clickCheckBox(myself,sel,"id_clone_cc","",onoff=clonecc)
		if clonetag!="<default>": self.clickCheckBox(myself,sel,"id_clone_tag","",onoff=clonetag)

	def clickActionInCloneMultiTestRun(self,myself,sel,ActionName):
		''' Click Action in Clone Multiple Test Run Page including button or link. '''

		if ActionName == "Clone": self.clickBtnAndWait(myself,sel,"submit","Clone")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")
		elif ActionName == "Cancel": self.clickBtnAndWait(myself,sel,"button","Cancel")

	def verifyErrWarningMsgInCloneMultiTestRun(self,myself,sel,errType,wrongUser=""):
		''' Verify the error warning message in clone multiple test runs. '''

		if errType == "Blank Build":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")
			self.verifyTargetText(myself,sel,"buildThis field is required.","css=form > div.errors > ul.errorlist > li")
		elif errType == "Invalid Run Manager":
			self.verifyTargetText(myself,sel,"Unknown user: \""+wrongUser+"\"","css=ul.errorlist > li")
			self.verifyTargetText(myself,sel,"managerUnknown user: \""+wrongUser+"\"","css=form > div.errors > ul.errorlist > li")
		elif errType == "Invalid Default Tester":
			self.verifyTargetText(myself,sel,"Unknown user: \""+wrongUser+"\"","css=ul.errorlist > li")
			self.verifyTargetText(myself,sel,"default_testerUnknown user: \""+wrongUser+"\"","css=form > div.errors > ul.errorlist > li")
		elif errType == "Invalid Assignee":
			self.verifyTargetText(myself,sel,"Unknown user: \""+wrongUser+"\"","css=ul.errorlist > li")
			self.verifyTargetText(myself,sel,"default_testerUnknown user: \""+wrongUser+"\"","css=form > div.errors > ul.errorlist > li")


	#----------------------------------------------------------------------
	#----------------- (5) Clone Warning pages functions--------------------
	#----------------------------------------------------------------------

	def verifyCloneWarningPage(self,myself,sel,warnMsgType):
		''' Verify clone warning page is shown when click Clone in advanced search plan/case/run result page and make sure the warning message is correct. '''

		time.sleep(env.t)
		if warnMsgType == "Plan":
			self.verifyPageTitle(myself,sel,"INFO - At least one plan is required by clone function.")
			self.verifyText(myself,sel,"At least one plan is required by clone function.")

		elif warnMsgType == "Case":
			self.verifyPageTitle(myself,sel,"INFO - At least one case is required.")
			self.verifyText(myself,sel,"At least one case is required.")

		elif warnMsgType == "Run":
			self.verifyPageTitle(myself,sel,"INFO - At least one run is required")
			self.verifyText(myself,sel,"At least one run is required")

	def clickContinueInCloneWarningPage(self,myself,sel):
		''' Click Continue in clone warning page. '''

		self.clickLink(myself,sel,"Continue")


	# ========================================================================================================
	# 	'Environment -> Groups' page related functions
	# ========================================================================================================


	def verifyEnvGroupsPageIsReady(self,myself,sel):
		'''Verify Environment Groups page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"Environment groups")
		self.verifyTargetText(myself,sel,"Environment Groups","css=h2")
		self.verifyLink(myself,sel,"Add new group")

	def verifyEditEnvGroupsPageIsReady(self,myself,sel,groupName,isSaved=False):
		'''Verify Edit Environment Groups page is ready. 
		   Note, the function is applicable to the scenario of adding env group successfully by clicking 'Save', 
		   In this case, just set 'isSave' as 'True' to do extra verification. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"Edit Environment group")
		self.verifyTargetText(myself,sel,"Edit Environment Group","css=h2")
		self.verifyLink(myself,sel,"Edit")

		self.verifyValue(myself,sel,groupName,"name")

		if isSaved:
			self.verifyTargetText(myself,sel,"Environment group saved successfully.","css=span.successlink")

	def clickActionInEditEnvGroupsPage(self,myself,sel,ActionName):
		''' Click a button or link in the Edit Environment Groups page. '''

		if ActionName == "Save": self.clickBtn(myself,sel,"submit","Save")
		elif ActionName == "Back": self.clickBtn(myself,sel,"button","Back")

		if ActionName == "Add": self.clickLink(myself,sel,"Add")
		elif ActionName == "Remove": self.clickLink(myself,sel,"Remove")

	def searchGroupInEnvGroupsPage(self,myself,sel,groupName):
		'''Search a Group in Environment Groups page. '''

		self.inputText(myself,sel,"searchbar", groupName)
		self.clickBtn(myself,sel,"submit","Search environment group")

		self.verifyLink(myself,sel,groupName)

	def addGroupInEnvGroupsPage(self,myself,sel,groupName):
		'''Add a Group in Environment Groups page. '''

		sel.answer_on_next_prompt(groupName)
		self.clickLink(myself,sel,"Add new group")
		myself.assertEqual("New environment group name", sel.get_prompt())
		time.sleep(env.ts)

		self.verifyEditEnvGroupsPageIsReady(myself,sel,groupName,isSaved=False)

		self.clickActionInEditEnvGroupsPage(myself,sel,"Save")
		self.verifyEditEnvGroupsPageIsReady(myself,sel,groupName,isSaved=True)

	def activateGroupInEnvGroupsPage(self,myself,sel,groupName,action="Enable"):
		'''Enable or Disable a Group in Environment Groups page. '''

		if not self.isLink(myself,sel,groupName):
			self.searchGroupInEnvGroupsPage(myself,sel,groupName)

		self.verifyLink(myself,sel,groupName)
		for r in range(1,1000):
			if self.isTargetText(myself,sel,groupName,"//tr["+str(r)+"]/th/label/a"):

				if action=="Enable":
					self.clickElement(myself,sel,"//tr["+str(r)+"]/td[4]/a[3]") #click "Enable" link
					self.verifyElement(myself,sel,"//tr["+str(r)+"]/td[4]/a[2]")

				elif action=="Disable":
					self.clickElement(myself,sel,"//tr["+str(r)+"]/td[4]/a[2]") #click "Disable" link
					self.verifyElement(myself,sel,"//tr["+str(r)+"]/td[4]/a[3]")
				break

	def removeGroupInEnvGroupsPage(self,myself,sel,groupName):
		'''Remove a Group in Environment Groups page. '''

		if not self.isLink(myself,sel,groupName):
			self.searchGroupInEnvGroupsPage(myself,sel,groupName)

		self.verifyLink(myself,sel,groupName)
		for r in range(1,1000):
			if self.isTargetText(myself,sel,groupName,"//tr["+str(r)+"]/th/label/a"):

				self.clickElement(myself,sel,"//tr["+str(r)+"]/td[4]/a[4]") #click "Delete" link
				myself.assertEqual("Are you sure you wish to remove environment group - "+groupName, sel.get_confirmation())
				time.sleep(env.ts)

				self.verifyLinkNotPresent(myself,sel,groupName)
				break


	# ========================================================================================================
	# 	'Admin -> Management' page related functions
	# ========================================================================================================


	def verifyManagementPageIsReady(self,myself,sel):
		'''Verify Management administration page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"Management administration")
		self.verifyTargetText(myself,sel,"Management","css=a.section")
		self.verifyLink(myself,sel,"Builds")
		self.verifyElement(myself,sel,"//a[contains(@href, 'testbuild/add/')]")

	def addBuildFromManagementPage(self,myself,sel,buildName,product,ActionName="Save"):
		'''Add Build from 'Admin -> Management' Page. '''

		self.clickElement(myself,sel,"//a[contains(@href, 'testbuild/add/')]")
		self.verifyPageTitle(myself,sel,"Add build")
		self.verifyTargetText(myself,sel,"Add build","css=h2")

		self.inputText(myself,sel,"id_name",buildName)
		self.selectOptionInDropDownList(myself,sel,"id_product",product)

		if ActionName == "Save": self.clickBtnAndWait(myself,sel,"submit","Save")
		elif ActionName == "Save and add another": self.clickBtnAndWait(myself,sel,"submit","Save and add another")
		elif ActionName == "Save and continue editing": self.clickBtnAndWait(myself,sel,"submit","Save and continue editing")

	def verifySelectBuildToChangePageIsReady(self,myself,sel):
		'''Verify the 'Select build to change' page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"Select build to change")
		self.verifyTargetText(myself,sel,"Select build to change","css=h2")
		self.verifyElement(myself,sel,"searchbar")

	def searchBuildToVerify(self,myself,sel,buildName):
		'''Search Build in the 'Select build to change' page to make sure if it exists. '''

		self.inputText(myself,sel,"searchbar",buildName)
		self.clickElement(myself,sel,"//input[@value='Search']")
		self.verifyText(myself,sel,buildName)


	# ========================================================================================================
	# 	'Reporting -> Testing Report' page related functions
	# ========================================================================================================


	def verifyTestingReportPageIsReady(self,myself,sel):
		'''Verify Testing Report page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"CaseRun Report")
		self.verifyTargetText(myself,sel,"Testing Report","css=h2")
		self.verifyElement(myself,sel,"//input[@value='Generate Report']")

	def verifyTestingReportResultPageIsReady(self,myself,sel,product="<default>",prodversionList="<default>",\
		buildList="<default>",executeDateAfter="<default>",executeDateBefore="<default>",reportType="<default>",\
		verifyOptions=False):
		'''Verify Testing Report page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"CaseRun Report")
		self.verifyTargetText(myself,sel,"Testing Report","css=h2")
		self.verifyElement(myself,sel,"//input[@value='Generate Report']")

		#(1)verify testing report options
		if verifyOptions:
			if product!="<default>": 
				self.verifySelectedLabel(myself,sel,product,"r_product")

			if prodversionList!="<default>": 
				self.verifySelectedLabels(myself,sel,prodversionList,"r_version")

			if buildList!="<default>": 
				self.verifySelectedLabels(myself,sel,buildList,"r_build")

			if executeDateAfter!="<default>": self.verifyValue(myself,sel,executeDateAfter,"r_created_since")
			if executeDateBefore!="<default>": self.verifyValue(myself,sel,executeDateBefore,"r_created_before")

			if reportType!="<default>": 
				if reportType == "By Case-Run Tester":
					self.verifyRadioBtn(myself,sel,"on","report_type","per_build_report")
				elif reportType == "By Case Priority":
					self.verifyRadioBtn(myself,sel,"on","report_type","per_priority_report")
				elif reportType == "By Plan's Tag":
					self.verifyRadioBtn(myself,sel,"on","report_type","runs_with_rates_per_plan_tag")

		#(2)verify testing report result
		if product!="<default>": 
			productStr = product+";"
			self.verifyText(myself,sel,productStr)

		if prodversionList!="<default>": 
			self.verifyText(myself,sel,"Run Version:")
			for i in range(len(prodversionList)):
				self.verifyText(myself,sel,prodversionList[i])

		if buildList!="<default>": 
			self.verifyText(myself,sel,"Run Build:")
			for i in range(len(buildList)):
				self.verifyText(myself,sel,buildList[i])

		self.verifyElement(myself,sel,"//body[@id='body']/table/tbody")

	def generateTestingReport(self,myself,sel,product="<default>",prodversionList="<default>",buildList="<default>",\
		executeDateAfter="<default>",executeDateBefore="<default>",reportType="<default>",verifyOptions=False):
		'''Generate Testing Report. '''

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"r_product"):
				self.selectOptionInDropDownList(myself,sel,"r_product",product)

		#select version
		if prodversionList!="<default>": 
			for i in range(len(prodversionList)):
				self.selectOptionInList(myself,sel,"r_version",prodversionList[i])

		#select Build
		if buildList!="<default>": 
			for i in range(len(buildList)):
				self.selectOptionInList(myself,sel,"r_build",buildList[i])

		if executeDateAfter!="<default>": self.inputText(myself,sel,"r_created_since",executeDateAfter)
		if executeDateBefore!="<default>": self.inputText(myself,sel,"r_created_before",executeDateBefore)

		#select report type
		if reportType!="<default>": 
			if reportType == "By Case-Run Tester":
				self.clickRadioBtn(myself,sel,"report_type","per_build_report",onoff="on")
			elif reportType == "By Case Priority":
				self.clickRadioBtn(myself,sel,"report_type","per_priority_report",onoff="on")
			elif reportType == "By Plan's Tag":
				self.clickRadioBtn(myself,sel,"report_type","runs_with_rates_per_plan_tag",onoff="on")

		self.clickBtn(myself,sel,"submit","Generate Report")
		time.sleep(env.ts)

		self.verifyTestingReportResultPageIsReady(myself,sel,product,prodversionList,buildList,\
		executeDateAfter,executeDateBefore,reportType,verifyOptions)


	# ========================================================================================================
	# 	Some Sub-window pages related functions
	# ========================================================================================================


	#----------------------------------------------------------------------
	#------------------- (1) 'Add Product Version' page -------------------
	#----------------------------------------------------------------------

	def verifyAddProductVersionPageIsReady(self,myself,sel,prodverPageId="default_product_version",prodversion="<default>",product="<default>"):
		''' Verify Add Product Version page is ready. '''

		time.sleep(env.ts)

		#Note:
		#If the 'Add Product Version' window is opened from the create plan page, the value of 'prodverPageId' is "default_product_version"
		#If the 'Add Product Version' window is opened from the create run page, the value of 'prodverPageId' is "product_version"
		if prodverPageId=="default_product_version": sel.select_window("name=id_default_product_version")
		elif prodverPageId=="product_version": sel.select_window("name=id_product_version")

		self.verifyPageTitle(myself,sel,"Add version")
		self.verifyTargetText(myself,sel,"Add version","css=h2")

		if prodversion!="<default>": self.verifyValue(myself,sel,prodversion,"id_value")
		if product!="<default>": self.verifySelectedLabel(myself,sel,product,"id_product")

	def fillDataForAddProductVersionPage(self,myself,sel,prodversion="<default>",product="<default>"):
		''' Fill the data for Add Product Version page. '''

		if prodversion!="<default>": self.inputText(myself,sel,"id_value", prodversion)

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"id_product"):
				self.selectOptionInDropDownList(myself,sel,"id_product",product)

	def clickActionInAddProductVersionPage(self,myself,sel,ActionName):
		''' Click Action in Add Product Version page including button or link. '''

		if ActionName == "Save":
			self.clickBtn(myself,sel,"submit","Save")

		elif ActionName == "Add Product":
			self.clickElement(myself,sel,"//img[@alt='Add Another']")
			sel.wait_for_pop_up("id_product", "30000")
			time.sleep(env.ts)

	def verifyErrWarningMsgInAddProductVersionPage(self,myself,sel,errType):
		''' Verify the error warning message when Add Product Version. '''

		if errType == "Blank Product Version":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")


	#----------------------------------------------------------------------
	#----------------------- (2) 'Add Product' page -----------------------
	#----------------------------------------------------------------------

	def verifyAddProductPageIsReady(self,myself,sel,product="<default>",classification="<default>",\
		description="<default>",disallowNew="<default>",votesToConfirm="<default>"):
		''' Verify Add Product page is ready. '''

		time.sleep(env.ts)
		sel.select_window("name=id_product")
		self.verifyPageTitle(myself,sel,"Add product")
		self.verifyTargetText(myself,sel,"Add product","css=h2")

		if product!="<default>": self.verifyValue(myself,sel,product,"id_product")
		if classification!="<default>": self.verifySelectedLabel(myself,sel,classification,"id_classification")
		if description!="<default>": self.verifyValue(myself,sel,description,"id_description")
		if disallowNew!="<default>": self.verifyCheckBox(myself,sel,disallowNew,"id_disallow_new","")
		if votesToConfirm!="<default>": self.verifyCheckBox(myself,sel,votesToConfirm,"id_votes_to_confirm","")

	def fillDataForAddProductPage(self,myself,sel,product="<default>",classification="<default>",\
		description="<default>",disallowNew="<default>",votesToConfirm="<default>"):
		''' Fill the data for Add Product page. '''

		if product!="<default>": self.inputText(myself,sel,"id_name",product)

		if classification!="<default>": 
			if not self.isSelectedLabel(myself,sel,classification,"id_classification"):
				self.selectOptionInDropDownList(myself,sel,"id_classification",classification)

		if description!="<default>": self.inputText(myself,sel,"id_description", description)

		if disallowNew!="<default>":
			self.clickCheckBox(myself,sel,"id_disallow_new","",onoff=disallowNew)

		if votesToConfirm!="<default>":
			self.clickCheckBox(myself,sel,"id_votes_to_confirm","",onoff=votesToConfirm)

	def clickActionInAddProductPage(self,myself,sel,ActionName):
		''' Click Action in Add Product page including button or link. '''

		if ActionName == "Save":
			self.clickBtn(myself,sel,"submit","Save")

		elif ActionName == "Add Classification":
			self.clickElement(myself,sel,"//img[@alt='Add Another']")
			sel.wait_for_pop_up("id_product", "30000")
			time.sleep(env.ts)

	def verifyErrWarningMsgInAddProductPage(self,myself,sel,errType):
		''' Verify the error warning message when Add Product. '''

		if errType == "Blank Product":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")
		if errType == "Existing Product":
			self.verifyTargetText(myself,sel,"Product with this Name already exists.","css=ul.errorlist > li")
		elif errType == "Blank Classification":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")


	#----------------------------------------------------------------------
	#-------------------- (3) 'Add Classification' page -------------------
	#----------------------------------------------------------------------

	def verifyAddClassificationPageIsReady(self,myself,sel,classification="<default>",description="<default>",sortkey="<default>"):
		''' Verify Add Classification page is ready. '''

		time.sleep(env.ts)
		sel.select_window("name=id_classification")
		self.verifyPageTitle(myself,sel,"Add classification")
		self.verifyTargetText(myself,sel,"Add classification","css=h2")

		if classification!="<default>": self.verifyValue(myself,sel,classification,"id_name")
		if description!="<default>": self.verifyValue(myself,sel,description,"id_description")
		if sortkey!="<default>": self.verifyValue(myself,sel,sortkey,"id_sortkey")

	def fillDataForAddClassificationPage(self,myself,sel,classification="<default>",description="<default>",sortkey="<default>"):
		''' Fill the data for Add Classification page. '''

		if classification!="<default>": self.inputText(myself,sel,"id_name", classification)
		if description!="<default>": self.inputText(myself,sel,"id_description", description)
		if sortkey!="<default>": self.inputText(myself,sel,"id_sortkey", sortkey)

	def clickActionInAddClassificationPage(self,myself,sel,ActionName):
		''' Click Action in Add Classification page including button or link. '''

		if ActionName == "Save":
			self.clickBtn(myself,sel,"submit","Save")

	def verifyErrWarningMsgInAddClassificationPage(self,myself,sel,errType):
		''' Verify the error warning message when Add Classification. '''

		if errType == "Blank Classification Name":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")


	#----------------------------------------------------------------------
	#------------------------ (4) 'Add Build' page ------------------------
	#----------------------------------------------------------------------

	def verifyAddBuildPageIsReady(self,myself,sel,build="<default>",product="<default>",description="<default>",isActive="<default>"):
		''' Verify Add Build page is ready. '''

		time.sleep(env.ts)
		sel.select_window("name=id_build")
		self.verifyPageTitle(myself,sel,"Add build")
		self.verifyTargetText(myself,sel,"Add build","css=h2")

		if build!="<default>": self.verifyValue(myself,sel,build,"id_name")
		if product!="<default>": self.verifySelectedLabel(myself,sel,product,"id_product")
		if description!="<default>": self.verifyValue(myself,sel,description,"id_description")
		if isActive!="<default>": self.verifyCheckBox(myself,sel,isActive,"id_is_active","")
		
	def fillDataForAddBuildPage(self,myself,sel,build="<default>",product="<default>",description="<default>",isActive="<default>"):
		''' Fill the data for Add Build page. '''

		if build!="<default>": self.inputText(myself,sel,"id_name", build)

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"id_product"):
				self.selectOptionInDropDownList(myself,sel,"id_product",product)

		if description!="<default>": self.inputText(myself,sel,"id_description", description)

		if isActive!="<default>":
			self.clickCheckBox(myself,sel,"id_is_active","",onoff=isActive)

	def clickActionInAddBuildPage(self,myself,sel,ActionName):
		''' Click Action in Add Build page including button or link. '''

		if ActionName == "Save":
			self.clickBtn(myself,sel,"submit","Save")

		elif ActionName == "Add Product":
			self.clickElement(myself,sel,"//img[@alt='Add Another']")
			sel.wait_for_pop_up("id_product", "30000")
			time.sleep(env.ts)

	def verifyErrWarningMsgInAddBuildPage(self,myself,sel,errType):
		''' Verify the error warning message when Add Build. '''

		if errType == "Blank Build":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")
		elif errType == "Existing Build":
			self.verifyTargetText(myself,sel,"Build with this Product and Name already exists.","css=div.sub > ul > li")
		elif errType == "Blank Product":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")


	# ========================================================================================================
	# 	Other WebSite pages related functions
	# ========================================================================================================


	def verifyBugPageIsReady(self,myself,sel,bugNo):
		''' Verify bug page is ready. '''

		time.sleep(env.t)
		self.verifyText(myself,sel,"Red Hat Bugzilla")
		self.verifyText(myself,sel,"Bug "+bugNo)

	def verifyReleaseSchedulePageIsReady(self,myself,sel):
		''' Verify Release Schedule page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Nitrate - Trac")
		self.verifyElement(myself,sel,"//img[@alt='Nitrate Project Page']")

