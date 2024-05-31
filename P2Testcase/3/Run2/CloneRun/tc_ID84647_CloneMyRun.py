from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class CloneMyRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneMyRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	testrunName1=cc().getFormatName(self,sel,absPath,"testrunName")
	testrunId1 = cc().createTestRunFromPlan(self,sel,testplanName,testrunName1)

	testrunName2=cc().getFormatName(self,sel,absPath,"testrunName")
	testrunId2 = cc().createTestRunFromPlan(self,sel,testplanName,testrunName2)

	cc().openSearchMyRunPage(self,sel)

	#(2)Execute test
	cc().selectTestRunsInSearchRun(self,sel,[testrunId1,testrunId2])
	cc().clickActionInSearchRun(self,sel,"Clone")
	cc().verifyCloneMultiTestRunPageIsReady(self,sel,{testrunId1:testrunName1,testrunId2:testrunName2})

	cc().fillDataForCloneMultiTestRun(self,sel,testrunIdOnoffs={testrunId1:"on",testrunId2:"on"},product=env.product1,prodversion=env.prodversion12,build=env.build12)
	cc().clickActionInCloneMultiTestRun(self,sel,"Clone")
	
	cc().verifySearchRunPageIsReady(self,sel,product=env.product1,prodversion=env.prodversion12,build=env.build12)
	cc().verifyLink(self,sel,testrunName1)
	cc().verifyLink(self,sel,testrunName2)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
