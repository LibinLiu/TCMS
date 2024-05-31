from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class ClickCaserunidOrNameInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClickCaserunidOrNameInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestRun(self,sel,env.testrunName4)

	#expand test case by clicking test case name
	cc().expandCaseInRun(self,sel,env.testcaseName41)
	cc().verifyText(self,sel,env.component41)

	#collapse test case by clicking test case name
	cc().expandCaseInRun(self,sel,env.testcaseName41)
	cc().verifyTextNotPresent(self,sel,env.component41)
	
	#expand test case by clicking test case run id
	cc().expandCaseInRun(self,sel,env.testcaseName41,testcaserunId=env.testcaserunId41)
	cc().verifyText(self,sel,env.component41)

	#collapse test case by clicking test case run id
	cc().expandCaseInRun(self,sel,env.testcaseName41,testcaserunId=env.testcaserunId41)
	cc().verifyTextNotPresent(self,sel,env.component41)
	

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
