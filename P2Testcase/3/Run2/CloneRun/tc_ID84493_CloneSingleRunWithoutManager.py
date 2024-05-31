from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class CloneSingleRunWithoutManager(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneSingleRunWithoutManager(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	cc().openTestRun(self,sel,env.testrunName)

	#(2)Execute test
	cc().selectCaseInRun(self,sel,"All")
	cc().clickActionInRun(self,sel,"Clone")
	cc().verifyCloneTestRunPageIsReady(self,sel,env.testrunName)

	#Input Manager as null In the test Run and then save it
	cc().fillDataForTestRun(self,sel,runmanager="")
	cc().clickActionInCloneTestRun(self,sel,"Save")
	cc().verifyCreateTestRunPageIsReady(self,sel)
	cc().verifyErrWarningMsgInCreateTestRun(self,sel,"Blank Run Manager",wrongUser="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
