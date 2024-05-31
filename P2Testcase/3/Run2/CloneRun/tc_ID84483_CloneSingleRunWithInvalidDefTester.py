from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class CloneSingleRunWithInvalidDefTester(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneSingleRunWithInvalidDefTester(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data
	cc().openTestRun(self,sel,env.testrunName)

	#Execute test
	cc().selectCaseInRun(self,sel,"All")
	cc().clickActionInRun(self,sel,"Clone")
	cc().verifyCloneTestRunPageIsReady(self,sel,env.testrunName)

	#Input Invalid Default Tester In the test Run and then save it
	DefaultTesterName="aabb"+env.useremail
	cc().fillDataForTestRun(self,sel,defaulttester=DefaultTesterName)
	cc().clickActionInCloneTestRun(self,sel,"Save")
	cc().verifyCreateTestRunPageIsReady(self,sel)
	cc().verifyErrWarningMsgInCreateTestRun(self,sel,"Invalid Default Tester",wrongUser=DefaultTesterName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
