from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class FilterCaseByCaseStatusInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_FilterCaseByCaseStatusInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName4)

	cc().filterCaseInPlan(self,sel,caseSummary=env.testcaseName41,statusList=[2],testcaseResultIdNames={env.testcaseId41:env.testcaseName41})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
