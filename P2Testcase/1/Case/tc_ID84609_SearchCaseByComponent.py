from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseByComponent(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseByComponent(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().openSearchCasePage(self,sel)

	#Verify you can't see any component without choosing a product.
	cc().verifySearchCasePageIsReady(self,sel,componentAll="---------")

	#Search test case by component
	cc().searchTestCase(self,sel,summary=env.testcaseName,product=env.product1,\
		component=env.component11,testcaseIdNames={env.testcaseId:env.testcaseName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
