from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CloneCasesIntoAnotherPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneCasesIntoAnotherPlan(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName1 = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId1 = cc().createTestPlan(self,sel,testplanName1)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName1,testcaseName1)

	testcaseName2=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId2 = cc().createTestCaseFromPlan(self,sel,testplanName1,testcaseName2)

	testplanName2 = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId2 = cc().createTestPlan(self,sel,testplanName2)

	cc().openTestPlan(self,sel,testplanName1)

	#(2)Execute test
	cc().clickCaseActionInPlan(self,sel,"Clone")
	cc().verifyCloneTestCasePageIsReady(self,sel,{testcaseId1:testcaseName1,testcaseId2:testcaseName2})

	cc().saveCloneTestCase(self,sel,selectPlan="Use Filterplan",selectFilterPlanIds=[testplanId2])

	cc().verifyTestPlanPageIsReady(self,sel,testplanName2)
	cc().verifyLink(self,sel,"Cases (2/2)")
	cc().verifyLink(self,sel,testcaseName1)
	cc().verifyLink(self,sel,testcaseName2)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
