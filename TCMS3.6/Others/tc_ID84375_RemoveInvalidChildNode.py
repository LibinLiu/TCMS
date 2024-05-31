from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class RemoveInvalidChildNode(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_RemoveInvalidChildNode(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	cc().addChildNode(self,sel,env.testplanId,{env.testplanId2:env.testplanName2})

	invalidtestplanId = "aa"
	cc().removeInvalidChildNode(self,sel,env.testplanId,invalidtestplanId)

	cc().removeChildNode(self,sel,env.testplanId,{env.testplanId2:env.testplanName2})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
