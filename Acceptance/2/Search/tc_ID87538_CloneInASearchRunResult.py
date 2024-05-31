from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class CloneInASearchRunResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneInASearchRunResult(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	absPath = os.path.abspath(__file__)

	rdm=random.uniform(1, 1000)
	testrunNameSuffix="["+str(rdm)+"]"

	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId=cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	testrunName1=cc().getFormatName(self,sel,absPath,"testrunName")+testrunNameSuffix
	testrunId1=cc().createTestRunFromPlan(self,sel,testplanName,testrunName1)

	testrunName2=cc().getFormatName(self,sel,absPath,"testrunName")+testrunNameSuffix
	testrunId2=cc().createTestRunFromPlan(self,sel,testplanName,testrunName2)

	testrunName3=cc().getFormatName(self,sel,absPath,"testrunName")+testrunNameSuffix
	testrunId3=cc().createTestRunFromPlan(self,sel,testplanName,testrunName3)

	#--(B) Execute test
	#(1)Clone - not select any test run
	cc().searchRunByRunOptInASearch(self,sel,summary=testrunNameSuffix,\
		resultIdNames={testrunId1:testrunName1,testrunId2:testrunName2,testrunId3:testrunName3})

	cc().clickActionInASearchRunResult(self,sel,"Clone")
	cc().verifyCloneWarningPage(self,sel,"Run")

	#(2)Clone - select 1 test run
	cc().searchRunByRunOptInASearch(self,sel,summary=testrunNameSuffix,\
		resultIdNames={testrunId1:testrunName1,testrunId2:testrunName2,testrunId3:testrunName3})
	cc().selectRunInASearchRunResult(self,sel,[testrunId1])

	cc().clickActionInASearchRunResult(self,sel,"Clone")
        cc().verifyCloneTestRunPageIsReady(self,sel,testrunName1)

	#(3)Clone - select 2 test runs
	cc().searchRunByRunOptInASearch(self,sel,summary=testrunNameSuffix,\
		resultIdNames={testrunId1:testrunName1,testrunId2:testrunName2,testrunId3:testrunName3})
	cc().selectRunInASearchRunResult(self,sel,[testrunId1,testrunId2])

	cc().clickActionInASearchRunResult(self,sel,"Clone")
	cc().verifyCloneMultiTestRunPageIsReady(self,sel,{testrunId1:testrunName1,testrunId2:testrunName2})

	#(4)Clone - select all test runs
	cc().searchRunByRunOptInASearch(self,sel,summary=testrunNameSuffix,\
		resultIdNames={testrunId1:testrunName1,testrunId2:testrunName2,testrunId3:testrunName3})
	cc().selectRunInASearchRunResult(self,sel,"All")

	cc().clickActionInASearchRunResult(self,sel,"Clone")
        cc().verifyCloneMultiTestRunPageIsReady(self,sel,{testrunId1:testrunName1,testrunId2:testrunName2,testrunId3:testrunName3})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
