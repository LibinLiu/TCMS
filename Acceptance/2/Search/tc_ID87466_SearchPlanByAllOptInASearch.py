from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchPlanByAllOptInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchPlanByAllOptInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	#Add a new tag and component in test plan
	cc().openTestPlan(self,sel,env.testplanName)

	rdm=random.uniform(1, 1000)
	tagName1 = "aa@@bb111"+str(rdm)
	cc().addTagInPlan(self,sel,tagName1,needRemove=False)
	cc().addComponentInPlan(self,sel,[env.component12])

	#Add a tag and bug in test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	rdm=random.uniform(1, 1000)
	tagName2 = "aa@@bb222"+str(rdm)
	cc().addTagInCase(self,sel,tagName2)
	cc().addBugInCase(self,sel,env.bugno,env.bugurl)

	#Add a tag in run
	cc().openTestRun(self,sel,env.testrunName)

	rdm=random.uniform(1, 1000)
	tagName3 = "aa@@bb333"+str(rdm)
	cc().addTagInRun(self,sel,tagName3,needRemove=False)

	#--(B) Execute test
	#Search plan by all information
	cc().openAdvancedSearchPage(self,sel)

	#(1)Fill in the test plan information
	cc().fillDataForPlanItemsInASearch(self,sel,productList=[env.product1],componentList=[env.component12],\
		prodversionList=[env.prodversion11],planId=env.testplanId,\
		summary=env.testplanName,planTypeList=[env.plantype11],author=env.user,\
		owner=env.user,tag=tagName1,tagOption="Contains",active="Active",\
		createdAfter="2000-01-01",createdBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

	#(2)Fill in the test case information
	cc().fillDataForCaseItemsInASearch(self,sel,productList=[env.product1],componentList=[env.component11],\
		categoryList=[env.category11],caseId=env.testcaseId,summary=env.testcaseName,author=env.user,\
		defaultTester=env.user,tag=tagName2,tagOption="Contains",bugID=env.bugno,\
		statusList=[1,2,3,4],automated="Automated",autoproposed="Non Auto Proposed",priorityList=[1,2,3,4,5],\
		script="",createdAfter="2000-01-01",createdBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

	#(3)Fill in the test run information
	cc().fillDataForRunItemsInASearch(self,sel,productList=[env.product1],prodversionList=[env.prodversion11],\
		buildList=[env.build11],runId=env.testrunId,summary=env.testrunName,manager=env.user,\
		defaultTester=env.user,actualTester="",tag=tagName3,tagOption="Contains",\
		status="All",runAfter="2000-01-01",runBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

        cc().clickActionInAdvancedSearch(self,sel,"Search Plan")
	cc().verifyAdvancedSearchPlanResultIsReady(self,sel,tIdNames={env.testplanId:env.testplanName})

	#--(C) Remove test data
	#Remove the added tag and component from test plan
	cc().openTestPlan(self,sel,env.testplanName)
	cc().removeTagInPlan(self,sel,[tagName1])
	cc().removeComponentInPlan(self,sel,{env.componentId12:env.component12})

	#Remove the added tag and bug from test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().removeTagInCase(self,sel,tagName2)
	cc().removeBugInCase(self,sel,env.testcaseId,env.bugno,env.bugurl)

	#Remove the added tag from test run
	cc().openTestRun(self,sel,env.testrunName)
	cc().removeTagInRun(self,sel,tagName3)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
