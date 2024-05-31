from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClickRunNumInASearchPlanResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClickRunNumInASearchPlanResult(self):
        sel = self.selenium
        sel.open(env.openurl)

	cc().verifyHomePageIsReady(self,sel)

	cc().searchPlanByPlanOptInASearch(self,sel,planId=env.testplanId,resultIdNames={env.testplanId:env.testplanName})

	cc().clickOtherActionInSearchPlanResult(self,sel,"Run Number",actionValue="1")

	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName)
	cc().verifyFirstLevelLabelOpenInPlan(self,sel,"Runs")
	cc().verifyLink(self,sel,env.testrunId)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
