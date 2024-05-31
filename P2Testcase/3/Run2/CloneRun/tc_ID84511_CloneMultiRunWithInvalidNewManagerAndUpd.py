from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class CloneMultiRunWithInvalidNewManagerAndUpd(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneMultiRunWithInvalidNewManagerAndUpd(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	testplanName=env.testplanName4
	testrunId1=env.testrunId4
	testrunName1=env.testrunName4
	testrunId2=env.testrunId42
	testrunName2=env.testrunName42

	cc().openTestPlan(self,sel,testplanName)

	#(2)Execute test
	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Runs")
	cc().selectTestRunsInPlan(self,sel,[testrunId1,testrunId2])
	cc().clickOtherActionInPlan(self,sel,"Run_Clone")
	cc().verifyCloneMultiTestRunPageIsReady(self,sel,{testrunId1:testrunName1,testrunId2:testrunName2})

	invalidManager="aabb"+env.user
	cc().fillDataForCloneMultiTestRun(self,sel,testrunIdOnoffs={testrunId1:"on",testrunId2:"on"},product=env.product1,\
		prodversion=env.prodversion12,build=env.build12,runmanager=invalidManager,updatemanager="on")
	cc().clickActionInCloneMultiTestRun(self,sel,"Clone")

	cc().verifyCloneMultiTestRunPageIsReady(self,sel,{testrunId1:testrunName1,testrunId2:testrunName2})
	cc().verifyErrWarningMsgInCloneMultiTestRun(self,sel,"Invalid Run Manager",wrongUser=invalidManager)	

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
