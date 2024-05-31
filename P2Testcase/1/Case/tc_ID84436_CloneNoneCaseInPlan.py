from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CloneNoneCaseInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneNoneCaseInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	#Try to clone without none cases selected
	cc().selectTestCasesInPlan(self,sel,"")
	cc().clickCaseActionInPlan(self,sel,"Clone")
	cc().verifyCloneWarningPage(self,sel,"Case")

	cc().clickContinueInCloneWarningPage(self,sel)
	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
