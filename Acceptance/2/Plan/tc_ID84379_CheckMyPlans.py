from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CheckMyPlans(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CheckMyPlans(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().openSearchMyPlanPage(self,sel)
	cc().verifyMyPlanFromSearch(self,sel,env.testplanId)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
