from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class PrintCopyInASearchCaseResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_PrintCopyInASearchCaseResult(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	absPath = os.path.abspath(__file__)

	rdm=random.uniform(1, 1000)
	testcaseNameSuffix="["+str(rdm)+"]"

	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId=cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")+testcaseNameSuffix
	testcaseId1=cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	testcaseName2=cc().getFormatName(self,sel,absPath,"testcaseName")+testcaseNameSuffix
	testcaseId2=cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName2)

	testcaseName3=cc().getFormatName(self,sel,absPath,"testcaseName")+testcaseNameSuffix
	testcaseId3=cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName3)

	#--(B) Execute test
	#(1)Print copy - not select any test case
	cc().searchCaseByCaseOptInASearch(self,sel,summary=testcaseNameSuffix,\
		resultIdNames={testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})

	cc().clickActionInASearchCaseResult(self,sel,"Printable copy")
	cc().verifyPrintNoTestCaseWarningFromSearchPageIsReady(self,sel)

	#(2)Print copy - select a test case
	cc().searchCaseByCaseOptInASearch(self,sel,summary=testcaseNameSuffix,\
		resultIdNames={testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})
	cc().selectCaseInASearchCaseResult(self,sel,[testcaseId1])

	cc().clickActionInASearchCaseResult(self,sel,"Printable copy")
	cc().verifyPrintTestCasePageIsReady(self,sel,{testcaseId1:testcaseName1})

	#(3)Print copy - select 2 test cases
	cc().openHomePage(self,sel)
	cc().searchCaseByCaseOptInASearch(self,sel,summary=testcaseNameSuffix,\
		resultIdNames={testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})
	cc().selectCaseInASearchCaseResult(self,sel,[testcaseId1,testcaseId2])

	cc().clickActionInASearchCaseResult(self,sel,"Printable copy")
	cc().verifyPrintTestCasePageIsReady(self,sel,{testcaseId1:testcaseName1,testcaseId2:testcaseName2})

	#(4)Print copy - select all test cases
	cc().openHomePage(self,sel)
	cc().searchCaseByCaseOptInASearch(self,sel,summary=testcaseNameSuffix,\
		resultIdNames={testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})
	cc().selectCaseInASearchCaseResult(self,sel,"All")

	cc().clickActionInASearchCaseResult(self,sel,"Printable copy")
	cc().verifyPrintTestCasePageIsReady(self,sel,{testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
