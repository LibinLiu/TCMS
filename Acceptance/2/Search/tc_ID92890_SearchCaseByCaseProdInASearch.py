from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseByCaseProdInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseByCaseProdInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)

	cc().verifyHomePageIsReady(self,sel)

	cc().openAdvancedSearchPage(self,sel)

	cc().fillDataForCaseItemsInASearch(self,sel,productList=[env.product1],caseId=env.testcaseId)

	cc().clickActionInAdvancedSearch(self,sel,"Search Case")
	cc().verifyAdvancedSearchCaseResultIsReady(self,sel,tIdNames={env.testcaseId:env.testcaseName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
