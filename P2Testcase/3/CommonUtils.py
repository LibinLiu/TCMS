from selenium import selenium
import unittest, time, re, os

from env import *
import CommonPages1_Home, CommonPages2_Plan, CommonPages3_Case, CommonPages4_Run, CommonPages5_Search, CommonPages6_Other

class CCommonUtils(CommonPages1_Home.CCommonPages,CommonPages2_Plan.CCommonPages,CommonPages3_Case.CCommonPages,\
		CommonPages4_Run.CCommonPages, CommonPages5_Search.CCommonPages,CommonPages6_Other.CCommonPages):


	# ========================================================================================================
	# 	Home page related functions
	# ========================================================================================================


	def openHomePage(self,myself,sel):
		''' Open home page. '''

		if self.isHomePageOpen(myself,sel): return

		sel.open(env.openurl)
		self.verifyHomePageIsReady(myself,sel)

	def openBookmarksPage(self,myself,sel):
		''' Open Bookmarks page from home page. '''

		self.openHomePage(myself,sel)
		self.clickActionLinkInHomePage(myself,sel,"Bookmarks")
		self.verifyBookmarksPageIsReady(myself,sel)

	def openBasicinfoPage(self,myself,sel):
		''' Open Basic information page from home page. '''

		self.openHomePage(myself,sel)
		self.clickActionLinkInHomePage(myself,sel,"Basic Information")
		self.verifyBasicInformationPageIsReady(myself,sel)

	def editBasicinfo(self,myself,sel,firstName="<default>",lastName="<default>",phoneNumber="<default>",\
		IMType="<default>",IMValue="<default>",webURL="<default>",address="<default>",notes="<default>"):
		''' Edit the Basic information form with provided data. '''

		self.openBasicinfoPage(myself,sel)

		#Fill the data for the edit Basic information form with provided data.
		self.fillDataForBasicinfoPage(myself,sel,firstName,lastName,phoneNumber,IMType,IMValue,webURL,address,notes)

		self.clickActionInBasicinfo(myself,sel,"Save Change")

		self.verifyBasicInformationPageIsReady(myself,sel,firstName,lastName,phoneNumber,IMType,IMValue,webURL,address,notes,True)


	# ========================================================================================================
	# 	Test Plan related functions
	# ========================================================================================================


	def createTestPlan(self,myself,sel,testplanName):
		''' Create a test plan. Example of call: CCommonUtils().createTestPlan(self,sel,"test") '''

		testplanId = ""

		self.clickMenu(myself,sel,"PLANNING","New Plan")

		self.fillDataForTestPlan(myself,sel,planname=testplanName,product=env.product1,prodversion=env.prodversion11,typename=env.plantype11)
		self.clickActionInCreateTestPlan(myself,sel,"Create test plan")
		self.verifyTestPlanPageIsReady(myself,sel,testplanName)

		testplanId = self.getTestPlanId(myself,sel,testplanName)
		return testplanId

	def openTestPlan(self,myself,sel,testplanName):
		''' To open a test plan. Example of call: CCommonUtils().openTestPlan(self,sel,"test")
			
		    Firstly, to open a test plan directly by url, if failed, try to  open a test plan 
		    from home page, if not exists, try to search it and then open it. 

		    Note: the test plan name is supposed to be unique.
		'''

		if self.isTestPlanPageOpen(myself,sel,testplanName): return

		testplanId = ""
		if testplanName==env.testplanName: testplanId = env.testplanId
		elif testplanName==env.testplanName2: testplanId = env.testplanId2
		elif testplanName==env.testplanName3: testplanId = env.testplanId3
		elif testplanName==env.testplanName4: testplanId = env.testplanId4

		if not testplanId == "":
			sel.open("/plan/"+testplanId+"/")
			time.sleep(env.tl)

			if not self.isTestPlanPageOpen(myself,sel,testplanName):
				self.openHomePage(myself,sel)
				if not self.isLink(myself,sel,testplanName):
					self.searchTestPlan(myself,sel,planName=testplanName)
				self.clickLinkAndWait(myself,sel,testplanName)
				self.verifyTestPlanPageIsReady(myself,sel,testplanName)

		else:
			self.openHomePage(myself,sel)
			if not self.isLink(myself,sel,testplanName):
				self.searchTestPlan(myself,sel,planName=testplanName)
			self.clickLinkAndWait(myself,sel,testplanName)
			self.verifyTestPlanPageIsReady(myself,sel,testplanName)

	def getTestPlanId(self,myself,sel,testplanName):
		''' Get a test plan id by printing a test plan. Note: the test case name is supposed to be unique. '''

		testplanId = ""

		self.openTestPlan(myself,sel,testplanName)

		#Method 1: Get plan id by navigation text in the top of the test plan page
		tstr = sel.get_text("css=div.sprites.crumble")
		t1 = tstr.find('Planning >> ')
		t2 = tstr.find(': ')
		testplanId = tstr[t1+12:t2]

		if testplanId == "":
			#Method 2: Get plan id by print plan page
			self.clickBtnAndWait(myself,sel,"button","Print Plan ")

			#verify Print Test Plan Page Is Ready
			self.verifyTargetText(myself,sel,"Test Plan Document","plan_document")

			tstr = sel.get_text("css=h1")
			t1 = tstr.find('[')
			t2 = tstr.find(']')
			testplanId = tstr[t1+1:t2]

			#return to home page
			sel.open(env.openurl)
			self.verifyHomePageIsReady(myself,sel)

		return testplanId

	def hasTestPlan(self,myself,sel,testplanName):
		''' Firstly check if the test plan exists in home page, if not, try to search it in Advanced Search, if not yet, return False, or else return True. 
			 Note: the test plan name is supposed to be unique.
		'''

		self.openHomePage(myself,sel)

		if self.isLink(myself,sel,testplanName): return True
		else: 
			testplanId = ""
			if testplanName==env.testplanName: testplanId = env.testplanId
			elif testplanName==env.testplanName2: testplanId = env.testplanId2
			elif testplanName==env.testplanName3: testplanId = env.testplanId3
			elif testplanName==env.testplanName4: testplanId = env.testplanId4

			if not testplanId == "": self.searchPlanById(myself,sel,testplanId)
			else: self.searchPlanByName(myself,sel,testplanName)
				
			if self.isLink(myself,sel,testplanName): return True
			else: return False

	def addCasesToRunInPlan(self,myself,sel,testplanName,testrunIdNames,testcaseIdNames):
		''' Add cases to runs, note that the cases 'testcaseIdNames' and runs 'testrunIdNames' should be in the same test plan 'testplanName'. '''

		self.openTestPlan(myself,sel,testplanName)

		if testrunIdNames!="":
			self.selectTestCasesInPlan(myself,sel,testcaseIdNames.keys())
			self.clickCaseActionInPlan(myself,sel,"Add cases to run")
			self.verifyAddCaseToRunFromPlanPageIsReady(myself,sel,testplanName,testrunIdNames,testcaseIdNames)

			self.selectTestRunsInAddCaseToRunFromPlanPage(myself,sel,testrunIdNames.keys())
			self.clickActionInAddCaseToRunFromPlanPage(myself,sel,"Update")
			self.verifyTestPlanPageIsReady(myself,sel,testplanName)

		#Verify the cases have been added into the test runs
		for tName in testrunIdNames.values():
			self.openTestRun(myself,sel,tName)
			self.verifyTestRunPageIsReady(myself,sel,tName,testcaseIds=testcaseIdNames.keys())


	# ========================================================================================================
	# 	Test Case related functions
	# ========================================================================================================


	def createTestCaseFromPlan(self,myself,sel,testplanName,testcaseName):
		''' Create a test case from a test plan. Note: the test case name is supposed to be unique. '''

		testcaseId = ""

		self.openTestPlan(myself,sel,testplanName)

		self.clickCaseActionInPlan(myself,sel,"Write new case")
		self.verifyCreateTestCasePageIsReady(myself,sel)

		#Fill the data for a new test case form with provided data.
		self.fillDataForTestCase(myself,sel,summary=testcaseName,product=env.product1,component=[env.component11],category=env.category11,manual="off",\
			auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")

		#save the test case
		self.clickActionInCreateCase(myself,sel,"Save")
		self.verifyTestCasePageIsReady(myself,sel,testcaseName)
		testcaseId = self.getTestCaseId(myself,sel,testcaseName)

		#open the test plan to change the status of just created test case from reviewing to confirmed
		self.openTestPlan(myself,sel,testplanName)
		self.clickFirstLevelLinkInPlan(myself,sel,"tab_reviewcases")
		self.changeReviewCaseStatusInPlan(myself,sel,"CONFIRMED")
		self.clickFirstLevelLinkInPlan(myself,sel,"tab_testcases")
		self.verifyLink(myself,sel,testcaseId)

		return testcaseId

	def createCustomizedTestCaseFromPlan(self,myself,sel,testplanName,summary="<default>",product="<default>",component="<default>",\
		category="<default>",manual="<default>",auto="<default>",autoproposal="<default>",requirement="<default>",script="<default>",\
		alias="<default>",defaulttester="<default>",estdays="<default>",esthours="<default>",estmins="<default>",estsecs="<default>",\
		priority="<default>",arguments="<default>",notes="<default>"):
		''' Create a test case from a test plan with provided data. Note: the test case name is supposed to be unique. '''

		testcaseId = ""

		self.openTestPlan(myself,sel,testplanName)

		self.clickCaseActionInPlan(myself,sel,"Write new case")
		self.verifyCreateTestCasePageIsReady(myself,sel)

		#Fill the data for a new test case form with provided data.
		self.fillDataForTestCase(myself,sel,summary,product,component,category,manual,auto,autoproposal,requirement,script,\
		alias,defaulttester,estdays,esthours,estmins,estsecs,priority,arguments,notes)

		#save the test case
		self.clickActionInCreateCase(myself,sel,"Save")
		self.verifyTestCasePageIsReady(myself,sel,summary)
		testcaseId = self.getTestCaseId(myself,sel,summary)

		#open the test plan to change the status of just created test case from reviewing to confirmed
		self.openTestPlan(myself,sel,testplanName)
		self.clickFirstLevelLinkInPlan(myself,sel,"tab_reviewcases")
		self.changeReviewCaseStatusInPlan(myself,sel,"CONFIRMED")
		self.clickFirstLevelLinkInPlan(myself,sel,"tab_testcases")
		self.verifyLink(myself,sel,testcaseId)

		return testcaseId

	def openTestCaseFromPlan(self,myself,sel,testplanName,testcaseId,testcaseName):
		''' Open a test case from test plan. '''

		self.openTestPlan(myself,sel,testplanName)

		self.clickLinkAndWait(myself,sel,testcaseId)

		self.verifyTestCasePageIsReady(myself,sel,testcaseName)

	def openReviewingTestCaseFromPlan(self,myself,sel,testplanName,testcaseId,testcaseName):
		''' Open a reviewing test case from test plan. '''

		self.openTestPlan(myself,sel,testplanName)

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Reviewing Cases")

		self.clickLinkAndWait(myself,sel,testcaseId)

		self.verifyTestCasePageIsReady(myself,sel,testcaseName)

	def getTestCaseId(self,myself,sel,testcaseName):
		''' Get a test case id by searching the test case name. Note: the test case name is supposed to be unique. '''

		testcaseId = ""

		if not self.isTestCasePageOpen(myself,sel,testcaseName):
			self.openSearchCasePage(myself,sel)
			self.inputText(myself,sel,"id_summary",testcaseName)
			self.clickBtn(myself,sel,"submit","search")

			for i in range(1000):
			    try:
			       if self.isLink(myself,sel,testcaseName):
					self.clickLink(myself,sel,testcaseName)
					time.sleep(env.ts)

					break
			    except: pass
			    time.sleep(1)

		#Get the case id number
		title = sel.get_title()
		t1=title.find("Test case - ")
		t2=title.find(": ")
		testcaseId = title[t1+12:t2]

		return testcaseId

	def getTestCaseCreatedDate(self,myself,sel,testcaseName):
		''' Get the test case's Created Date. '''

		CreatedDate = ""

		if not self.isTestCasePageOpen(myself,sel,testcaseName):
			self.openSearchCasePage(myself,sel)
			self.inputText(myself,sel,"id_summary",testcaseName)
			self.clickBtn(myself,sel,"submit","search")

			for i in range(1000):
			    try:
			       if self.isLink(myself,sel,testcaseName):
					self.clickLink(myself,sel,testcaseName)
					time.sleep(env.ts)

					break
			    except: pass
			    time.sleep(1)

		#Get the case created Date
		CreatedDate = sel.get_text("//div[@id='content']/div[4]/fieldset/div[2]/div[2]/div[2]")

		return CreatedDate

	def addCasesToPlanFromOtherPlan(self,myself,sel,toTestplanName,testcaseIdNames,summary="<default>",\
			author="<default>",product="<default>",plan="<default>",priority="<default>",\
			automated="<default>",autoproposed="<default>",category="<default>",\
			status="<default>",component="<default>",bugID="<default>",tag="<default>"):
		''' Add case into a plan from another test plan. 'testcaseIdNames' is a 'dict' type para. '''

		self.openTestPlan(myself,sel,toTestplanName)

		self.clickCaseActionInPlan(myself,sel,"Add cases from other plans")
		self.verifyAddCasesFromOtherPlansPageIsReady(myself,sel,toTestplanName)

		self.fillDataForAddCasesFromOtherPlansPage(myself,sel,product=product,plan=plan)
		self.clickActionInAddCasesFromOtherPlansPage(myself,sel,"Search")
		self.verifyAddCasesFromOtherPlansPageIsReady(myself,sel,toTestplanName,testcaseIdNames=testcaseIdNames)

		self.selectCaseInAddCasesFromOtherPlansPage(myself,sel,testcaseIdNames.keys())
		self.clickActionInAddCasesFromOtherPlansPage(myself,sel,"Add selected cases")

		self.verifyTestPlanPageIsReady(myself,sel,toTestplanName)
		if testcaseIdNames!="<default>":
			
			if testcaseIdNames!="":
				for tId,tName in testcaseIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: self.verifyTargetText(myself,sel,"No test case found","css=center")


	# ========================================================================================================
	# 	Test Run related functions
	# ========================================================================================================


	def createTestRunFromPlan(self,myself,sel,testplanName,testrunName):
		''' Create a test run from a test plan. Note: the test run name is supposed to be unique. '''

		testrunId = ""

		self.openTestPlan(myself,sel,testplanName)

		self.clickCaseActionInPlan(myself,sel,"Write new run")
		self.verifyCreateTestRunPageIsReady(myself,sel)

		#Fill the data for a new test run form with provided data.
		self.fillDataForTestRun(myself,sel,summary=testrunName,product=env.product1,prodversion=env.prodversion11,build=env.build11,\
		runmanager=env.useremail,defaulttester=env.useremail)

		#save the test run
		self.clickActionInCreateRun(myself,sel,"Save")
		self.verifyTestRunPageIsReady(myself,sel,testrunName)

		testrunId = self.getTestRunId(myself,sel,testrunName)
		return testrunId

	def createCustomizedTestRunFromPlan(self,myself,sel,testplanName,summary="<default>",product="<default>",\
		prodversion="<default>",build="<default>",runmanager="<default>",defaulttester="<default>",estdays="<default>",\
		esthours="<default>",estmins="<default>",estsecs="<default>",notes="<default>",envGPPropOnoffs="<default>",envGPPropValues="<default>"):
		''' Create a test run from a test plan with provided data. Note: the test run name is supposed to be unique. '''

		testrunId = ""

		self.openTestPlan(myself,sel,testplanName)

		self.clickCaseActionInPlan(myself,sel,"Run")
		self.verifyCreateTestRunPageIsReady(myself,sel)

		#Fill the data for a new test run form with provided data.
		self.fillDataForTestRun(myself,sel,summary,product,prodversion,build,runmanager,\
		defaulttester,estdays,esthours,estmins,estsecs,notes,envGPPropOnoffs,envGPPropValues)

		#save the test run
		self.clickActionInCreateRun(myself,sel,"Save")
		self.verifyTestRunPageIsReady(myself,sel,summary,summary=summary,product=product,prodversion=prodversion,\
		build=build,runmanager=runmanager,defaulttester=defaulttester,estdays=estdays,\
		esthours=esthours,estmins=estmins,estsecs=estsecs,notes=notes,envGPPropOnoffs=envGPPropOnoffs,envGPPropValues=envGPPropValues)

		testrunId = self.getTestRunId(myself,sel,summary)
		return testrunId

	def openCreateTestRunFromPlan(self,myself,sel,testplanName,filterCase=True,\
		caseType="Test Cases",caseSummary="<default>",author="<default>",defaulttester="<default>",\
		priorityList="<default>",automated="<default>",autoproposed="<default>",category="<default>",\
		statusList="<default>",component="<default>",tag="<default>",testcaseResultIdNames="<default>",\
		testcaseResultNoIdNames="<default>"):
		''' Open the Create test run page from a test plan. '''

		self.openTestPlan(myself,sel,testplanName)

		if filterCase:
			self.filterCaseInPlan(myself,sel,caseType,caseSummary,author,defaulttester,priorityList,\
			automated,autoproposed,category,statusList,component,tag,testcaseResultIdNames,testcaseResultNoIdNames)

		#The para 'testcaseResultIdNames' is used to select the cases here and can be used for both 'filterCase=True' and 'filterCase=False'
		if testcaseResultIdNames!="<default>":
			self.selectTestCasesInPlan(myself,sel,testcaseResultIdNames.keys())

		self.clickCaseActionInPlan(myself,sel,"Write new run")
		self.verifyCreateTestRunPageIsReady(myself,sel)

	def openTestRun(self,myself,sel,testrunName):
		''' Open a test run from home page, if not exists, try to search it and then open it. 
			Note: the test run name is supposed to be unique.
		'''

		if self.isTestRunPageOpen(myself,sel,testrunName): return

		testrunId = ""
		if testrunName==env.testrunName: testrunId = env.testrunId
		elif testrunName==env.testrunName2: testrunId = env.testrunId2
		elif testrunName==env.testrunName3: testrunId = env.testrunId3
		elif testrunName==env.testrunName4: testrunId = env.testrunId4

		if not testrunId == "":
			sel.open("/run/"+testrunId+"/")
			time.sleep(env.tl)

			if not self.isTestRunPageOpen(myself,sel,testrunName):
				self.openHomePage(myself,sel)
				if not self.isLink(myself,sel,testrunName):
					self.searchTestRun(myself,sel,summary=testrunName)
				self.clickLinkAndWait(myself,sel,testrunName)
				self.verifyTestRunPageIsReady(myself,sel,testrunName)
		else:
			self.openHomePage(myself,sel)
			if not self.isLink(myself,sel,testrunName):
				self.searchTestRun(myself,sel,summary=testrunName)
			self.clickLinkAndWait(myself,sel,testrunName)
			self.verifyTestRunPageIsReady(myself,sel,testrunName)

	def openTestRunFromPlan(self,myself,sel,testplanName,testrunId,testrunName,clickRunIdOrName="id"):
		''' Open a test run from test plan. clickRunIdOrName's value involving: 'id','name' '''

		self.openTestPlan(myself,sel,testplanName)

		self.clickFirstLevelLinkByLabelNameInPlan(myself,sel,"Runs")
		if clickRunIdOrName=="id":
			self.clickLinkAndWait(myself,sel,testrunId)
		elif clickRunIdOrName=="name":
			self.clickLinkAndWait(myself,sel,testrunName)

		self.verifyTestRunPageIsReady(myself,sel,testrunName)

	def getTestRunId(self,myself,sel,testrunName):
		''' Get a test run id by open a test run. Note: the test run name is supposed to be unique. '''

		testrunId = ""

		self.openTestRun(myself,sel,testrunName)

		#Method 1: Get run id by navigation text in the top of the test run page
		tstr = sel.get_text("css=div.sprites.crumble")
		t1 = tstr.find('>> [')
		t2 = tstr.find('] '+testrunName)
		testrunId = tstr[t1+4:t2]

		return testrunId

	def getCaseRunIDInRun(self,myself,sel,testrunName,testcaseName):
		''' Get a case run id by open a test run. Note: the test run and test case name is supposed to be unique. '''

		testcaserunId = ""

		self.openTestRun(myself,sel,testrunName)

		self.expandCaseInRun(myself,sel,testcaseName)
		cururl = sel.get_location()
		t = cururl.find("#caserun_")
		testcaserunId = cururl[t+9:]

		self.expandCaseInRun(myself,sel,testcaseName)

		return testcaserunId

	def getCaseRunLineNoInRun(self,myself,sel,testrunName,testcaseName):
		''' Get the case run's line number in the case run table in the test run. '''

		LineNo = ""

		self.openTestRun(myself,sel,testrunName)

		self.verifyLink(myself,sel,testcaseName)
		for i in range(1,1000):
		       if self.isTargetText(myself,sel,testcaseName,"link_"+str(i)):
				LineNo = i
				break

		return LineNo

	def addCasesForRun(self,myself,sel,testrunName,testcaseIds):
		''' Add case which should be exists the same test plan of the test run for run. Note: the test run and test case name is supposed to be unique.

		    An example of the value of testcaseIds: testcaseIds=[testcaseId1,testcaseId2]
		    Example of call: CCommonUtils().AddCasesForRun(self,sel,testplanName,testrunName,[env.testcaseId]) '''

		self.openTestRun(myself,sel,testrunName)

		if testcaseIds=="":
			#(1)Verify if no case to choose, it will to return to the run when click "Update" button in run add case page.
			self.selectCaseAction(myself,sel,"Add")
			self.verifyTestRunAddCasePageIsReady(myself,sel,testrunName)

			self.clickActionInRunAddCasePage(myself,sel,"Update")
			self.verifyTestRunPageIsReady(myself,sel,testrunName)

		else:
			#(2)Verify if want to add mutiple cases, the cases you choose have been added to the "cases" table
			self.selectCaseAction(myself,sel,"Add")
			self.verifyTestRunAddCasePageIsReady(myself,sel,testrunName)

			self.selectTestCasesInRunAddCasePage(myself,sel,testcaseIds)
			self.clickActionInRunAddCasePage(myself,sel,"Update")
			self.verifyTestRunPageIsReady(myself,sel,testrunName)

			for i in range(len(testcaseIds)):
				self.verifyLink(myself,sel,testcaseIds[i])


	# ========================================================================================================
	# 	Clone test plan/case/run & clone warning page related functions
	# ========================================================================================================



	# ========================================================================================================
	# 	Search Plan/Case/Run page related functions
	# ========================================================================================================


	#----------------------------------------------------------------------
	#---------------------- (1) 'Search Plan' page ------------------------
	#----------------------------------------------------------------------

	def openSearchPlanPage(self,myself,sel):
		''' Open a Search Plan page from home page. '''

		self.clickMenu(myself,sel,"PLANNING","Search Plans")

		self.verifySearchPlanPageIsReady(myself,sel)

	def openSearchMyPlanPage(self,myself,sel):
		''' Open the Search My Plan page from home page. '''

		self.clickMenu(myself,sel,"TESTING","My Plans")

		self.verifySearchPlanPageIsReady(myself,sel,author=env.useremail)

	def searchTestPlan(self,myself,sel,planName="<default>",author="<default>",owner="<default>",\
			planType="<default>",tag="<default>",caseDefaultTester="<default>",product="<default>",\
			prodversion="<default>",envgroup="<default>",createdAfter="<default>",createdBefore="<default>",\
			active="<default>",testplanIdNames="<default>"):
		''' Search test plan by some search items. '''

		self.openSearchPlanPage(myself,sel)

		self.fillDataForSearchPlan(myself,sel,planName,author,owner,planType,tag,caseDefaultTester,\
			product,prodversion,envgroup,createdAfter,createdBefore,active)

		self.clickActionInSearchPlan(myself,sel,"Search")
		time.sleep(env.ts)

		self.verifySearchPlanPageIsReady(myself,sel,planName,author,owner,planType,tag,caseDefaultTester,\
			product,prodversion,envgroup,createdAfter,createdBefore,active,testplanIdNames)


	#----------------------------------------------------------------------
	#---------------------- (2) 'Search Case' page ------------------------
	#----------------------------------------------------------------------

	def openSearchCasePage(self,myself,sel):
		''' Open a Search Case page from home page. '''

		self.clickMenu(myself,sel,"TESTING","Search Cases")

		self.verifySearchCasePageIsReady(myself,sel)

	def searchTestCase(self,myself,sel,summary="<default>",author="<default>",product="<default>",plan="<default>",\
			priority="<default>",automated="<default>",autoproposed="<default>",category="<default>",\
			status="<default>",component="<default>",bugID="<default>",\
			tag="<default>",testcaseIdNames="<default>"):
		''' Search test case by some search items.

		    Example of call:
			CCommonUtils().searchTestCase(self,sel,summary=env.testcaseName,product=env.product1,automated="Auto",\
			category=env.category11,component=env.component11,autoproposed="1",priority=[1,2,3,4,5],status=[1,2,3,4])
		'''

		self.openSearchCasePage(myself,sel)

		self.fillDataForSearchCase(myself,sel,summary,author,product,plan,priority,automated,\
			autoproposed,category,status,component,bugID,tag)

		self.clickActionInSearchCase(myself,sel,"Search")
		time.sleep(env.ts)

		self.verifySearchCasePageIsReady(myself,sel,testcaseIdNames=testcaseIdNames)


	#----------------------------------------------------------------------
	#---------------------- (3) 'Search Run' page -------------------------
	#----------------------------------------------------------------------

	def openSearchRunPage(self,myself,sel):
		''' Open a Search Run page from home page. '''

		self.clickMenu(myself,sel,"TESTING","Search Runs")

		self.verifySearchRunPageIsReady(myself,sel)

	def openSearchMyRunPage(self,myself,sel):
		''' Open the Search My Run page from home page. '''

		self.clickMenu(myself,sel,"TESTING","My Runs")

		self.verifySearchRunPageIsReady(myself,sel,ownertype="Manager | Tester",owner=env.useremail)

	def searchTestRun(self,myself,sel,summary="<default>",plan="<default>",product="<default>",prodversion="<default>",\
			build="<default>",envgroup="<default>",status="<default>",ownertype="<default>",owner="<default>",\
			caserunassignee="<default>",tag="<default>",testrunIdNames="<default>"):
		''' Search test run by some search items. '''

		self.openSearchRunPage(myself,sel)

		self.fillDataForSearchRun(myself,sel,summary,plan,product,prodversion,build,\
			envgroup,status,ownertype,owner,caserunassignee,tag)

		self.clickActionInSearchRun(myself,sel,"Search")
		time.sleep(env.ts)

		self.verifySearchRunPageIsReady(myself,sel,summary,plan,product,prodversion,build,\
			envgroup,status,ownertype,owner,caserunassignee,tag,testrunIdNames)


	# ========================================================================================================
	# 	'Advanced Search' page related functions
	# ========================================================================================================


	def openAdvancedSearchPage(self,myself,sel):
		''' Open the Advanced Search page. '''

		self.clickLinkAndWait(myself,sel,"Advanced Search")

		self.verifyAdvancedSearchPageIsReady(myself,sel)

	def searchPlanByPlanOptInASearch(self,myself,sel,productList="<default>",componentList="<default>",\
		prodversionList="<default>",planId="<default>",summary="<default>",planTypeList="<default>",\
		author="<default>",owner="<default>",tag="<default>",tagOption="<default>",active="<default>",\
		createdAfter="<default>",createdBefore="<default>",resultIdNames="<default>",resultNoIdNames="<default>"):
		''' Search plan by Plan Options In the advanced search page. 'resultIdNames' is a 'dict' type para. '''

		self.openAdvancedSearchPage(myself,sel)

		self.fillDataForPlanItemsInASearch(myself,sel,productList,componentList,prodversionList,\
		planId,summary,planTypeList,author,owner,tag,tagOption,active,createdAfter,createdBefore)

		self.clickActionInAdvancedSearch(myself,sel,"Search Plan")
		self.verifyAdvancedSearchPlanResultIsReady(myself,sel,tIdNames=resultIdNames,tNoIdNames=resultNoIdNames)

	def searchCaseByCaseOptInASearch(self,myself,sel,productList="<default>",componentList="<default>",\
		categoryList="<default>",caseId="<default>",summary="<default>",author="<default>",\
		defaultTester="<default>",tag="<default>",tagOption="<default>",bugID="<default>",\
		statusList="<default>",automated="<default>",autoproposed="<default>",priorityList="<default>",\
		script="<default>",createdAfter="<default>",createdBefore="<default>",\
		resultIdNames="<default>",resultNoIdNames="<default>"):
		''' Search case by Case Options In the advanced search page. '''

		self.openAdvancedSearchPage(myself,sel)

		self.fillDataForCaseItemsInASearch(myself,sel,productList,componentList,\
		categoryList,caseId,summary,author,defaultTester,tag,tagOption,bugID,statusList,\
		automated,autoproposed,priorityList,script,createdAfter,createdBefore)

		self.clickActionInAdvancedSearch(myself,sel,"Search Case")
		self.verifyAdvancedSearchCaseResultIsReady(myself,sel,tIdNames=resultIdNames,tNoIdNames=resultNoIdNames)

	def searchRunByRunOptInASearch(self,myself,sel,productList="<default>",prodversionList="<default>",\
		buildList="<default>",runId="<default>",summary="<default>",manager="<default>",\
		defaultTester="<default>",actualTester="<default>",tag="<default>",tagOption="<default>",\
		status="<default>",runAfter="<default>",runBefore="<default>",\
		resultIdNames="<default>",resultNoIdNames="<default>"):
		''' Search run by Run Options In the advanced search page. '''

		self.openAdvancedSearchPage(myself,sel)

		self.fillDataForRunItemsInASearch(myself,sel,productList,prodversionList,buildList,\
		runId,summary,manager,defaultTester,actualTester,tag,tagOption,status,runAfter,runBefore)

		self.clickActionInAdvancedSearch(myself,sel,"Search Run")
		self.verifyAdvancedSearchRunResultIsReady(myself,sel,tIdNames=resultIdNames,tNoIdNames=resultNoIdNames)


	# ========================================================================================================
	# 	'Environment -> Groups' page related functions
	# ========================================================================================================


	def openEnvGroupsPage(self,myself,sel):
		''' Open Environment Groups from home page. '''

		self.openHomePage(myself,sel)
		self.clickMenu(myself,sel,"ENVIRONMENT","Groups")
		self.verifyEnvGroupsPageIsReady(myself,sel)


	# ========================================================================================================
	# 	'Admin -> Management' page related functions
	# ========================================================================================================


	def openManagementPage(self,myself,sel):
		''' Open 'Admin -> Management' page from home page. '''

		self.openHomePage(myself,sel)
		self.clickMenu(myself,sel,"ADMIN","Management")
		self.verifyManagementPageIsReady(myself,sel)


	# ========================================================================================================
	# 	'Reporting -> Testing Report' page related functions
	# ========================================================================================================


	def openTestingReportPage(self,myself,sel):
		''' Open 'Testing Report' page from home page. '''

		self.openHomePage(myself,sel)
		self.clickMenu(myself,sel,"REPORTING","Testing Report")
		self.verifyTestingReportPageIsReady(myself,sel)


	# ========================================================================================================
	# 	Other Common functions
	# ========================================================================================================

	def getFormatName(self,myself,sel,absPath,nameType):
		''' This function is used for getting uniformly formatted test plan/case/run Name when create new test plan/case/run in test case.
		    The value of 'absPath' should be as below: absPath = os.path.abspath(__file__)
		    The value of 'nameType' involving: "testplanName", "testcaseName", "testrunName"

		    Examples for call:
			absPath = os.path.abspath(__file__)
			testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
			testcaseName = cc().getFormatName(self,sel,absPath,"testcaseName")
			testrunName = cc().getFormatName(self,sel,absPath,"testrunName")
		'''

		testplanNameUni = "[Auto-%s]Test Plan created at: "+time.strftime('%Y'+'-'+'%m'+'-'+'%d'+' '+'%H'+':'+'%M'+':'+'%S') + " -> [%s]"
		testcaseNameUni = "[Auto-%s]Test Case created at: "+time.strftime('%Y'+'-'+'%m'+'-'+'%d'+' '+'%H'+':'+'%M'+':'+'%S') + " -> [%s]"
		testrunNameUni = "[Auto-%s]Test Run created at: "+time.strftime('%Y'+'-'+'%m'+'-'+'%d'+' '+'%H'+':'+'%M'+':'+'%S') + " -> [%s]"

		strPathWithDirAndFileName = os.path.split(absPath)
		strPathName = strPathWithDirAndFileName[0]
		strFileName = strPathWithDirAndFileName[1]
		strFileName = strFileName[:strFileName.find(".")]+".py" #Set the extension of the file as '.py' instead of '.pyc'
		
		#(1)To get the id str like 'ID84237' from the file name like 'tc_ID84237_InputNothing.py'.
		tStr = strFileName[3:]
		t = tStr.find('_')
		idStr = tStr[:t]

		#(2)To get the dir name, where the current case script will be, from the path name 'strPathName'.
		strDirName = strPathName
		t1 = strDirName.find(os.sep)
		while t1!=-1:
			strDirName = strDirName[t1+1:]
			t1 = strDirName.find(os.sep)

		#(3)To get the parent dir name from the path name 'strPathName'.
		t2 = strPathName.find(strDirName)
		strParDirName = (strPathName[:t2])[:-1]
		t2 = strParDirName.find(os.sep)
		while t2!=-1:
			strParDirName = strParDirName[t2+1:]
			t2 = strParDirName.find(os.sep)

		#(4)To get the parent's parent dir name from the path name 'strPathName'.
		t3 = strPathName.find(strParDirName + os.sep + strDirName)
		strParParDirName = (strPathName[:t3])[:-1]
		t3 = strParParDirName.find(os.sep)
		while t3!=-1:
			strParParDirName = strParParDirName[t3+1:]
			t3 = strParParDirName.find(os.sep)

		#(5)To remove pre-part of the file name to just leave the post-part of the file name behind
		#   For example, there will be the 'InputNothing.py' left over the script file 'tc_ID84237_InputNothing.py'.
		strPostPartFileName = strFileName[3:]
		t4 = strPostPartFileName.find("_")
		strPostPartFileName = strPostPartFileName[t4+1:]

		strFormatPath = strParParDirName + os.sep + strParDirName + os.sep + strDirName + os.sep + strPostPartFileName

		formatName = ""
		if nameType == "testplanName":	formatName = testplanNameUni%(idStr,strFormatPath)
		elif nameType == "testcaseName": formatName = testcaseNameUni%(idStr,strFormatPath)
		elif nameType == "testrunName":	formatName = testrunNameUni%(idStr,strFormatPath)

		return formatName

	def getAutoDataFormatName(self,myself,sel,nameType,dataNo,dataSuiteSymbol):
		''' This function is used for getting uniformly formatted test plan/case/run Name when create new test plan/case/run for automation data use.
		    The value of 'nameType' involving: "testplanName", "testcaseName", "testrunName"

		    Examples for call:
			testplanName = cc().getAutoDataFormatName(self,sel,"testplanName","1","01")
			testcaseName = cc().getAutoDataFormatName(self,sel,"testcaseName","1","01")
			testrunName  = cc().getAutoDataFormatName(self,sel,"testrunName","1","01")
		'''

		testplanNameUni = "TestPlan%s_%s For automation only"
		testcaseNameUni = "TesetCase%s_%s For automation only"
		testrunNameUni = "TesetRun%s_%s For automation only"

		formatName = ""
		if nameType == "testplanName":
			formatName = testplanNameUni%(dataNo,dataSuiteSymbol)
			if not (len(formatName)>6): myself.fail("The length of the test plan name: '" + formatName + "' should be more than 6!")
			
		elif nameType == "testcaseName":
			formatName = testcaseNameUni%(dataNo,dataSuiteSymbol)
			if not (len(formatName)>8): myself.fail("The length of the test case name: '" + formatName + "' should be more than 8!")

		elif nameType == "testrunName":
			formatName = testrunNameUni%(dataNo,dataSuiteSymbol)
			if not (len(formatName)>8): myself.fail("The length of the test run name: '" + formatName + "' should be more than 8!")

		return formatName

	def replaceStrInFile(self,myself,sel,filePath,replaceStrDict):
		''' This function is used replace string in a file. '''
		#write data into data file
		newStr=""
		f = file(filePath, 'r')
		for eachLine in f:
			for oStr,rStr in replaceStrDict.items():
				if eachLine.find(oStr)>0: eachLine=eachLine.replace(oStr,rStr)
			newStr+=eachLine
		f = file(filePath, 'w') # open for 'w'riting
		f.write(newStr) # write text to file
		f.close()

