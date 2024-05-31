from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CloneSingleRunWithFilteredCaseRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneSingleRunWithFilteredCaseRun(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
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

	#(2)Execute test
	cc().openTestRun(self,sel,testrunName)
	cc().filterCaseInRun(self,sel,summary=testcaseName1,testcaseResultIdNames={testcaseId1:testcaseName1},\
		testcaseResultNoIdNames={testcaseId2:testcaseName2})

	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().clickActionInRun(self,sel,"Clone")
	cc().verifyCloneTestRunPageIsReady(self,sel,testrunName,testcaseIdNames={testcaseId1:testcaseName1},\
		testcaseNoIdNames={testcaseId2:testcaseName2})

	testrunNameNew=testrunName + " - Changed Run Name"
	cc().fillDataForTestRun(self,sel,summary=testrunNameNew,product=env.product2)
	cc().clickActionInCloneTestRun(self,sel,"Save")
	cc().verifyTestRunPageIsReady(self,sel,testrunNameNew,summary=testrunNameNew,product=env.product2,\
		testcaseIds=[testcaseId1],notestcaseIds=[testcaseId2])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
