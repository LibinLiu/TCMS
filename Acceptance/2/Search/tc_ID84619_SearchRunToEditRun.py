from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchRunToEditRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchRunToEditRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Search run by some search run conditions
	cc().searchTestRun(self,sel,summary=env.testrunName,product=env.product1,\
			ownertype="Manager | Tester",owner=env.user+"@redhat.com",\
			testrunIdNames={env.testrunId:env.testrunName})
	cc().clickLink(self,sel,env.testrunName)

	#Edit & change test run
	runNameNew=env.testrunName+"_aa_aa"
	cc().editTestRun(self,sel,env.testrunName,summary=runNameNew)

	#Restore test run
	cc().editTestRun(self,sel,runNameNew,summary=env.testrunName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
