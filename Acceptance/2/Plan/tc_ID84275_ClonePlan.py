from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClonePlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClonePlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	cc().clickActionInTestPlan(self,sel,"Clone Plan")
	cc().verifyCloneTestPlanPageIsReady(self,sel,testplanName)

	cc().clickActionInCloneTestPlan(self,sel,"Clone")
	cc().verifyTestPlanPageIsReady(self,sel,"Copy of "+testplanName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
