from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class EditRemovePropertyInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_EditRemovePropertyInRun(self):
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
	testrunId = cc().createTestRunFromPlan(self,sel,testplanName,testrunName)

	#(2)Execute test
	cc().openTestRunFromPlan(self,sel,testplanName,testrunId,testrunName)
	cc().addPropertyInRun(self,sel,env.runproperty1,env.runpropvalue11,needRemove=False)

	cc().editPropertyInRun(self,sel,env.runproperty1,env.runpropvalue11,env.runpropvalue12,needRemove=True)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
