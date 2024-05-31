from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class EditEstTimeInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_EditEstTimeInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#open Test Run From Plan
	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)

	#Change some test run info
	cc().editTestRun(self,sel,env.testrunName,estdays="1",esthours="2",estmins="3",estsecs="10")

	#Restore the test run info
	cc().editTestRun(self,sel,env.testrunName,estdays="0",esthours="0",estmins="0",estsecs="0")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
