from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class FilterCaseByAutTagInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_FilterCaseByAutTagInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Add a tag in test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)

	rdm=random.uniform(1, 1000)
	tagName = "aa@@aa11"+str(rdm)
	cc().addTagInCase(self,sel,tagName)

	#Filter test case by author and tag in plan
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().filterCaseInPlan(self,sel,author=env.user,tag=tagName,testcaseResultIdNames={env.testcaseId41:env.testcaseName41})
	cc().verifyLinkNotPresent(self,sel,env.testcaseId42)

	#Remove the added tag
	cc().clickLink(self,sel,env.testcaseId41)
	cc().removeTagInCase(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
