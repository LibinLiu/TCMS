from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class EditDefaultTesterInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_EditDefaultTesterInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#open Test Run From Plan
	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)

	cc().editTestRun(self,sel,env.testrunName,defaulttester="")
	cc().editTestRun(self,sel,env.testrunName,defaulttester=env.useremail)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
