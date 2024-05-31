from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class RemoveNoComponentInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveNoComponentInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	cc().addComponentInCase(self,sel,env.product1,[env.component14])

	cc().removeComponentInCase(self,sel,"")
	cc().verifyText(self,sel,env.component14)

	cc().removeComponentInCase(self,sel,[env.componentId14])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
