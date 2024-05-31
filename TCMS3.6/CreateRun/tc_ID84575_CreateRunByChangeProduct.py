from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class CreateRunByChangeProduct(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateRunByChangeProduct(self):
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
	cc().openCreateTestRunFromPlan(self,sel,testplanName,caseSummary=testcaseName1,\
		testcaseResultIdNames={testcaseId1:testcaseName1})

	#Fill the data for a new test run form with provided data.
	cc().fillDataForTestRun(self,sel,summary=testrunName,product=env.product2)

	#save the test run
	cc().clickActionInCreateRun(self,sel,"Save")
	cc().verifyTestRunPageIsReady(self,sel,testrunName,summary=testrunName,product=env.product2,\
		testcaseIds=[testcaseId1])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
