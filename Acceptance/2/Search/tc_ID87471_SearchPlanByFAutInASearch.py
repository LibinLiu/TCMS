from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchPlanByFAutInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchPlanByFAutInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	''' Note: Due to bug existing in below function, so commentated below auto script 
	#(A)Single-user fuzzy search
	cc().openAdvancedSearchPage(self,sel)

	cc().fillDataForPlanItemsInASearch(self,sel,planId=env.testplanId,author=env.user[:len(env.user)-2])
        cc().clickActionInAdvancedSearch(self,sel,"Search Plan")

	cc().verifyAdvancedSearchPlanResultIsReady(self,sel,tIdNames={env.testplanId:env.testplanName})
	'''

	#(B)Multi-user fuzzy search
	cc().openAdvancedSearchPage(self,sel)

	cc().fillDataForPlanItemsInASearch(self,sel,planId=env.testplanId,author=env.user+", mytester1x, mytester2x")
        cc().clickActionInAdvancedSearch(self,sel,"Search Plan")

	cc().verifyAdvancedSearchPlanResultIsReady(self,sel,tIdNames={env.testplanId:env.testplanName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
