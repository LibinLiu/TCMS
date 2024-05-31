from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class EditAutomated(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_EditAutomated(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#Set Automated for more than 1 Cases
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41,env.testcaseId42])
	cc().setAutomatedForCaseInPlan(self,sel,["Manual"])

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,automated="Manual")

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName42,automated="Manual")

	#Restore Automated for more than 1 Cases
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41,env.testcaseId42])
	cc().setAutomatedForCaseInPlan(self,sel,["Automated"])

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,automated="Auto")

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName42,automated="Auto")
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
