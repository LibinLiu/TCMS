from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClonePlanWithoutAttach(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClonePlanWithoutAttach(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)
	
	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId = cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	attachmentPath = os.path.abspath(__file__)
	attachmentName = os.path.basename(attachmentPath)
	cc().openTestPlan(self,sel,testplanName)
	cc().addAttachmentInPlan(self,sel,[attachmentPath])

	#(2)Execute test
	cc().searchTestPlan(self,sel,planName=testplanName,testplanIdNames={testplanId:testplanName})

	cc().selectTestPlanInSearchPlan(self,sel,[testplanId])
	cc().clickActionInSearchPlan(self,sel,"Clone")
	cc().verifyCloneTestPlanPageIsReady(self,sel,testplanName)

	cc().fillDataForCloneTestPlan(self,sel,copyPlanAttachments="off")
	cc().clickActionInCloneTestPlan(self,sel,"Clone")
	cc().verifyTestPlanPageIsReady(self,sel,"Copy of "+testplanName,attachmentNameList="",testcaseNameList=[testcaseName1])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
