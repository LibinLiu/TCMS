from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddTagForRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddTagForRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)

	tagName = "aa@@aa11"
	cc().addTagInRun(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
