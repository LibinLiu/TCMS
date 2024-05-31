from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class ClickBugURL(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClickBugURL(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	
	#Add a bug url
	cc().addBugInCase(self,sel,env.bugno,env.bugurl)

	#Click bug url to open the bug
        cc().clickLinkAndWait(self,sel,env.bugurl)
	cc().verifyBugPageIsReady(self,sel,env.bugno)

	#Remove the bug url
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	cc().removeBugInCase(self,sel,env.testcaseId,env.bugno,env.bugurl)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
