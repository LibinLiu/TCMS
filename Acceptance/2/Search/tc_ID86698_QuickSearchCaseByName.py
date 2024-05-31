from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class QuickSearchCaseByName(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_QuickSearchCaseByName(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Accurate search
	cc().quickSearch(self,sel,"Test Case",env.testcaseName)
	cc().verifySearchCasePageIsReady(self,sel,testcaseIdNames={env.testcaseId:env.testcaseName})

	#(2)Fuzzy search
	cc().quickSearch(self,sel,"Test Case",(env.testcaseName)[:8])
	cc().verifySearchCasePageIsReady(self,sel,testcaseIdNames={env.testcaseId:env.testcaseName})

	#(3)False search
	cc().quickSearch(self,sel,"Test Case",(env.testcaseName)[:8]+"88888")
	cc().verifySearchCasePageIsReady(self,sel,testcaseIdNames="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
