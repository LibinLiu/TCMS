from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CloneAllCasesInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneAllCasesInPlan(self):
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

	cc().openTestPlan(self,sel,testplanName)

	#(2)Execute test
	cc().clickCaseActionInPlan(self,sel,"Clone")   
	cc().verifyCloneTestCasePageIsReady(self,sel,{testcaseId1:testcaseName1,testcaseId2:testcaseName2})

	cc().saveCloneTestCase(self,sel,selectPlan="Use Sameplan")
	cc().verifyTestPlanPageIsReady(self,sel,testplanName)
	cc().verifyLink(self,sel,"Cases (4/4)")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
