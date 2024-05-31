from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchPlanRunByCaseItemInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchPlanRunByCaseItemInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	#Add a tag and bug in test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	rdm=random.uniform(1, 1000)
	tagName = "aa@@bb222"+str(rdm)
	cc().addTagInCase(self,sel,tagName)
	cc().addBugInCase(self,sel,env.bugno,env.bugurl)

	#--(B) Execute test
	#(1)Search test plan
	cc().openAdvancedSearchPage(self,sel)

	#Fill in the test case information
	cc().fillDataForCaseItemsInASearch(self,sel,productList=[env.product1],componentList=[env.component11],\
		categoryList=[env.category11],caseId=env.testcaseId,summary=env.testcaseName,author=env.user,\
		defaultTester=env.user,tag=tagName,tagOption="Contains",bugID=env.bugno,\
		statusList=[1,2,3,4],automated="Automated",autoproposed="Non Auto Proposed",priorityList=[1,2,3,4,5],\
		script="",createdAfter="2000-01-01",createdBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

        cc().clickActionInAdvancedSearch(self,sel,"Search Plan")
	cc().verifyAdvancedSearchPlanResultIsReady(self,sel,tIdNames={env.testplanId:env.testplanName})

	#(2)Search test run
	cc().openAdvancedSearchPage(self,sel)

	#Fill in the test case information
	cc().fillDataForCaseItemsInASearch(self,sel,productList=[env.product1],componentList=[env.component11],\
		categoryList=[env.category11],caseId=env.testcaseId,summary=env.testcaseName,author=env.user,\
		defaultTester=env.user,tag=tagName,tagOption="Contains",bugID=env.bugno,\
		statusList=[1,2,3,4],automated="Automated",autoproposed="Non Auto Proposed",priorityList=[1,2,3,4,5],\
		script="",createdAfter="2000-01-01",createdBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

        cc().clickActionInAdvancedSearch(self,sel,"Search Run")
	cc().verifyAdvancedSearchRunResultIsReady(self,sel,tIdNames={env.testrunId:env.testrunName})

	#--(C) Remove test data
	#Remove the added tag and bug from test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().removeTagInCase(self,sel,tagName)
	cc().removeBugInCase(self,sel,env.testcaseId,env.bugno,env.bugurl)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
