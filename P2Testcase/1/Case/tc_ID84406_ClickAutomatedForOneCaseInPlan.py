from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClickAutomatedForOneCaseInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClickAutomatedForOneCaseInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#Set the test case as "Manual" and "Autoproposed"
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41])
	cc().setAutomatedForCaseInPlan(self,sel,["Manual","Autoproposed"])

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,automated="Manual(Autoproposed)")

	#Restore to set the test case as "Automated"
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41])
	cc().setAutomatedForCaseInPlan(self,sel,["Automated"])

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,automated="Auto")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
