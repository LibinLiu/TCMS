from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ChangeCategoryForCasesInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ChangeCategoryForCasesInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#Change the test case category
	cc().openTestPlan(self,sel,env.testplanName)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId])
	cc().setCategoryForCaseInPlan(self,sel,product=env.product2,category=env.category21)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName,product=env.product2,category=env.category21)

	#Restore the test case category
	cc().openTestPlan(self,sel,env.testplanName)
	cc().selectTestCasesInPlan(self,sel,[env.testcaseId])
	cc().setCategoryForCaseInPlan(self,sel,product=env.product1,category=env.category11)

	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName,product=env.product1,category=env.category11)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
