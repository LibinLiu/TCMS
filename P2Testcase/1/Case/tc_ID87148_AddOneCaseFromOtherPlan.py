from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddOneCaseFromOtherPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddOneCaseFromOtherPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Add the case of env.testplanName to env.testplanName2
	cc().addCasesToPlanFromOtherPlan(self,sel,env.testplanName2,{env.testcaseId:env.testcaseName},\
		product="---------",plan=env.testplanId)

	#Remove just added test case
	cc().removeTestCasesInPlan(self,sel,{env.testcaseId:env.testcaseName})
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
