from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class PrintCopyInASearchPlanResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_PrintCopyInASearchPlanResult(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	absPath = os.path.abspath(__file__)

	rdm=random.uniform(1, 1000)
	testplanNameSuffix="["+str(rdm)+"]"

	testplanName1 = cc().getFormatName(self,sel,absPath,"testplanName")+testplanNameSuffix
	testplanId1=cc().createTestPlan(self,sel,testplanName1)

	testplanName2 = cc().getFormatName(self,sel,absPath,"testplanName")+testplanNameSuffix
	testplanId2=cc().createTestPlan(self,sel,testplanName2)

	testplanName3 = cc().getFormatName(self,sel,absPath,"testplanName")+testplanNameSuffix
	testplanId3=cc().createTestPlan(self,sel,testplanName3)

	#--(B) Execute test
	#(1)Print copy - not select any test plan
	cc().searchPlanByPlanOptInASearch(self,sel,summary=testplanNameSuffix,\
		resultIdNames={testplanId1:testplanName1,testplanId2:testplanName2,testplanId3:testplanName3})

	cc().clickActionInASearchPlanResult(self,sel,"Printable copy")
	cc().verifyPrintNoTestPlanWarningFromSearchPageIsReady(self,sel)

	#(2)Print copy - select a test plan
	cc().searchPlanByPlanOptInASearch(self,sel,summary=testplanNameSuffix,\
		resultIdNames={testplanId1:testplanName1,testplanId2:testplanName2,testplanId3:testplanName3})
	cc().selectPlanInASearchPlanResult(self,sel,[testplanId1])

	cc().clickActionInASearchPlanResult(self,sel,"Printable copy")
	cc().verifyPrintTestPlanPageIsReady(self,sel,{testplanId1:testplanName1})

	#(3)Print copy - select 2 test plans
	cc().openHomePage(self,sel)
	cc().searchPlanByPlanOptInASearch(self,sel,summary=testplanNameSuffix,\
		resultIdNames={testplanId1:testplanName1,testplanId2:testplanName2,testplanId3:testplanName3})
	cc().selectPlanInASearchPlanResult(self,sel,[testplanId1,testplanId2])

	cc().clickActionInASearchPlanResult(self,sel,"Printable copy")
	cc().verifyPrintTestPlanPageIsReady(self,sel,{testplanId1:testplanName1,testplanId2:testplanName2})

	#(4)Print copy - select all test plans
	cc().openHomePage(self,sel)
	cc().searchPlanByPlanOptInASearch(self,sel,summary=testplanNameSuffix,\
		resultIdNames={testplanId1:testplanName1,testplanId2:testplanName2,testplanId3:testplanName3})
	cc().selectPlanInASearchPlanResult(self,sel,"All")

	cc().clickActionInASearchPlanResult(self,sel,"Printable copy")
	cc().verifyPrintTestPlanPageIsReady(self,sel,{testplanId1:testplanName1,testplanId2:testplanName2,testplanId3:testplanName3})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
