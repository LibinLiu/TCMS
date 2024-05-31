from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class CloneSingleRunWithoutDefTester(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneSingleRunWithoutDefTester(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	testrunName=cc().getFormatName(self,sel,absPath,"testrunName")
	testrunId = cc().createTestRunFromPlan(self,sel,testplanName,testrunName)

	#(2)Execute test
	cc().selectCaseInRun(self,sel,"All")
	cc().clickActionInRun(self,sel,"Clone")
	cc().verifyCloneTestRunPageIsReady(self,sel,testrunName)

	cc().fillDataForTestRun(self,sel,defaulttester="")
	cc().clickActionInCloneTestRun(self,sel,"Save")
	cc().verifyTestRunPageIsReady(self,sel,testrunName,defaulttester="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
