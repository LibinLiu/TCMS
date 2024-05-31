from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class RemoveBugInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveBugInCase(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	
	#Add a bug
	cc().addBugInCase(self,sel,env.bugno,env.bugurl)

	#Remove the added bug
	cc().removeBugInCase(self,sel,env.testcaseId,env.bugno,env.bugurl)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
