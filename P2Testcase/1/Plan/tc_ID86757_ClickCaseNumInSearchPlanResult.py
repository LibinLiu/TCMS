from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClickCaseNumInSearchPlanResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClickCaseNumInSearchPlanResult(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().searchTestPlan(self,sel,planName=env.testplanName,author=env.user,planType=env.plantype11,\
		testplanIdNames={env.testplanId:env.testplanName})

	cc().clickOtherActionInSearchPlanResult(self,sel,"Case Number",actionValue="1")

	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName)
	cc().verifyFirstLevelLabelOpenInPlan(self,sel,"Cases")
	cc().verifyLink(self,sel,env.testcaseId)
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
