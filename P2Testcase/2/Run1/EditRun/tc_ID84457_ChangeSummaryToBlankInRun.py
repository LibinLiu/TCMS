from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ChangeSummaryToBlankInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ChangeSummaryToBlankInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#open Test Run From Plan by clicking test run name in plan
	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName,clickRunIdOrName="name")

	#Change the run summary to blank and then save it
	runNameNew=""
	cc().editTestRun(self,sel,env.testrunName,summary=runNameNew)
	cc().verifyErrWarningMsgInEditTestRun(self,sel,"Blank Summary")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
