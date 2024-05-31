from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClickAddWithoutTagName(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClickAddWithoutTagName(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	tagName=""
	cc().addTagInCase(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
