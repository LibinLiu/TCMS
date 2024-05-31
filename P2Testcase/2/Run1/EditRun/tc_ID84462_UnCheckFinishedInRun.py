from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class UnCheckFinishedInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_UnCheckFinishedInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#open Test Run From Plan
	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)

	#Check finished
	cc().editTestRun(self,sel,env.testrunName,finished="on")

	#UnCheck finished
	cc().editTestRun(self,sel,env.testrunName,finished="off")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
