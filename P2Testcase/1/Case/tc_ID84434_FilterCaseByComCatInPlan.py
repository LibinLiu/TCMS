from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class FilterCaseByComCatInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_FilterCaseByComCatInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName4)

	#Filter test case by category and component in plan
	cc().filterCaseInPlan(self,sel,category=env.category11,component=env.component41,testcaseResultIdNames={env.testcaseId41:env.testcaseName41})
	cc().verifyLinkNotPresent(self,sel,env.testcaseId42)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
