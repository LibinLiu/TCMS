from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddCaseIntoMorePlanInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddCaseIntoMorePlanInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#(1)Add the case into another plan
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().addTestPlanInCase(self,sel,testplanIdNames={env.testplanId2:env.testplanName2})
	cc().removeTestPlanInCase(self,sel,[env.testplanId2],env.testcaseId)

	#(2)Add the case into multiple plans split with comma
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().addTestPlanInCase(self,sel,testplanIdNames={env.testplanId2:env.testplanName2,env.testplanId3:env.testplanName3})
	cc().removeTestPlanInCase(self,sel,[env.testplanId2,env.testplanId3],env.testcaseId)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
