from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddTagsByMultiTimesInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddTagsByMultiTimesInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	tagName = ["mytag1@xx","mytag2@xx","mytag3@xx","mytag4@xx"]

	#Add Several Tags by multiple times
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	for i in range(len(tagName)):
		cc().addTagInCase(self,sel,tagName[i])

	sel.refresh()
	time.sleep(env.t)
	for i in range(len(tagName)):
		cc().verifyText(self,sel,tagName[i])

	#Remove Several Tags by multiple times
	for i in range(len(tagName)):
		cc().removeTagInCase(self,sel,tagName[i])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
