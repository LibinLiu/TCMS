from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class CheckRunNumWithTagInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CheckRunNumWithTagInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	rdm=random.uniform(1, 1000)
	tagName = "mytag@xx"+str(rdm)

	cc().openTestRun(self,sel,env.testrunName)
	cc().addTagInRun(self,sel,tagName,needRemove=False)

	cc().openTestPlan(self,sel,env.testplanName)

	cc().addTagInPlan(self,sel,tagName,needRemove=False)
	cc().verifyTagInfoInPlan(self,sel,runNum=1,tagName=tagName)

	#Remove the tag from plan and run
	cc().removeTagInPlan(self,sel,[tagName])

	cc().openTestRun(self,sel,env.testrunName)
	cc().removeTagInRun(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
