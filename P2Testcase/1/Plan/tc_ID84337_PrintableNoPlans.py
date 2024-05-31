from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class PrintableNoPlans(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_PrintableNoPlans(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().searchTestPlan(self,sel,planName=env.testplanName,testplanIdNames={env.testplanId:env.testplanName})

	cc().clickActionInSearchPlan(self,sel,"Printable copy")
	cc().verifyPrintNoTestPlanWarningFromSearchPageIsReady(self,sel)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
