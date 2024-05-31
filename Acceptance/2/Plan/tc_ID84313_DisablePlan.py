from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class DisablePlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_DisablePlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	#There will be a line in the plan name when plan is disabled
	cc().clickActionInTestPlan(self,sel,"Disable Plan")
	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName,isPlanEnabled=False)

	#There will be NOT a line in the plan name when plan is enabled
	cc().clickActionInTestPlan(self,sel,"Enable Plan")
	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName,isPlanEnabled=True)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
