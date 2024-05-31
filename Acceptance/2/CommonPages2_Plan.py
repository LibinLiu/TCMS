from selenium import selenium
import unittest, time, re

from env import *
import CommonElements

class CCommonPages(CommonElements.CCommonElements):


	# ========================================================================================================
	# 	Test Plan pages related functions
	# ========================================================================================================


	#-----------------------------------------------------------------------
	#-------------------- (1) Test Plan 'Create' page ----------------------
	#-----------------------------------------------------------------------

	def verifyCreateTestPlanPageIsReady(self,myself,sel,product="<default>",prodversion="<default>"):
		''' Verify create test plan page is ready. '''

		time.sleep(env.t)
		sel.select_window("null")
		self.verifyTargetText(myself,sel,"Create New Test Plan","css=h2")
		self.verifyElement(myself,sel,"//input[@value='Create test plan']")
		self.verifyElement(myself,sel,"//input[@value='Cancel']")

		if product!="<default>": self.verifySelectedLabel(myself,sel,product,"id_product")
		if prodversion!="<default>": self.verifySelectedLabel(myself,sel,prodversion,"id_default_product_version")

	def fillDataForTestPlan(self,myself,sel,planname="<default>",product="<default>",prodversion="<default>",\
		typename="<default>",uploadPlanDocName="<default>",parentID="<default>",envGroup="<default>",referenceLink="<default>"):

		''' Fill the data for a new or edit test plan form with provided data. '''

		#input plan name
		if planname!="<default>": self.inputText(myself,sel,"id_name", planname)

		#select product
		if product!="<default>": 
			if not product == sel.get_selected_label("//select[@name='product']"):
				self.selectOptionInDropDownList(myself,sel,"product",product)

		#select product version
		if prodversion!="<default>": 
			if not prodversion == sel.get_selected_label("//select[@name='default_product_version']"):
				self.selectOptionInDropDownList(myself,sel,"default_product_version",prodversion)

		#add Type
		if typename!="<default>": 
			if not typename == sel.get_selected_label("//select[@id='id_type']"):
				self.selectOptionInDropDownList(myself,sel,"id_type",typename)

		#add Parent ID
		if parentID!="<default>": self.inputText(myself,sel,"id_parent", parentID)

		#upload plan document, an example to set the para 'uploadPlanDocName':
		#uploadPlanDocName = os.path.dirname(os.path.abspath(__file__)) + os.sep + "testdata.sh"
		if uploadPlanDocName!="<default>": self.inputText(myself,sel,"id_upload_plan_text", uploadPlanDocName)

		#select Environment Group
		if envGroup!="<default>": 
			if not envGroup == sel.get_selected_label("//select[@name='env_group']"):
				self.selectOptionInDropDownList(myself,sel,"env_group",envGroup)

		#add Reference Link
		if referenceLink!="<default>": self.inputText(myself,sel,"id_extra_link", referenceLink)

	def clickActionInCreateTestPlan(self,myself,sel,ActionName):
		''' Click Action in new test plan including button or link. '''

		if ActionName == "Create test plan": self.clickBtnAndWait(myself,sel,"submit","Create test plan")
		elif ActionName == "Cancel": self.clickBtnAndWait(myself,sel,"button","Cancel")

		if ActionName == "Add Product":
			self.clickLink(myself,sel,"Add Product")
			sel.wait_for_pop_up("id_product", "30000")
			time.sleep(env.ts)

		elif ActionName == "Add Product Version":
			self.clickLink(myself,sel,"Add Product Version")
			sel.wait_for_pop_up("id_default_product_version", "30000")
			time.sleep(env.ts)


	#---------------------------------------------------------------------
	#-------------------- (2) Test Plan 'Edit' page ----------------------
	#---------------------------------------------------------------------

	def verifyEditTestPlanPageIsReady(self,myself,sel,testplanName):
		''' Verify edit test plan page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,testplanName)
		self.verifyElement(myself,sel,"//input[@value='Save']")
		self.verifyElement(myself,sel,"//input[@value='Reset']")
		self.verifyElement(myself,sel,"//input[@value='Back']")

	def isEditTestPlanPageOpen(self,myself,sel,testplanName):
		''' Verify if the current page is test plan page in edit status. '''

		t1 = self.isPageTitle(myself,sel, testplanName)
		t2 = self.isText(myself,sel,"Edit")
		t3 = self.isElement(myself,sel,"//input[@value='Save']")

		if t1 and t2 and t3: return True
		else: return False

	def editTestPlan(self,myself,sel,testplanName,planname="<default>",product="<default>",prodversion="<default>",\
		typename="<default>",uploadPlanDocName="<default>",parentID="<default>",envGroup="<default>",referenceLink="<default>",\
		active="<default>"):
		''' Edit a test plan from an opened test plan. 
		    Note: The value of 'active' just involves: 'on','off'
		'''

		self.clickActionInTestPlan(myself,sel,"Edit Plan")
		self.verifyEditTestPlanPageIsReady(myself,sel,testplanName)

		#Fill the data for the edit test plan with provided data.
		self.fillDataForTestPlan(myself,sel,planname,product,prodversion,typename,uploadPlanDocName,parentID,envGroup,referenceLink)

		if active!="<default>":
			self.clickCheckBox(myself,sel,"id_is_active","",onoff=active)

		self.clickActionInEditPlan(myself,sel,"Save")

		#Verify if test plan is saved as expected
		if self.isEditTestPlanPageOpen(myself,sel,testplanName):
			self.verifyEditTestPlanPageIsReady(myself,sel,testplanName)
		else: 
			isPlanEnabled=True
			if active=="on": isPlanEnabled=True
			elif active=="off": isPlanEnabled=False

			if planname!="<default>": testplanName=planname

			self.verifyTestPlanPageIsReady(myself,sel,testplanName,isPlanEnabled,product,prodversion,\
				typename,parentID,envGroup,referenceLink)

	def clickActionInEditPlan(self,myself,sel,ActionName):
		''' Click Action in a edit test plan including button or link. '''

		if ActionName == "Save": self.clickBtnAndWait(myself,sel,"submit","Save")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")
		elif ActionName == "Back": self.clickBtnAndWait(myself,sel,"button","Back")

	def verifyErrWarningMsgInEditTestPlan(self,myself,sel,errType):
		''' Verify the error warning message when edit test plan. '''

		if errType == "Blank Plan Name":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")
		elif errType == "Upload Invalid Plan Document1": #This error will happen to some file unable to analyse like a binary file
			self.verifyElement(myself,sel,"css=ul.errorlist")
			self.verifyTargetText(myself,sel,"Unable to analyse the file or the file you upload is not Open Document.","css=ul.errorlist > li")
		elif errType == "Upload Invalid Plan Document2": #This error will happen to certain file like a '.sh' file
			self.verifyElement(myself,sel,"css=ul.errorlist")
			self.verifyTargetText(myself,sel,"The file you uploaded is not a correct, Html/Plain text/ODT file.","css=ul.errorlist > li")


	#---------------------------------------------------------------------
	#-------------------- (3) Test Plan 'Read' page ----------------------
	#---------------------------------------------------------------------

	def verifyTestPlanPageIsReady(self,myself,sel,testplanName,isPlanEnabled=True,product="<default>",\
		prodversion="<default>",typename="<default>",parentID="<default>",envGroup="<default>",\
		referenceLink="<default>",attachmentNameList="<default>",testcaseIdNames="<default>",testcaseNameList="<default>"):
		''' Verify test plan page is ready. 

		    About the two paras of 'testcaseIdNames' and 'testcaseNameList':
			If the Id and Name of the test cases needed to check is known, used the para 'testcaseIdNames',
			If only the Name of the test cases needed to check is known, used the para 'testcaseNameList'
		'''

		time.sleep(env.tl) #Wait some more time to make sure all the plan action buttons are loaded.
		self.verifyPageTitle(myself,sel, testplanName)
		self.verifyTargetText(myself,sel,testplanName,"display_title")

		if isPlanEnabled:
			#There will be NOT a line in the plan name when plan is enabled or active
			self.verifyTargetText(myself,sel,testplanName,"//h2[@id='display_title'][@class='']")
		else:
			#There will be a line in the plan name when plan is disabled or not-active
			self.verifyTargetText(myself,sel,testplanName,"//h2[@id='display_title'][@class='line-through']")

		if product!="<default>": self.verifyLink(myself,sel,product)
		if prodversion!="<default>": self.verifyTargetText(myself,sel,prodversion,"//div[@id='display_product_version']")
		if typename!="<default>": self.verifyTargetText(myself,sel,typename,"//div[@id='display_type']")

		if parentID!="<default>": 
			if parentID == "": parentID="None"
			self.verifyTargetText(myself,sel,parentID,"//div[@id='content']/div[3]/div[2]/div[4]/div[2]")

		if envGroup!="<default>" and envGroup!="---------":
			if envGroup!="":
				self.verifyLink(myself,sel,envGroup)
			else:
				self.verifyElementNotPresent(myself,sel,"//div[@id='content']/div[3]/div[2]/div/div[2]/span/a")

		if referenceLink!="<default>":
			if referenceLink == "": referenceLink="None"
			self.verifyTargetText(myself,sel,referenceLink,"//div[@id='content']/div[3]/div[2]/div[2]/div[2]")

		if testcaseIdNames!="<default>":
			if testcaseIdNames!="":
				for tId,tName in testcaseIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)
			else:
				#if testcaseIdNames=="", it indicates there should be no test case in the test plan
				self.verifyTargetText(myself,sel,"No test case was found in this plan.","//div[@id='testcases']/table/tbody/tr/td/center")

		if testcaseNameList!="<default>":
			if testcaseNameList!="":
				for i in range(len(testcaseNameList)):
					self.verifyLink(myself,sel,testcaseNameList[i])
			else:
				#if testcaseNameList=="", it indicates there should be no test case in the test plan
				self.verifyTargetText(myself,sel,"No test case was found in this plan.","//div[@id='testcases']/table/tbody/tr/td/center")

		if attachmentNameList!="<default>":
			self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Attachments")
			if attachmentNameList!="":
				for i in range(len(attachmentNameList)): 
					self.verifyLink(myself,sel,attachmentNameList[i])
			else:
				self.verifyTargetText(myself,sel,"No attachments","css=span.grey")

	def isTestPlanPageOpen(self,myself,sel,testplanName):
		''' Verify if the current page is test plan page. '''

		t1 = self.isPageTitle(myself,sel, testplanName)
		t2 = self.isTargetText(myself,sel,testplanName,"display_title")
		t3 = self.isElement(myself,sel,"//input[@type='button' and @value='Edit Plan ']")
		t4 = self.isElement(myself,sel,"//div[@id='testcases']/form/div/div[1]/ul/li[2]/span") #verify the 'Run' label exists under the label 'Cases'

		if t1 and t2 and t3 and t4: return True
		else: return False

	def verifyFirstLevelLabelOpenInPlan(self,myself,sel,labelName):
		''' Verify if the label 'labelName' is focused currently in test plan page. '''

		target="//body/div[2]/div[@id='plan_detail']/div/ul/li[@id='%s' and @class='tab tab_focus']/a"

		if labelName=="Document": self.verifyElement(myself,sel,target%("tab_document"))
		elif labelName=="Cases":  self.verifyElement(myself,sel,target%("tab_testcases"))
		elif labelName=="Reviewing Cases": self.verifyElement(myself,sel,target%("tab_reviewcases"))
		elif labelName=="Runs": self.verifyElement(myself,sel,target%("tab_testruns"))
		elif labelName=="Default Components": self.verifyElement(myself,sel,target%("tab_components"))
		elif labelName=="Attachments": self.verifyElement(myself,sel,target%("tab_attachment"))
		elif labelName=="Tags": self.verifyElement(myself,sel,target%("tab_tag"))
		elif labelName=="Log": self.verifyElement(myself,sel,target%("tab_tag"))
		elif labelName=="Tree View": self.verifyElement(myself,sel,target%("tab_treeview"))

	def clickFirstLevelLinkInPlan(self,myself,sel,linkId):
		''' Click the first level link in test plan. '''

		self.clickElement(myself,sel,"//body/div[2]/div[@id='plan_detail']/div/ul/li[@id='"+linkId+"']/a")
		time.sleep(env.t)

	def clickFirstLevelLinkByLabelNameInPlan(self,myself,sel,labelName):
		''' Click the first level link in test plan. '''

		if labelName=="Document": self.clickFirstLevelLinkInPlan(myself,sel,"tab_document")
		elif labelName=="Cases": self.clickFirstLevelLinkInPlan(myself,sel,"tab_testcases")
		elif labelName=="Reviewing Cases": self.clickFirstLevelLinkInPlan(myself,sel,"tab_reviewcases")
		elif labelName=="Runs": self.clickFirstLevelLinkInPlan(myself,sel,"tab_testruns")
		elif labelName=="Default Components": self.clickFirstLevelLinkInPlan(myself,sel,"tab_components")
		elif labelName=="Attachments": self.clickFirstLevelLinkInPlan(myself,sel,"tab_attachment")
		elif labelName=="Tags": self.clickFirstLevelLinkInPlan(myself,sel,"tab_tag")
		elif labelName=="Log": self.clickLink(myself,sel,labelName);time.sleep(env.ts)
		elif labelName=="Tree View": self.clickFirstLevelLinkInPlan(myself,sel,"tab_treeview")

	def clickActionInTestPlan(self,myself,sel,ActionName):
		''' Click Action in test plan in read status including button or link. '''

		if ActionName == "Edit Plan":
			self.clickElementAndWait(myself,sel,"//body[@id='body']/div[@id='content']/div[2]/span[@id='id_buttons']/input[@id='btn_edit']")
		elif ActionName == "Clone Plan":
			self.clickElementAndWait(myself,sel,"//body[@id='body']/div[@id='content']/div[2]/span[@id='id_buttons']/input[@id='btn_clone']")
		elif ActionName == "Enable Plan":
			self.clickElementAndWait(myself,sel,"//body[@id='body']/div[@id='content']/div[2]/span[@id='id_buttons']/input[@id='btn_enable']")
			time.sleep(env.ts)
		elif ActionName == "Disable Plan":
			self.clickElementAndWait(myself,sel,"//body[@id='body']/div[@id='content']/div[2]/span[@id='id_buttons']/input[@id='btn_disable']")
			time.sleep(env.ts)
		elif ActionName == "Export All Cases":
			self.clickElementAndWait(myself,sel,"//body[@id='body']/div[@id='content']/div[2]/span[@id='id_buttons']/input[@id='btn_export']")
		elif ActionName == "Print Plan":
			self.clickElementAndWait(myself,sel,"//body[@id='body']/div[@id='content']/div[2]/span[@id='id_buttons']/input[@id='btn_print']")

	def clickOtherActionInPlan(self,myself,sel,action):
		''' Click other action in test plan. '''

		if action == "Run_Clone": #click 'Runs'->'Clone'
			self.clickElementAndWait(myself,sel,"//input[@type='submit' and @value='Clone']")

		if action.find("Change parent node for plan ")!=-1: #click 'Tree View'->'Change parent node for plan <plan id>'
			self.clickElement(myself,sel,"//input[@type='button' and @value='"+action+"']")
		elif action.find("Add child node to current plan ")!=-1: #click 'Tree View'->'Add child node to current plan <plan id>'
			self.clickElement(myself,sel,"//input[@type='button' and @value='"+action+"']")
		elif action.find("Remove child node from current plan ")!=-1: #click 'Tree View'->'Remove child node from current plan <plan id>'
			self.clickElement(myself,sel,"//input[@type='button' and @value='"+action+"']")


	### ----------------------------------------- Begin of 'Document' Label Part ----------------------------------------- ###

	def verifyDocumentInfoInPlan(self,myself,sel,planDocStr):
		''' Verify if the Document info under 'Document' label is correct in test plan. '''
		
		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Document")

		self.verifyText(myself,sel,"Version:")
		self.verifyText(myself,sel,"Last Editor:")
		self.verifyText(myself,sel,env.user)
		self.verifyText(myself,sel,"Summary:")

		if planDocStr!="":
			self.verifyTargetText(myself,sel,planDocStr,"css=p")
		else:
			self.verifyElementNotPresent(myself,sel,"css=p")

	def addPlanDocDataInPlan(self,myself,sel,testplanName,planDocStr):
		''' Add plan document data into the test plan by way of uploading file. '''

		self.clickActionInTestPlan(myself,sel,"Edit Plan")
		self.verifyEditTestPlanPageIsReady(myself,sel,testplanName)

		planDocName = os.path.dirname(os.path.abspath(__file__)) + os.sep + "testplandoc.txt"
		fPlanDoc = file(planDocName, 'w') # open for 'w'riting
		fPlanDoc.write(planDocStr) # write text to file
		fPlanDoc.close() # close the file

		self.fillDataForTestPlan(myself,sel,uploadPlanDocName=planDocName)

		self.clickActionInEditPlan(myself,sel,"Save")
		if self.isEditTestPlanPageOpen(myself,sel,testplanName):
			self.verifyEditTestPlanPageIsReady(myself,sel,testplanName)

			self.clickActionInEditPlan(myself,sel,"Save")
			self.verifyTestPlanPageIsReady(myself,sel,testplanName)
			self.verifyDocumentInfoInPlan(myself,sel,planDocStr)

		os.remove(planDocName)


	### ----------------------------------------- Begin of 'Cases' Label Part ----------------------------------------- ###

	def verifyCaseAuthorInPlan(self,myself,sel,caseLineNum,authorName):
		''' Verify if the case author is correct in test plan. '''
		
		self.verifyElement(myself,sel,"//div[@id='testcases']/table/tbody/tr["+str(caseLineNum)+"]/td[5]/a[@href='/accounts/"+authorName+"/profile/']")

	def verifyCaseDefaultTesterInPlan(self,myself,sel,caseLineNum,defaultTesterName):
		''' Verify if the case default tester is correct in test plan. '''
		
		self.verifyElement(myself,sel,"//div[@id='testcases']/table/tbody/tr["+str(caseLineNum)+"]/td[6]/a[@href='/accounts/"+defaultTesterName+"/profile/']")

	def clickCaseActionInPlan(self,myself,sel,action):
		''' Click case action in test plan. Example of call: CCommonUtils().clickCaseActionInPlan(self,sel,"Print")'''

		self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div[1]/ul/li[1]/span")
		sel.mouse_move("//div[@id='testcases']/form/div/div[1]/ul/li[1]/span")# move onto the 'Case' label

		if action == "Write new case":
			actionTarget = "//div[@id='testcases']/form/div/div[1]/ul/li[1]/ul/li[1]/input" #click 'Case'->'Write new case'
			self.clickElementAndWait(myself,sel,actionTarget)
		elif action == "Add cases from other plans":
			actionTarget = "//div[@id='testcases']/form/div/div[1]/ul/li[1]/ul/li[3]/input" #click 'Case'->'Add cases from other plans'
			self.clickElementAndWait(myself,sel,actionTarget)
		elif action == "Print":
			actionTarget = "//div[@id='testcases']/form/div/div/ul/li/ul/li[5]/input" #click 'Case'->'Print'
			self.clickElementAndWait(myself,sel,actionTarget)
		elif action == "Clone":
			actionTarget = "//div[@id='testcases']/form/div/div/ul/li/ul/li[6]/input" #click 'Case'->'Clone'
			self.clickElementAndWait(myself,sel,actionTarget)
		elif action == "Remove":
			actionTarget = "//div[@id='testcases']/form/div/div[1]/ul/li[1]/ul/li[7]/input" #click 'Case'->'Remove'
			self.clickElement(myself,sel,actionTarget)
			myself.failUnless(re.search(r"^Are you sure you want to delete test case\(s\) from this test plan[\s\S]$", sel.get_confirmation()))
			time.sleep(env.ts)

		if action == "Run" or action == "Write new run":
			self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div[1]/ul/li[2]/span")
			sel.mouse_move("//div[@id='testcases']/form/div/div[1]/ul/li[2]/span")# move onto the 'Run' label

			actionTarget = "//input[@value='Write new run']" #click 'Write new run' link under 'Run' label
			self.clickElementAndWait(myself,sel,actionTarget)
		elif action == "Add cases to run":
			self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div[1]/ul/li[2]/span")
			sel.mouse_move("//div[@id='testcases']/form/div/div[1]/ul/li[2]/span")# move onto the 'Run' label

			actionTarget = "//input[@value='Add cases to run']" #click 'Write new run' link under 'Run' label
			self.clickElement(myself,sel,actionTarget)

		elif action == "Automated":
			actionTarget = "//div[@id='testcases']/form/div/div/ul/li[4]/input" #click 'Automated' link under 'Cases' label
			self.clickElement(myself,sel,actionTarget)
			time.sleep(env.ts)

		elif action == "Category":
			actionTarget = "//div[@id='testcases']/form/div/div/ul/li[8]/input" #click 'Category' link under 'Cases' label
			self.clickElement(myself,sel,actionTarget)
			time.sleep(env.ts)

		if action == "Open filter options": 
			if self.isElement(myself,sel,"//a[contains(text(),'Toggle filter options')]"):
				self.clickElement(myself,sel,"//a[contains(text(),'Toggle filter options')]")
			elif self.isElement(myself,sel,"//a[contains(text(),'Show filter options')]"):
				self.clickElement(myself,sel,"//a[contains(text(),'Show filter options')]")
		elif action == "Hide filter options": self.clickElement(myself,sel,"//a[contains(text(),'Hide filter options')]")

		if action == "Filter cases": self.clickElement(myself,sel,"//div[@id='testcases']/form/div[2]/div[5]/input")

	def selectTestCasesInPlan(self,myself,sel,testcaseIds):
		''' Select some test cases in the teset plan. The data type of the para testcaseIds is 'list' type.
		    Especially, if testcaseIds == 'all', it means to select all test cases, if testcaseIds == '', it means select no any test case.

		    An example of the value of testcaseIds: [testcaseId1,testcaseId2]
		    Example of call: CCommonUtils().selectTestCasesInPlan(self,sel,[env.testcaseId])
		'''

		if testcaseIds == "All":
			self.clickCheckBox(myself,sel,"","all",onoff="off")
			self.clickCheckBox(myself,sel,"","all",onoff="on")
		else:
			self.clickCheckBox(myself,sel,"","all",onoff="on")
			self.clickCheckBox(myself,sel,"","all",onoff="off")
			if testcaseIds != "":
				for i in range(len(testcaseIds)):
					self.clickCheckBox(myself,sel,"case",testcaseIds[i],onoff="on")

	def removeTestCasesInPlan(self,myself,sel,testcaseIdNames):
		''' Remove cases from current test plan. 'testcaseIdNames' is a 'dict' type para. '''

		self.selectTestCasesInPlan(myself,sel,testcaseIdNames.keys())
		self.clickCaseActionInPlan(myself,sel,"Remove")

		if testcaseIdNames!="<default>":
			
			if testcaseIdNames!="":
				for tId,tName in testcaseIdNames.items():
					self.verifyLinkNotPresent(myself,sel,tId)
					self.verifyLinkNotPresent(myself,sel,tName)

	def addTagForCaseInPlan(self,myself,sel,tagName,testcaseIdNames):
		''' Add tag for case in test plan. The data type of the para testcaseIdNames is 'dict' type.

		    An example of the value of testcaseIdNames: {testcaseId1:testcaseName1,testcaseId2:testcaseName2} 
		    Example of call: CCommonUtils().addTagForCaseInPlan(self,sel,tagName,{testcaseId1:testcaseName1,testcaseId2:testcaseName2})
		'''

		self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[3]/span")
		sel.mouse_over("//div[@id='testcases']/form/div/div/ul/li[3]/span")

		#Click 'Add Tag'
		self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[3]/ul/li/input")
		time.sleep(env.ts)

		self.inputText(myself,sel,"add_tag_plan", tagName)
		self.clickBtn(myself,sel,"submit","Submit")
		time.sleep(env.ts)

		self.verifyTargetText(myself,sel,"You have successfully operate tags in the following case:","css=div.dia_title")
		for tcId,tcName in testcaseIdNames.items():
			self.verifyText(myself,sel,tcId+"   "+tcName)

		self.clickElement(myself,sel,"//input[@value='Close']")
		time.sleep(env.ts)

		#To handle serveral tags by comma
		tagNameList=[]
		t=tagName.find(",")
		while t!=-1:
			tagNameList.append(tagName[:t])
			tagName=tagName[t+1:]
			t=tagName.find(",")
		tagNameList.append(tagName)

		for tagItem in tagNameList:
			self.verifyLink(myself,sel,tagItem)

	def removeTagForCaseInPlan(self,myself,sel,tagName,testcaseIdNames):
		''' Remove tags for cases in test plan. The data type of the para testcaseIdNames is 'dict' type.

		    An example of the value of testcaseIdNames: {testcaseId1:testcaseName1,testcaseId2:testcaseName2} 
		    Example of call: CCommonUtils().removeTagForCaseInPlan(self,sel,tagName,{testcaseId1:testcaseName1,testcaseId2:testcaseName2})
		'''

		self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[3]/span")
		sel.mouse_over("//div[@id='testcases']/form/div/div/ul/li[3]/span")

		#Click 'Remove Tag'
		self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[3]/ul/li[2]/input")
		time.sleep(env.ts)

		self.inputText(myself,sel,"add_tag_plan", tagName)
		self.clickBtn(myself,sel,"submit","Submit")
		time.sleep(env.ts)

		self.verifyTargetText(myself,sel,"You have successfully operate tags in the following case:","css=div.dia_title")
		for tcId,tcName in testcaseIdNames.items():
			self.verifyText(myself,sel,tcId+"   "+tcName)

		self.clickElement(myself,sel,"//input[@value='Close']")
		time.sleep(env.ts)

		#To handle serveral tags by comma
		tagNameList=[]
		t=tagName.find(",")
		while t!=-1:
			tagNameList.append(tagName[:t])
			tagName=tagName[t+1:]
			t=tagName.find(",")
		tagNameList.append(tagName)

		for tagItem in tagNameList:
			self.verifyLinkNotPresent(myself,sel,tagItem)

	def removeInvalidTagForCaseInPlan(self,myself,sel,tagName,testcaseIdNames):
		''' Remove non-existing tags for cases in test plan. The data type of the para testcaseIdNames is 'dict' type.

		    An example of the value of testcaseIdNames: {testcaseId1:testcaseName1,testcaseId2:testcaseName2} 
		    Example of call: CCommonUtils().removeTagForCaseInPlan(self,sel,tagName,{testcaseId1:testcaseName1,testcaseId2:testcaseName2})
		'''

		self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[3]/span")
		sel.mouse_over("//div[@id='testcases']/form/div/div/ul/li[3]/span")

		#Click 'Remove Tag'
		self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[3]/ul/li[2]/input")
		time.sleep(env.ts)

		self.inputText(myself,sel,"add_tag_plan", tagName)
		self.clickBtn(myself,sel,"submit","Submit")
		time.sleep(env.ts)

		#To handle serveral tags by comma
		tagNameList=[]
		t=tagName.find(",")
		while t!=-1:
			tagNameList.append(tagName[:t])
			tagName=tagName[t+1:]
			t=tagName.find(",")
		tagNameList.append(tagName)

		myself.assertEqual("Tag "+tagNameList[0]+" does not exist in current plan.", sel.get_alert())
		self.verifyLinkNotPresent(myself,sel,tagNameList[0])

	def setAutomatedForCaseInPlan(self,myself,sel,toAutomatedList):
		''' Change the Automated status of the test case in 'Cases' label. toAutomatedList's value included: "Automated", "Manual", "Autoproposed" '''

		self.clickCaseActionInPlan(myself,sel,"Automated")

		for i in range(len(toAutomatedList)):

			if toAutomatedList[i]=="Automated": self.clickCheckBox(myself,sel,"id_o_is_automated","",onoff="on")
			elif toAutomatedList[i]=="Manual": self.clickCheckBox(myself,sel,"id_o_is_manual","",onoff="on")
			elif toAutomatedList[i]=="Autoproposed": self.clickCheckBox(myself,sel,"id_o_is_automated_proposed","",onoff="on")

		self.clickBtn(myself,sel,"submit","Submit")
		
	def setStatusForCaseInPlan(self,myself,sel,toStatus):
		''' Change the Status of the test case in 'Cases' label by choosing one status from the drop dowm list of "Status" label.
		    The toStatus's value should just involve: "PROPOSED", "CONFIRMED", "DISABLED", "NEED_UPDATE" '''

		self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[7]/span")
		sel.mouse_over("//div[@id='testcases']/form/div/div/ul/li[7]/span")

		if toStatus=="PROPOSED": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[7]/ul/li/input")
		elif toStatus=="CONFIRMED": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[7]/ul/li[2]/input")
		elif toStatus=="DISABLED": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[7]/ul/li[3]/input")
		elif toStatus=="NEED_UPDATE": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[7]/ul/li[4]/input")
		time.sleep(env.ts)

		myself.failUnless(re.search(r"^Are you sure you want to change the status[\s\S]$", sel.get_confirmation()))
		time.sleep(env.ts)
		sel.refresh()
		time.sleep(env.ts)

	def setCategoryForCaseInPlan(self,myself,sel,selectedCase=True,product="<default>",category="<default>"):
		''' Change the Category for the selected test case in 'Cases' label. '''

		self.clickCaseActionInPlan(myself,sel,"Category")

		if selectedCase:
			#verify the dialog has been opened
			self.verifyTargetText(myself,sel,"Select Category","css=div.alert")

			#select product
			if product!="<default>": 
				if not self.isSelectedLabel(myself,sel,product,"id_product"):
					self.selectOptionInDropDownList(myself,sel,"id_product",product)

			#select category
			if category!="<default>":
				self.selectOptionInList(myself,sel,"id_o_category",category)

			self.clickBtn(myself,sel,"submit","Select")
		else:
			myself.assertEqual("No cases selected! Please select at least one case.", sel.get_alert())

	def setPriorityForCaseInPlan(self,myself,sel,toPriority):
		''' Change the Priority of the test case in 'Cases' label. toPriority's value should just involve: 'P1', 'P2', 'P3', 'P4', 'P5' '''

		self.verifyElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[9]/span")
		sel.mouse_over("//div[@id='testcases']/form/div/div/ul/li[9]/span")

		if toPriority=="P1": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[9]/ul/li[1]/input")
		elif toPriority=="P2": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[9]/ul/li[2]/input")
		elif toPriority=="P3": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[9]/ul/li[3]/input")
		elif toPriority=="P4": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[9]/ul/li[4]/input")
		elif toPriority=="P5": self.clickElement(myself,sel,"//div[@id='testcases']/form/div/div/ul/li[9]/ul/li[5]/input")
		time.sleep(env.ts)

		myself.failUnless(re.search(r"^Are you sure you want to change the priority[\s\S]$", sel.get_confirmation()))
		time.sleep(env.ts)
		sel.refresh()
		time.sleep(env.t)

	def changeCaseStatusInPlan(self,myself,sel,toStatus):
		''' Change the status of the test case in 'Cases' label by select Option In DropDown List of the test case. 
		    The toStatus's value included: "PROPOSED", "CONFIRMED", "DISABLED", "NEED_UPDATE" '''

		self.selectOptionInDropDownList(myself,sel,"//div[@id='testcases']/table/tbody/tr/td[8]/select",toStatus)
		sel.refresh()
		time.sleep(env.t)

	def verifyCommentForCaseInPlan(self,myself,sel,testcaseName,comString,comExists=True):
		''' Verify Comments For Case in test plan. '''

		self.clickElement(myself,sel,"//a[contains(text(),'"+testcaseName+"')]")
		time.sleep(env.ts)

		if comExists:
			#Verify if the comments exist
			self.verifyText(myself,sel,comString)

		else:
			#Verify the comments do not exist
			self.verifyTextNotPresent(myself,sel,comString)

	def addCommentForCaseInPlan(self,myself,sel,testcaseName,comString,needRemove=True):
		''' Add Comment For Case in test plan. '''

		self.clickElement(myself,sel,"//a[contains(text(),'"+testcaseName+"')]")
		time.sleep(env.ts)

		self.inputText(myself,sel,"//textarea[@id='id_comment']",comString)
		self.clickBtn(myself,sel,"submit","Add Comment")
		time.sleep(env.ts)

		#Verify if the comments have been added successfully
		self.verifyText(myself,sel,comString)

		if needRemove:
			#Delete the added comments
			self.clickElement(myself,sel,"//input[@value='Delete Comment']")
			myself.failUnless(re.search(r"^Are you sure to delete the comment[\s\S]$", sel.get_confirmation()))
			time.sleep(env.ts)

			#Verify the added comments have been deleted
			self.verifyTextNotPresent(myself,sel,comString)

	def removeCommentForCaseInPlan(self,myself,sel,testcaseName,comString):
		''' Remove Comment For Case in test plan. '''

		self.clickElement(myself,sel,"//a[contains(text(),'"+testcaseName+"')]")
		time.sleep(env.ts)

		#Verify if the comments exist
		self.verifyText(myself,sel,comString)

		#Delete the added comments
		self.clickElement(myself,sel,"//input[@value='Delete Comment']")
		myself.failUnless(re.search(r"^Are you sure to delete the comment[\s\S]$", sel.get_confirmation()))
		time.sleep(env.ts)

		#Verify if the comments have been deleted
		self.verifyTextNotPresent(myself,sel,comString)

	def editCaseSortNumInPlan(self,myself,sel,oldSortNum,newSortNum):
		''' Edit sort number of case run in test run. ''' 

		sel.answer_on_next_prompt(newSortNum)
		self.clickLink(myself,sel,oldSortNum)
		myself.assertEqual("Enter your new order number", sel.get_prompt())
		time.sleep(env.ts)

		if newSortNum == "": self.verifyLink(myself,sel,oldSortNum)
		else: self.verifyLink(myself,sel,newSortNum)

	def fillDataForFilterCaseInPlan(self,myself,sel,caseType="Test Cases",caseSummary="<default>",author="<default>",defaulttester="<default>",\
			priorityList="<default>",automated="<default>",autoproposed="<default>",category="<default>",\
			statusList="<default>",component="<default>",tag="<default>"):

		''' Fill the data for filter items in run with provided data. '''

		if caseType=="testcases" or caseType=="reviewcases": pass
		elif caseType=="Test Cases": caseType="testcases"
		elif caseType=="Reviewing Cases": caseType="reviewcases"

		#input summary of new test run
		if caseSummary!="<default>": self.inputText(myself,sel,"//div[@id='"+caseType+"']/form/div[2]/div/div/div[2]/input", caseSummary)

		#input author
		if author!="<default>": self.inputText(myself,sel,"//div[@id='"+caseType+"']/form/div[2]/div/div[2]/div[2]/input", author)

		#add Default Tester
		if defaulttester!="<default>": self.inputText(myself,sel,"//div[@id='"+caseType+"']/form/div[2]/div/div[3]/div[2]/input", defaulttester)

		#Value of this para 'priorityList' included: 1,2,3,4,5, an example to set this para: priorityList=[1,2,3,4,5]
		if priorityList != "<default>":
			for i in range(1,6):
				self.clickCheckBox(myself,sel,"","",fieldTarget="//div[@id='"+caseType+"']/form/div[2]/div/div[4]/div[2]/ul/li["+str(i)+"]/label/input",onoff="off")

			for i in range(len(priorityList)):
				self.clickCheckBox(myself,sel,"","",fieldTarget="//div[@id='"+caseType+"']/form/div[2]/div/div[4]/div[2]/ul/li["+str(priorityList[i])+"]/label/input",onoff="on")

		#select automated as one of below values: "----------", "Manual", "Auto", "Both"
		if automated!="<default>": 
			self.selectOptionInDropDownList(myself,sel,"//div[@id='"+caseType+"']/form/div[2]/div/div[5]/div[2]/select",automated)

		#The value of 'autoproposed' involves: 'on','off'
		if autoproposed!="<default>": 
			self.clickCheckBox(myself,sel,"","",fieldTarget="//div[@id='"+caseType+"']/form/div[2]/div/div[5]/div[2]/div/input",onoff=autoproposed)

		#select category
		if category!="<default>": 
			self.selectOptionInDropDownList(myself,sel,"//div[@id='"+caseType+"']/form/div[2]/div[2]/div/div[2]/select",category)

		#Value of this para 'statusList' included: 1,2,3,4, an example to set this para: statusList=[1,2,3,4]
		if statusList != "<default>":
			for i in range(1,5):
				self.clickCheckBox(myself,sel,"","",fieldTarget="//div[@id='"+caseType+"']/form/div[2]/div[2]/div[2]/div[2]/ul/li["+str(i)+"]/label/input",onoff="off")

			for i in range(len(statusList)):
				self.clickCheckBox(myself,sel,"","",fieldTarget="//div[@id='"+caseType+"']/form/div[2]/div[2]/div[2]/div[2]/ul/li["+str(statusList[i])+"]/label/input",onoff="on")

		#select component
		if component!="<default>": 
			self.selectOptionInDropDownList(myself,sel,"//div[@id='"+caseType+"']/form/div[2]/div[2]/div[3]/div[2]/select",component)

		#add tag
		if tag!="<default>": self.inputText(myself,sel,"//div[@id='"+caseType+"']/form/div[2]/div[2]/div[4]/div[2]/input", tag)

	def filterCaseInPlan(self,myself,sel,caseType="Test Cases",caseSummary="<default>",author="<default>",defaulttester="<default>",\
		priorityList="<default>",automated="<default>",autoproposed="<default>",category="<default>",\
		statusList="<default>",component="<default>",tag="<default>",testcaseResultIdNames="<default>",\
		testcaseResultNoIdNames="<default>"):
		'''Filter test cases with right options in test plan.  'testcaseResultIdNames' is a 'dict' type para. '''

		if caseType=="testcases" or caseType=="reviewcases": pass
		elif caseType=="Test Cases": caseType="testcases"
		elif caseType=="Reviewing Cases": caseType="reviewcases"

		self.clickCaseActionInPlan(myself,sel,"Open filter options")

		self.fillDataForFilterCaseInPlan(myself,sel,caseType,caseSummary,author,defaulttester,priorityList,\
				automated,autoproposed,category,statusList,component,tag)

		#Click the "Filter cases" button
		self.clickCaseActionInPlan(myself,sel,"Filter cases")

		if testcaseResultIdNames!="<default>":
			if testcaseResultIdNames!="":
				for tId,tName in testcaseResultIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)
			else:
				#if testcaseResultIdNames=="", it indicates there should be no test case run searched out
				self.verifyTargetText(myself,sel,"No test case was found in this plan.","//div[@id='"+caseType+"']/table/tbody/tr/td/center")

		if testcaseResultNoIdNames!="<default>":
			if testcaseResultNoIdNames!="":
				for tId,tName in testcaseResultNoIdNames.items():
					self.verifyLinkNotPresent(myself,sel,tId)
					self.verifyLinkNotPresent(myself,sel,tName)


	### ----------------------------------------- Begin of 'Reviewing Cases' Label Part ----------------------------------------- ###

	def changeReviewCaseStatusInPlan(self,myself,sel,toStatus):
		''' Change the status of the test case in 'Reviewing Cases' label. toStatus's value included: "PROPOSED", "CONFIRMED", "DISABLED", "NEED_UPDATE" '''

		self.selectOptionInDropDownList(myself,sel,"//div[@id='reviewcases']/table/tbody/tr/td[8]/select",toStatus)
		sel.refresh()
		time.sleep(env.t)

	def setStatusForReviewingCaseInPlan(self,myself,sel,toStatus):
		''' Change the Status of the Reviewing test case in 'Reviewing Cases' label by choosing one status from the drop dowm list of "Status" label.
		    The toStatus's value should just involve: "PROPOSED", "CONFIRMED", "DISABLED", "NEED_UPDATE" '''

		self.verifyElement(myself,sel,"//div[@id='reviewcases']/form/div/div/ul/li[6]/span")
		sel.mouse_over("//div[@id='reviewcases']/form/div/div/ul/li[6]/span")

		if toStatus=="PROPOSED": self.clickElement(myself,sel,"//div[@id='reviewcases']/form/div/div/ul/li[6]/ul/li/input")
		elif toStatus=="CONFIRMED": self.clickElement(myself,sel,"//div[@id='reviewcases']/form/div/div/ul/li[6]/ul/li[2]/input")
		elif toStatus=="DISABLED": self.clickElement(myself,sel,"//div[@id='reviewcases']/form/div/div/ul/li[6]/ul/li[3]/input")
		elif toStatus=="NEED_UPDATE": self.clickElement(myself,sel,"//div[@id='reviewcases']/form/div/div/ul/li[6]/ul/li[4]/input")
		time.sleep(env.ts)

		myself.failUnless(re.search(r"^Are you sure you want to change the status[\s\S]$", sel.get_confirmation()))
		time.sleep(env.ts)
		sel.refresh()
		time.sleep(env.ts)


	### ----------------------------------------- Begin of 'Runs' Label Part ----------------------------------------- ###

	def verifyRunProgBarInPlan(self,myself,sel,failpercent="<default>",successpercent="<default>"):
		''' Verify if the first Run Prog Bar under 'Runs' label is correct in test plan. '''
		
		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Runs")

		if failpercent!="<default>":
			self.verifyElement(myself,sel,"css=div.progress-failed")
			self.verifyTargetText(myself,sel,failpercent,"//table[@id='testruns_table']/tbody/tr/td[10]/div/div")

		if successpercent!="<default>":
			self.verifyElement(myself,sel,"css=div.progress-inner")
			self.verifyTargetText(myself,sel,successpercent,"//table[@id='testruns_table']/tbody/tr/td[11]/div/div")

	def selectTestRunsInPlan(self,myself,sel,testrunIds):
		''' Select part of test runs in the plan. The data type of the para testrunIds is 'list' type.

		    An example of the value of testrunIds: [testrunId1,testrunId2]
		    Example of call: CCommonUtils().selectTestRunsInPlan(self,sel,[env.testrunId])
		'''

		self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="on")
		self.clickCheckBox(myself,sel,"id_check_all_runs","",onoff="off") #Uncheck all runs
		if testrunIds != "":
			for i in range(len(testrunIds)):
				self.clickCheckBox(myself,sel,"run",testrunIds[i],onoff="on")


	### ----------------------------------------- Begin of 'Default Components' Label Part ----------------------------------------- ###

	def addComponentInPlan(self,myself,sel,componentNameList,removeCompNameList="<default>"):
		''' Add Component In Plan. ''' 

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Default Components")

		self.clickElement(myself,sel,"//input[@value='Update components']")

		for i in range(len(componentNameList)):
			self.selectOptionInList(myself,sel,"//p[2]/select[@id='id_component']",componentNameList[i])

		if removeCompNameList!="<default>":
			for i in range(len(removeCompNameList)):
				self.unselectOptionInList(myself,sel,"//p[2]/select[@id='id_component']",removeCompNameList[i])

		self.clickBtn(myself,sel,"submit","Update")

		for i in range(len(componentNameList)):
			self.verifyText(myself,sel,componentNameList[i])

		if removeCompNameList!="<default>":
			for i in range(len(removeCompNameList)):
				self.verifyTextNotPresent(myself,sel,removeCompNameList[i])

	def removeComponentInPlan(self,myself,sel,componentIdNames):
		''' Remove Component In Plan. ''' 

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Default Components")

		if componentIdNames=="All":
			self.clickCheckBox(myself,sel,"id_checkbox_all_component","",onoff="off")
			self.clickCheckBox(myself,sel,"id_checkbox_all_component","",onoff="on")
			
			self.clickElement(myself,sel,"//input[@name='a' and @value='Remove']")
			self.verifyTargetText(myself,sel,"No component defined.","//form[@id='id_form_plan_components']/table/tbody/tr/td/span")
		else:
			self.clickCheckBox(myself,sel,"id_checkbox_all_component","",onoff="on")
			self.clickCheckBox(myself,sel,"id_checkbox_all_component","",onoff="off")
			if componentIdNames != "":
				for cId in componentIdNames.keys():
					self.clickCheckBox(myself,sel,"component",cId,onoff="on")

				self.clickElement(myself,sel,"//input[@name='a' and @value='Remove']")

				for cName in componentIdNames.values():
					self.verifyTextNotPresent(myself,sel,cName)


	### ----------------------------------------- Begin of 'Attachments' Label Part ----------------------------------------- ###

	def addAttachmentInPlan(self,myself,sel,attachmentPathList):
		''' Add attachment for test plan. '''

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Attachments")

		self.clickLink(myself,sel,"add")
		self.verifyTargetText(myself,sel,"Upload New Attachment","css=span.tit")

		for i in range(len(attachmentPathList)):
			self.inputText(myself,sel,"upload_file", attachmentPathList[i])
			self.clickBtn(myself,sel,"submit","Upload")

			self.verifyLink(myself,sel,os.path.basename(attachmentPathList[i]))

	def removeAttachmentInPlan(self,myself,sel,attachmentNameList):
		''' Remove attachments for test plan. '''

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Attachments")

		for i in range(len(attachmentNameList)):

			self.verifyLink(myself,sel,attachmentNameList[i])

			for r in range(1,1000):
				if self.isTargetText(myself,sel,attachmentNameList[i],"//tr["+str(r)+"]/td[1]/a"):

					self.clickElement(myself,sel,"//tr["+str(r)+"]/td[5]/a[2]") #click "Delete" link
					myself.failUnless(re.search(r"^Arey you sure to delete the attachment[\s\S]$", sel.get_confirmation()))
					time.sleep(env.ts)

					self.verifyLinkNotPresent(myself,sel,attachmentNameList[i])
					break


	### ----------------------------------------- Begin of 'Tags' Label Part ----------------------------------------- ###

	def verifyTagInfoInPlan(self,myself,sel,tagNum="<default>",planNum="<default>",caseNum="<default>",runNum="<default>",tagName="<default>"):
		''' Verify if the tag info involving tag/plan/case/run number under 'Tags' label is correct in test plan. '''
		
		if str(tagNum)!="<default>":
			sel.refresh()
			time.sleep(env.t)
			self.verifyTargetText(myself,sel,"Tags ("+str(tagNum)+")","//body/div[2]/div[@id='plan_detail']/div/ul/li[@id='tab_tag']/a")
		if str(planNum)!="<default>":
			self.verifyTargetText(myself,sel,str(planNum),"//a[contains(@href, '/plans/?action=search&tag__name__in="+tagName+"')]")
		if str(caseNum)!="<default>":
			self.verifyTargetText(myself,sel,str(caseNum),"//a[contains(@href, '/cases/?a=search&tag__name__in="+tagName+"')]")
		if str(runNum)!="<default>":
			self.verifyTargetText(myself,sel,str(runNum),"//a[contains(@href, '/runs/?action=search&tag__name__in="+tagName+"')]")

	def addTagInPlan(self,myself,sel,tagName,needRemove=True):
		''' Add tag for test plan in test plan. '''

		#Click 'Tags'
		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Tags")

		self.inputText(myself,sel,"id_tags", tagName)
		self.clickLink(myself,sel,"Add")

		#To handle serveral tags by comma
		tagNameList=[]
		t=tagName.find(",")
		while t!=-1:
			tagNameList.append(tagName[:t])
			tagName=tagName[t+1:]
			t=tagName.find(",")
		tagNameList.append(tagName)

		for tagItem in tagNameList:
			self.verifyText(myself,sel,tagItem)

		if needRemove:	self.removeTagInPlan(myself,sel,tagNameList)

	def editTagInPlan(self,myself,sel,tagNameOld,tagNameNew):
		''' Edit a tag in test plan. '''

		sel.answer_on_next_prompt(tagNameNew)
		self.clickElement(myself,sel,"//a[@onclick=\"editTag(this.up(5), '%s')\"]"%tagNameOld)
		myself.assertEqual("Please type your new tag", sel.get_prompt())
		time.sleep(env.ts)

		self.verifyText(myself,sel,tagNameNew)

	def removeTagInPlan(self,myself,sel,tagNameList):
		''' Remove tags from test plan. '''

		#Click 'Tags'
		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Tags")

		for tagItem in tagNameList:
		        self.clickElement(myself,sel,"//a[@onclick=\"removeTag(this.up(5), '%s')\"]"%tagItem)
			self.verifyTextNotPresent(myself,sel,tagItem)


	### ----------------------------------------- Begin of 'Tree View' Label Part ----------------------------------------- ###

	def changeParentNode(self,myself,sel,curtestplanId,changetestplanId,changetestplanName,submitOrCancel="Submit"):
		''' ChangeParent Node for current test plan. '''

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Tree View")

		if changetestplanId!="" and changetestplanName!="":

			sel.answer_on_next_prompt(changetestplanId)
			self.clickOtherActionInPlan(myself,sel,"Change parent node for plan "+curtestplanId)
			myself.assertEqual("Enter new parent plan ID", sel.get_prompt())
			time.sleep(env.ts)

			self.verifyCheckBox(myself,sel,"on","id_preview_plan_"+changetestplanId,changetestplanId)
			self.verifyText(myself,sel,"["+changetestplanId+"] "+changetestplanName)

			if submitOrCancel=="Submit":
				self.clickBtn(myself,sel,"submit",submitOrCancel)
				time.sleep(env.ts)

				self.verifyLink(myself,sel,changetestplanId)
				self.verifyLink(myself,sel,changetestplanName)

			elif submitOrCancel=="Cancel":
				self.clickBtn(myself,sel,"button",submitOrCancel)
				time.sleep(env.ts)

				self.verifyLinkNotPresent(myself,sel,changetestplanId)
				self.verifyLinkNotPresent(myself,sel,changetestplanName)

	def addChildNode(self,myself,sel,curtestplanId,addtestplanIdNames,submitOrCancel="Submit"):
		''' Add Child Node for current test plan.

		    The para 'addtestplanIdNames' is 'dict' type, it's value is like: {testplanId1:testplanName1,testplanId2:testplanName2}
		'''

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Tree View")

		if addtestplanIdNames!="":
			addtestplanIdStr=""
			for tpId,tpName in addtestplanIdNames.items():
				addtestplanIdStr+=tpId+","

			sel.answer_on_next_prompt(addtestplanIdStr[:-1])
			self.clickOtherActionInPlan(myself,sel,"Add child node to current plan "+curtestplanId)
			myself.assertEqual("Enter a comma separated list of plan IDs", sel.get_prompt())
			time.sleep(env.ts)

			for tpId,tpName in addtestplanIdNames.items():
				self.verifyCheckBox(myself,sel,"on","id_preview_plan_"+tpId,tpId)
				self.verifyText(myself,sel,"["+tpId+"] "+tpName)

			if submitOrCancel=="Submit":
				self.clickBtn(myself,sel,"submit",submitOrCancel)
				time.sleep(env.ts)

				myself.assertEqual("The tree has been reloaded.", sel.get_alert())
				time.sleep(env.ts)

				for tpId,tpName in addtestplanIdNames.items():
					self.verifyLink(myself,sel,tpId)
					self.verifyLink(myself,sel,tpName)

				sel.refresh()
				time.sleep(env.t)

			elif submitOrCancel=="Cancel":
				self.clickBtn(myself,sel,"button",submitOrCancel)
				time.sleep(env.ts)

				for tpId,tpName in removetestplanIdNames.items():
					self.verifyLinkNotPresent(myself,sel,tpId)
					self.verifyLinkNotPresent(myself,sel,tpName)

	def removeChildNode(self,myself,sel,curtestplanId,removetestplanIdNames,submitOrCancel="Submit"):
		''' Remove Child Node for current test plan.

		    The para 'removetestplanIdNames' is 'dict' type, it's value is like: {testplanId1:testplanName1,testplanId2:testplanName2}
		'''

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Tree View")

		if removetestplanIdNames!="":
			removetestplanIdStr=""
			for tpId,tpName in removetestplanIdNames.items():
				removetestplanIdStr+=tpId+","

			sel.answer_on_next_prompt(removetestplanIdStr[:-1])
			self.clickOtherActionInPlan(myself,sel,"Remove child node from current plan "+curtestplanId)
			myself.assertEqual("Enter a comma separated list of plan IDs to be removed", sel.get_prompt())
			time.sleep(env.ts)

			for tpId,tpName in removetestplanIdNames.items():
				self.verifyCheckBox(myself,sel,"on","id_preview_plan_"+tpId,tpId)
				self.verifyText(myself,sel,"["+tpId+"] "+tpName)

			if submitOrCancel=="Submit":
				self.clickBtn(myself,sel,"submit",submitOrCancel)
				time.sleep(env.ts)

				myself.assertEqual("The tree has been reloaded.", sel.get_alert())
				time.sleep(env.ts)

				for tpId,tpName in removetestplanIdNames.items():
					self.verifyLinkNotPresent(myself,sel,tpId)
					self.verifyLinkNotPresent(myself,sel,tpName)

				sel.refresh()
				time.sleep(env.t)

			elif submitOrCancel=="Cancel":
				self.clickBtn(myself,sel,"button",submitOrCancel)
				time.sleep(env.ts)

				for tpId,tpName in addtestplanIdNames.items():
					self.verifyLink(myself,sel,tpId)
					self.verifyLink(myself,sel,tpName)

	def removeInvalidChildNode(self,myself,sel,curtestplanId,invalidtestplanId):
		''' Try to remove a invalid Child Node for current test plan. '''

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Tree View")

		sel.answer_on_next_prompt(invalidtestplanId)
		self.clickOtherActionInPlan(myself,sel,"Remove child node from current plan "+curtestplanId)
		myself.assertEqual("Enter a comma separated list of plan IDs to be removed", sel.get_prompt())
		time.sleep(env.ts)

		self.verifyTargetText(myself,sel,"The plan you specific does not exist in database. This operation will overwrite existing data","css=#dialog > form")

	#------------------------------------------------------------------------
	#--------------- (4) Test Plan 'Add Cases to Runs' page -----------------
	#------------------------------------------------------------------------

	def verifyAddCaseToRunFromPlanPageIsReady(self,myself,sel,testplanName,testrunIdNames,testcaseIdNames):
		''' Verify 'Add Cases to Runs' page is ready.  The data type of the para testrunIdNames is 'dict' type. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"Choose test run to assign case")
		self.verifyLink(myself,sel,"Plan:"+testplanName)

		for tId,tName in testrunIdNames.items():
			self.verifyLink(myself,sel,tId)
			self.verifyText(myself,sel,tName)

		for tId,tName in testcaseIdNames.items():
			self.verifyLink(myself,sel,tId)
			self.verifyLink(myself,sel,tName)

	def selectTestRunsInAddCaseToRunFromPlanPage(self,myself,sel,testrunIds):
		''' Select part of test runs in the 'Add Cases to Runs' page. The data type of the para testrunIds is 'list' type. '''

		for i in range(len(testrunIds)):
			self.clickCheckBox(myself,sel,"run",testrunIds[i],onoff="on")

	def clickActionInAddCaseToRunFromPlanPage(self,myself,sel,ActionName):
		''' Click Action in 'Add Cases to Runs' Page including button or link. '''

		if ActionName == "Update":
			self.clickBtn(myself,sel,"button","Update")
			myself.failUnless(re.search(r"^Are you sure to add cases to the run[\s\S]$", sel.get_confirmation()))
			time.sleep(env.ts)
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")


	#----------------------------------------------------------------------
	#-------------------- (5) Test Plan 'Other' page ----------------------
	#----------------------------------------------------------------------

	def verifyExportPlanWarningPageIsReady(self,myself,sel):
		''' Verify the warning page is ready and shown correctly when click Export button in search plan result without a test plan selected. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel, "INFO - At least one target is required.")
		self.verifyText(myself,sel,"At least one target is required.")




