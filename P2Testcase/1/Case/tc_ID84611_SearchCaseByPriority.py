from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseByPriority(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseByPriority(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Search test case by priority
	cc().searchTestCase(self,sel,summary=env.testcaseName,priority=[1,2],\
		testcaseIdNames={env.testcaseId:env.testcaseName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
