from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class PrintCopyInSearchPlanResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_PrintCopyInSearchPlanResult(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Search test plan by some options
	cc().searchTestPlan(self,sel,planName=env.testplanName,author=env.user,planType=env.plantype11,\
		testplanIdNames={env.testplanId:env.testplanName})

	#Select a test plan and click 'Printable copy' button
	cc().selectTestPlanInSearchPlan(self,sel,[env.testplanId])

	cc().clickActionInSearchPlan(self,sel,"Printable copy")
	cc().verifyPrintTestPlanPageIsReady(self,sel,{env.testplanId:env.testplanName},\
		testcaseIdNames={env.testcaseId:env.testcaseName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
