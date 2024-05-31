from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreateParentNode(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_CreateParentNode(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	cc().changeParentNode(self,sel,env.testplanId,env.testplanId3,env.testplanName3)

	cc().openTestPlan(self,sel,env.testplanName3)
	cc().removeChildNode(self,sel,env.testplanId3,{env.testplanId:env.testplanName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
