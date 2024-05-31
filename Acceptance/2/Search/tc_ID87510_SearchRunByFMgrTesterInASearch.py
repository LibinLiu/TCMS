from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchRunByFMgrTesterInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchRunByFMgrTesterInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	''' Note: Due to bug existing in below function, so commentated below auto script 
	#(A)Single-user fuzzy search
	#(1)Search test run by fuzzy author
	cc().openAdvancedSearchPage(self,sel)
	cc().fillDataForRunItemsInASearch(self,sel,runId=env.testrunId,manager=env.user[:3])

	cc().clickActionInAdvancedSearch(self,sel,"Search Run")
	cc().verifyAdvancedSearchRunResultIsReady(self,sel,tIdNames={env.testrunId:env.testrunName})
	#(2)Search test run by fuzzy default tester
	cc().openAdvancedSearchPage(self,sel)
	cc().fillDataForRunItemsInASearch(self,sel,runId=env.testrunId,defaultTester=env.user[:3])

	cc().clickActionInAdvancedSearch(self,sel,"Search Run")
	cc().verifyAdvancedSearchRunResultIsReady(self,sel,tIdNames={env.testrunId:env.testrunName})
	'''

	#(B)Multi-user fuzzy search
	#(1)Search test run by fuzzy author
	cc().openAdvancedSearchPage(self,sel)
	cc().fillDataForRunItemsInASearch(self,sel,runId=env.testrunId,manager=env.user+", mytester1x, mytester2x")

	cc().clickActionInAdvancedSearch(self,sel,"Search Run")
	cc().verifyAdvancedSearchRunResultIsReady(self,sel,tIdNames={env.testrunId:env.testrunName})

	#(2)Search test run by fuzzy default tester
	cc().openAdvancedSearchPage(self,sel)
	cc().fillDataForRunItemsInASearch(self,sel,runId=env.testrunId,defaultTester=env.user+", mytester1x, mytester2x")

	cc().clickActionInAdvancedSearch(self,sel,"Search Run")
	cc().verifyAdvancedSearchRunResultIsReady(self,sel,tIdNames={env.testrunId:env.testrunName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
