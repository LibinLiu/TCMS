from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchPlanByTag(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchPlanByTag(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	rdm=random.uniform(1, 1000)
	tagName = "bb@@bb22"+str(rdm)

	#Add a new tag
	cc().openTestPlan(self,sel,env.testplanName)
	cc().addTagInPlan(self,sel,tagName,needRemove=False)

	#Search plan by tag
	cc().searchTestPlan(self,sel,tag=tagName,testplanIdNames={env.testplanId:env.testplanName})

	#Remove the new tag
	cc().openTestPlan(self,sel,env.testplanName)
	cc().removeTagInPlan(self,sel,[tagName])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
