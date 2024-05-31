from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class AddSeveralTagsToSomeCases(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddSeveralTagsToSomeCases(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	tagName1 = "mytag1@xx"
	tagName2 = "mytag2@xx"
	tagName3 = "mytag3@xx"
	tagName = tagName1+","+tagName2+","+tagName3

	#(1)Add Several Tags to 1 Case
	#Add Several Tags
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41])
	cc().addTagForCaseInPlan(self,sel,tagName, testcaseIdNames={env.testcaseId41:env.testcaseName41})

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,taglist=[tagName1,tagName2,tagName3])

	#Remove Several Tags
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41])
	cc().removeTagForCaseInPlan(self,sel,tagName, testcaseIdNames={env.testcaseId41:env.testcaseName41})

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,notaglist=[tagName1,tagName2,tagName3])

	#(2)Add Several Tags to more than 1 Cases
	#Add Several Tags
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41,env.testcaseId42])
	cc().addTagForCaseInPlan(self,sel,tagName, testcaseIdNames={env.testcaseId41:env.testcaseName41, env.testcaseId42:env.testcaseName42})

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,taglist=[tagName1,tagName2,tagName3])

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName42,taglist=[tagName1,tagName2,tagName3])

	#Remove Several Tags
	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41,env.testcaseId42])
	cc().removeTagForCaseInPlan(self,sel,tagName, testcaseIdNames={env.testcaseId41:env.testcaseName41, env.testcaseId42:env.testcaseName42})

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName41,notaglist=[tagName1,tagName2,tagName3])

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName42,notaglist=[tagName1,tagName2,tagName3])
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
