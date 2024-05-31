from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class AddInvalidPlanIDInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddInvalidPlanIDInCase(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	invalidTPId=env.testplanId2+"123321"
	cc().addTestPlanInCase(self,sel,invalidTestPlanIds=[invalidTPId])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
