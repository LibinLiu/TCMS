from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CheckRunProgBarInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CheckRunProgBarInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#1) change status to 'PASSED'
	cc().openTestRun(self,sel,env.testrunName)
	cc().selectCaseInRun(self,sel,[env.testcaserunId])
	cc().alterCaseRunStatus(self,sel,"PASSED")
	
	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName,"PASSED")
	
	#2) check the test run progress bar in test plan
	cc().openTestPlan(self,sel,env.testplanName)
	cc().verifyRunProgBarInPlan(self,sel,successpercent="100%")

	#3) restore status to 'IDLE'
	cc().openTestRun(self,sel,env.testrunName)
	cc().selectCaseInRun(self,sel,[env.testcaserunId])
	cc().alterCaseRunStatus(self,sel,"IDLE")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName,"IDLE")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
