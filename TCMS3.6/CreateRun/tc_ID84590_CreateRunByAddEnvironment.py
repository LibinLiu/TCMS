from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreateRunByAddEnvironment(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateRunByAddEnvironment(self):
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

	cc().clickActionInCreateRun(self,sel,"Test Plan Name",ActionValue=testplanName)
	cc().verifyTestPlanPageIsReady(self,sel,testplanName,envGroup="")

	cc().editTestPlan(self,sel,testplanName,envGroup=env.envgroup1)

	cc().openCreateTestRunFromPlan(self,sel,testplanName,filterCase=False, testcaseResultIdNames={testcaseId1:testcaseName1})
	cc().verifyCreateTestRunPageIsReady(self,sel,envGroup=env.envgroup1,envGPPropOnoffs={env.envgpproperty11:'on'})

	cc().fillDataForTestRun(self,sel,summary=testrunName,envGPPropOnoffs={env.envgpproperty11:'on'},\
		envGPPropValues={env.envgpproperty11:env.envgppropvalue112})

	cc().clickActionInCreateRun(self,sel,"Save")
	cc().verifyTestRunPageIsReady(self,sel,testrunName,envGPPropOnoffs={env.envgpproperty11:'on'},\
		envGPPropValues={env.envgpproperty11:env.envgppropvalue112})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
