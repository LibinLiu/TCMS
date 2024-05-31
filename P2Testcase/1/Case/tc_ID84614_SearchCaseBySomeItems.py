from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseBySomeItems(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseBySomeItems(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Search test case by some items
	cc().searchTestCase(self,sel,summary=env.testcaseName,author=env.useremail,\
		plan=env.testplanName,product=env.product1,automated="Auto",\
		category=env.category11,autoproposed="off",priority=[1,2,3],status=[1,2],\
		testcaseIdNames={env.testcaseId:env.testcaseName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
