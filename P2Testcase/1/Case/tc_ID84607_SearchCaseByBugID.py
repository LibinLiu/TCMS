from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class SearchCaseByBugID(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseByBugID(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Add a bug in test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().addBugInCase(self,sel,env.bugno,env.bugurl)

	#Search test case by bugID
	cc().searchTestCase(self,sel,summary=env.testcaseName,bugID=env.bugno,\
		testcaseIdNames={env.testcaseId:env.testcaseName})

	#Remove the added bug
	cc().clickLink(self,sel,env.testcaseName)
	cc().removeBugInCase(self,sel,env.testcaseId,env.bugno,env.bugurl)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
