from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class RemoveOneComponent(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveOneComponent(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	cc().addComponentInPlan(self,sel,[env.component12,env.component13,env.component14,env.component15])

	cc().removeComponentInPlan(self,sel,{env.componentId13:env.component13})

	cc().removeComponentInPlan(self,sel,{env.componentId12:env.component12,\
		env.componentId14:env.component14,env.componentId15:env.component15})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
