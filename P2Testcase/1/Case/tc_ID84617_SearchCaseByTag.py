from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseByTag(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseByTag(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Add a tag in test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	rdm=random.uniform(1, 1000)
	tagName = "aa@@aa11"+str(rdm)
	cc().addTagInCase(self,sel,tagName)

	#Search test case by tag
	cc().searchTestCase(self,sel,tag=tagName,testcaseIdNames={env.testcaseId:env.testcaseName})

	#Remove the added tag
	cc().clickLink(self,sel,env.testcaseName)
	cc().removeTagInCase(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
