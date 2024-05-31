from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class CheckCaseNumWithTagInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CheckCaseNumWithTagInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	rdm=random.uniform(1, 1000)
	tagName = "mytag@xx"+str(rdm)

	cc().openTestPlan(self,sel,env.testplanName4)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41,env.testcaseId42])
	cc().addTagForCaseInPlan(self,sel,tagName, testcaseIdNames={env.testcaseId41:env.testcaseName41, env.testcaseId42:env.testcaseName42})

	cc().addTagInPlan(self,sel,tagName,needRemove=False)
	cc().verifyTagInfoInPlan(self,sel,caseNum=2,tagName=tagName)

	#Remove the tag from case and plan
	cc().removeTagInPlan(self,sel,[tagName])

	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Cases")
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId41,env.testcaseId42])
	cc().removeTagForCaseInPlan(self,sel,tagName, testcaseIdNames={env.testcaseId41:env.testcaseName41, env.testcaseId42:env.testcaseName42})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
