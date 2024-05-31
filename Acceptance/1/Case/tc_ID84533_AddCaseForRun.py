from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddCaseForRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddCaseForRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	testrunName=cc().getFormatName(self,sel,absPath,"testrunName")
	testrunId = cc().createTestRunFromPlan(self,sel,testplanName,testrunName)

	testcaseName2=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId2 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName2)

	#To add some new case and verify the case you choose has been added to the "cases" table
	cc().addCasesForRun(self,sel,testrunName,[testcaseId2])
	cc().verifyLink(self,sel,testcaseId1)
	cc().verifyLink(self,sel,testcaseId2)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
