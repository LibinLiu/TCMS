from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreatePlanInASearchPlanResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreatePlanInASearchPlanResult(self):
        sel = self.selenium
        sel.open(env.openurl)

	cc().verifyHomePageIsReady(self,sel)

	cc().searchPlanByPlanOptInASearch(self,sel,planId=env.testplanId,resultIdNames={env.testplanId:env.testplanName})

	cc().clickActionInASearchPlanResult(self,sel,"New Test Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)


    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
