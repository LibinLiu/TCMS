from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseByAllItems(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseByAllItems(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Add a bug in test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().addBugInCase(self,sel,env.bugno,env.bugurl)

	#Add a tag
	tagName = "aa@@aa11"
	cc().addTagInCase(self,sel,tagName)

	#Search test case by all items
	cc().searchTestCase(self,sel,summary=env.testcaseName,author=env.useremail,\
		plan=env.testplanName,bugID=env.bugno,tag=tagName,product=env.product1,automated="Auto",\
		category=env.category11,component=env.component11,autoproposed="off",priority=[1,2,3],\
		status=[1,2],testcaseIdNames={env.testcaseId:env.testcaseName})

	#Remove the added bug
	cc().clickLink(self,sel,env.testcaseName)
	cc().removeBugInCase(self,sel,env.testcaseId,env.bugno,env.bugurl)

	#Remove the added tag
	cc().removeTagInCase(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
