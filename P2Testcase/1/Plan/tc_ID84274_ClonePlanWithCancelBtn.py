from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClonePlanWithCancelBtn(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClonePlanWithCancelBtn(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)
	
	cc().searchTestPlan(self,sel,planName=env.testplanName,testplanIdNames={env.testplanId:env.testplanName})

	cc().selectTestPlanInSearchPlan(self,sel,[env.testplanId])
	cc().clickActionInSearchPlan(self,sel,"Clone")
	cc().verifyCloneTestPlanPageIsReady(self,sel,env.testplanName)

	cc().clickActionInCloneTestPlan(self,sel,"Cancel")
	cc().verifySearchPlanPageIsReady(self,sel,planName=env.testplanName,testplanIdNames={env.testplanId:env.testplanName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
