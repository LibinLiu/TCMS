from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchPlanCaseByRunItemInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchPlanCaseByRunItemInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	#Add a tag in run
	cc().openTestRun(self,sel,env.testrunName)

	rdm=random.uniform(1, 1000)
	tagName = "aa@@bb333"+str(rdm)
	cc().addTagInRun(self,sel,tagName,needRemove=False)

	#--(B) Execute test
	#(1)Search test plan
	cc().openAdvancedSearchPage(self,sel)

	#Fill in the test run information
	cc().fillDataForRunItemsInASearch(self,sel,productList=[env.product1],prodversionList=[env.prodversion11],\
		buildList=[env.build11],runId=env.testrunId,summary=env.testrunName,manager=env.user,\
		defaultTester=env.user,actualTester="",tag=tagName,tagOption="Contains",\
		status="All",runAfter="2000-01-01",runBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

        cc().clickActionInAdvancedSearch(self,sel,"Search Plan")
	cc().verifyAdvancedSearchPlanResultIsReady(self,sel,tIdNames={env.testplanId:env.testplanName})

	#(2)Search test case
	cc().openAdvancedSearchPage(self,sel)

	#Fill in the test run information
	cc().fillDataForRunItemsInASearch(self,sel,productList=[env.product1],prodversionList=[env.prodversion11],\
		buildList=[env.build11],runId=env.testrunId,summary=env.testrunName,manager=env.user,\
		defaultTester=env.user,actualTester="",tag=tagName,tagOption="Contains",\
		status="All",runAfter="2000-01-01",runBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

        cc().clickActionInAdvancedSearch(self,sel,"Search Case")
	cc().verifyAdvancedSearchCaseResultIsReady(self,sel,tIdNames={env.testcaseId:env.testcaseName})

	#--(C) Remove test data
	#Remove the added tag from test run
	cc().openTestRun(self,sel,env.testrunName)
	cc().removeTagInRun(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
