from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ExportNonePlanInSearchPlanResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ExportNonePlanInSearchPlanResult(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Search test plan by some options
	cc().searchTestPlan(self,sel,planName=env.testplanName,author=env.user,planType=env.plantype11,\
		testplanIdNames={env.testplanId:env.testplanName})

	#Click the Export button
	cc().selectTestPlanInSearchPlan(self,sel,testplanIds="")
	cc().clickActionInSearchPlan(self,sel,"Export")
	cc().verifyExportPlanWarningPageIsReady(self,sel)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
