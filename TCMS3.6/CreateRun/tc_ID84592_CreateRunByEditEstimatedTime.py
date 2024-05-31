from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreateRunByEditEstimatedTime(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateRunByEditEstimatedTime(self):
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

	#(2)Execute test
	cc().createCustomizedTestRunFromPlan(self,sel,testplanName,summary=testrunName,estdays="1",esthours="2",estmins="3",estsecs="10")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
