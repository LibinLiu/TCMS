from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AlterCaseRunStatusInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_AlterCaseRunStatusInRun(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestRun(self,sel,env.testrunName4)
	
	#--(A) Choose one case.
	#(1)change status to BLOCKED
	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().alterCaseRunStatus(self,sel,"BLOCKED")
	
	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"BLOCKED")
	
	#(2)restore status to IDLE
	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().alterCaseRunStatus(self,sel,"IDLE")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"IDLE")


	#--(B) Choose more cases.
	#(1)change status to BLOCKED
	cc().selectCaseInRun(self,sel,[env.testcaserunId41,env.testcaserunId42])
	cc().alterCaseRunStatus(self,sel,"BLOCKED")
	
	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"BLOCKED")
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName42,"BLOCKED")
	
	#(2)restore status to IDLE
	cc().selectCaseInRun(self,sel,[env.testcaserunId41,env.testcaserunId42])
	cc().alterCaseRunStatus(self,sel,"IDLE")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"IDLE")
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName42,"IDLE")


	#--(C) Choose all cases.
	#(1)change status to BLOCKED
	cc().selectCaseInRun(self,sel,"All")
	cc().alterCaseRunStatus(self,sel,"BLOCKED")
	
	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"BLOCKED")
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName42,"BLOCKED")
	
	#(2)restore status to IDLE
	cc().selectCaseInRun(self,sel,[env.testcaserunId41,env.testcaserunId42])
	cc().alterCaseRunStatus(self,sel,"IDLE")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"IDLE")
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName42,"IDLE")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
