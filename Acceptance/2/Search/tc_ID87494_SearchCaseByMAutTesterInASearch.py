from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseByMAutTesterInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_SearchCaseByMAutTesterInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Search test case by fuzzy author
	cc().openAdvancedSearchPage(self,sel)
	cc().fillDataForCaseItemsInASearch(self,sel,caseId=env.testcaseId,author=env.user+", mytester1x, mytester2x")

	cc().clickActionInAdvancedSearch(self,sel,"Search Case")
	cc().verifyAdvancedSearchCaseResultIsReady(self,sel,tIdNames={env.testcaseId:env.testcaseName})

	#(2)Search test case by fuzzy default tester
	cc().openAdvancedSearchPage(self,sel)
	cc().fillDataForCaseItemsInASearch(self,sel,caseId=env.testcaseId,defaultTester=env.user+", mytester1x, mytester2x")

	cc().clickActionInAdvancedSearch(self,sel,"Search Case")
	cc().verifyAdvancedSearchCaseResultIsReady(self,sel,tIdNames={env.testcaseId:env.testcaseName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
