from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class RemoveCaseForRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveCaseForRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	testcaseName2=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId2 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName2)

	testrunName=cc().getFormatName(self,sel,absPath,"testrunName")
	testrunId = cc().createTestRunFromPlan(self,sel,testplanName,testrunName)
	testcaserunId1=cc().getCaseRunIDInRun(self,sel,testrunName,testcaseName1)

	#Execute test
	#(1) - Remove just 1 test case
	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().selectCaseAction(self,sel,"Remove",removecaseNum="1")
	cc().verifyLinkNotPresent(self,sel,testcaseId1)

	cc().addCasesForRun(self,sel,testrunName,[testcaseId1])

	#(2) - Remove 2 test cases
	cc().selectCaseInRun(self,sel,"All")
	cc().selectCaseAction(self,sel,"Remove",removecaseNum="2")
	cc().verifyTestRunAddCasePageIsReady(self,sel,testrunName)

	#Verify the 2 cases exist in the add case page
	cc().verifyLink(self,sel,testcaseId1)
	cc().verifyLink(self,sel,testcaseId2)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
