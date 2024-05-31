from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CloneOneCaseInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneOneCaseInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName)

	cc().openTestCaseFromPlan(self,sel,testplanName,testcaseId,testcaseName)

	#(2)Execute test
	cc().clickActionInCase(self,sel,"Clone case")
	cc().verifyCloneTestCasePageIsReady(self,sel,{testcaseId:testcaseName})

	cc().saveCloneTestCase(self,sel,selectPlan="Use Sameplan")
	cc().verifyTestCasePageIsReady(self,sel,testcaseName)

	cc().openTestPlan(self,sel,testplanName)
	cc().verifyLink(self,sel,"Cases (2/2)")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
