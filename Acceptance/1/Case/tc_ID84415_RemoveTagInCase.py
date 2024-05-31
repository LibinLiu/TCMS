from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class RemoveTagInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveTagInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	#Add a tag
	tagName = "aa@@aa11"
	cc().addTagInCase(self,sel,tagName)

	#Remove the added tag
	cc().removeTagInCase(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
