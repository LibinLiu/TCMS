from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class RemoveComponentInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveComponentInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	cc().addComponentInCase(self,sel,env.product1,[env.component12,env.component14])

	cc().removeComponentInCase(self,sel,[env.componentId12,env.componentId14])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
