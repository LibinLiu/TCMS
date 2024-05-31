from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreateRunInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateRunInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName)

	testrunName=cc().getFormatName(self,sel,absPath,"testrunName")
	testrunId = cc().createTestRunFromPlan(self,sel,testplanName,testrunName)
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
