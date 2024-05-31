from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class UpdateCaseForRunWithoutCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_UpdateCaseForRunWithoutCase(self):
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

	#Execute test
	#Remove 2 test cases
	cc().selectCaseInRun(self,sel,"All")
	cc().selectCaseAction(self,sel,"Remove",removecaseNum="2")
	cc().verifyTestRunAddCasePageIsReady(self,sel,testrunName)

	cc().selectTestCasesInRunAddCasePage(self,sel,[testcaseId1,testcaseId2])
	cc().clickActionInRunAddCasePage(self,sel,"Update")
	cc().verifyTestRunPageIsReady(self,sel,testrunName)

	#Verify the 2 cases are shown in the case list
	cc().verifyLink(self,sel,testcaseId1)
	cc().verifyLink(self,sel,testcaseId2)


    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
