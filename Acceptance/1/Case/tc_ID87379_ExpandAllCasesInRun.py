from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class ExpandAllCasesInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ExpandAllCasesInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

	cc().openTestRun(self,sel,env.testrunName4)

	for i in range(10):
		#Verify all cases can be expanded
		cc().expandCaseInRun(self,sel,"All")
		cc().verifyText(self,sel,env.component41)
		cc().verifyText(self,sel,env.component42)

		#Verify all cases can be collapsed
		cc().expandCaseInRun(self,sel,"All")
		cc().verifyTextNotPresent(self,sel,env.component41)
		cc().verifyTextNotPresent(self,sel,env.component42)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
