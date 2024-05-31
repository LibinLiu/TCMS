from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClonePlanWithMeAsAuthor(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClonePlanWithMeAsAuthor(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)
	
	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId = cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	#(2)Execute test
	cc().searchTestPlan(self,sel,planName=testplanName,testplanIdNames={testplanId:testplanName})

	cc().selectTestPlanInSearchPlan(self,sel,[testplanId])
	cc().clickActionInSearchPlan(self,sel,"Clone")
	cc().verifyCloneTestPlanPageIsReady(self,sel,testplanName)

	cc().fillDataForCloneTestPlan(self,sel,keepOriginalAuthor="off")
	cc().clickActionInCloneTestPlan(self,sel,"Clone")
	cc().verifyTestPlanPageIsReady(self,sel,"Copy of "+testplanName,testcaseNameList=[testcaseName1])
	cc().verifyCaseAuthorInPlan(self,sel,"1",env.user)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
