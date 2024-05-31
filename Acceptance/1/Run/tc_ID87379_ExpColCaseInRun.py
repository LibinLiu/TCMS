from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ExpColCaseInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ExpColCaseInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestRun(self,sel,env.testrunName4)

	#Expand/Collapse all test cases in test run
	for i in range(10):
		cc().expandCaseInRun(self,sel,"All")
		cc().verifyText(self,sel,"Application")
		cc().verifyText(self,sel,"Database")

		cc().expandCaseInRun(self,sel,"All")
		cc().verifyTextNotPresent(self,sel,"Application")
		cc().verifyTextNotPresent(self,sel,"Database")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
