from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class AddCasesOfOtherPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddCasesOfOtherPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Add the cases of env.testplanName4 to env.testplanName2
	cc().addCasesToPlanFromOtherPlan(self,sel,env.testplanName2,\
		{env.testcaseId41:env.testcaseName41,env.testcaseId42:env.testcaseName42},\
		product="---------",plan=env.testplanId4)

	#Remove just added test case
	cc().removeTestCasesInPlan(self,sel,{env.testcaseId41:env.testcaseName41,env.testcaseId42:env.testcaseName42})
  
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
