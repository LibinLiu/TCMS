from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class AddInvalidCCInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddInvalidCCInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)
	cc().addCCInRun(self,sel,invalidUserEmail="aaabbb")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
