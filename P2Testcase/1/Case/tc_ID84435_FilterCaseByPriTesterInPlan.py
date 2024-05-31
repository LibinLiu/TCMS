from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class FilterCaseByPriTesterInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_FilterCaseByPriTesterInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Change the priority from 'P1' to 'P2' for the test case 'env.testcaseId42'
	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	cc().editTestCase(self,sel,env.testcaseName42,priority="P2")

	cc().openTestPlan(self,sel,env.testplanName4)

	#Filter test case by category and component in plan
	cc().filterCaseInPlan(self,sel,defaulttester=env.user,priorityList=[2],testcaseResultIdNames={env.testcaseId42:env.testcaseName42})
	cc().verifyLinkNotPresent(self,sel,env.testcaseId41)

	#Restore the priority from 'P2' to 'P1' for the test case 'env.testcaseId42'
	cc().clickLink(self,sel,env.testcaseId42)
	cc().editTestCase(self,sel,env.testcaseName42,priority="P1")


    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
