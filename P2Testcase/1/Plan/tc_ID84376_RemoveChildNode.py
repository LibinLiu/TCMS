from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class RemoveChildNode(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveChildNode(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	cc().addChildNode(self,sel,env.testplanId,{env.testplanId2:env.testplanName2})

	cc().removeChildNode(self,sel,env.testplanId,{env.testplanId2:env.testplanName2})
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
