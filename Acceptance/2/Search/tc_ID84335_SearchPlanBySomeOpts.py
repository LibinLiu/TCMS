from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchPlanBySomeOpts(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchPlanBySomeOpts(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Accurate search
	cc().searchTestPlan(self,sel,planName=env.testplanName,author=env.user,planType=env.plantype11,\
		testplanIdNames={env.testplanId:env.testplanName})

	#False search
	cc().searchTestPlan(self,sel,planName=env.testplanName+"fasdlkf@#!!@$!$526",\
			author=env.user+"fasdlkf@#!!@$!$526",planType=env.plantype11,testplanIdNames="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
