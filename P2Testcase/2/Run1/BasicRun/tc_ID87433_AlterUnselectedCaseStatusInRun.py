from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class AlterUnselectedCaseStatusInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AlterUnselectedCaseStatusInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestRun(self,sel,env.testrunName4)
        cc().alterCaseRunStatus(self,sel,"PASSED",selectedCase=False)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
