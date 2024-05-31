from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CheckMyPlanAuthor(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CheckMyPlanAuthor(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().openSearchMyPlanPage(self,sel)
	
	cc().verifyLink(self,sel,env.user)
	cc().verifyMyPlanFromSearch(self,sel,env.testplanId)
	cc().verifyLink(self,sel,env.user)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
