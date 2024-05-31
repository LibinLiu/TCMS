from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class CreateRunWithoutSummary(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateRunWithoutSummary(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,caseSummary=env.testcaseName41,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41},\
		testcaseResultNoIdNames={env.testcaseId42:env.testcaseName42})

	#Fill the data for a new test run form with provided data.
	cc().fillDataForTestRun(self,sel,summary="")

	#save the test run
	cc().clickActionInCreateRun(self,sel,"Save")
	cc().verifyCreateTestRunPageIsReady(self,sel)
	cc().verifyErrWarningMsgInCreateTestRun(self,sel,"Blank Summary")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
