from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreateRunWithInvalidRunManager(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateRunWithInvalidRunManager(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,caseSummary=env.testcaseName41,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41},\
		testcaseResultNoIdNames={env.testcaseId42:env.testcaseName42})

	#Input Invalid Default Tester In the test Run
	DefaultTesterName="aabb"+env.useremail
	cc().fillDataForTestRun(self,sel,defaulttester=DefaultTesterName)

	#save the test run
	cc().clickActionInCreateRun(self,sel,"Save")
	cc().verifyCreateTestRunPageIsReady(self,sel)
	cc().verifyErrWarningMsgInCreateTestRun(self,sel,"Invalid Run Manager",wrongUser=DefaultTesterName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
