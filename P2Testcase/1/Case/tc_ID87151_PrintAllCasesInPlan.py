from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class PrintAllCasesInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_PrintAllCasesInPlan(self):
	sel = self.selenium
	sel.open(env.openurl)

	cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,"All")
	cc().clickCaseActionInPlan(self,sel,"Print")

	cc().verifyPrintTestPlanPageIsReady(self,sel,{env.testplanId4:env.testplanName4},\
		testcaseIdNames={env.testcaseId41:env.testcaseName41,env.testcaseId42:env.testcaseName42})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
