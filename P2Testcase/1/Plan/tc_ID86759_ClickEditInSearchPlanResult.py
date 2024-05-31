from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class ClickEditInSearchPlanResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClickEditInSearchPlanResult(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().searchTestPlan(self,sel,planName=env.testplanName,testplanIdNames={env.testplanId:env.testplanName})

	cc().clickEditInSearchPlanResult(self,sel,env.testplanId)
	cc().verifyEditTestPlanPageIsReady(self,sel,env.testplanName)
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
