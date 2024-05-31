#coding=utf-8
from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchRunBySpecialSummary(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchRunBySpecialSummary(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	#Prepare test data
	cc().openTestRun(self,sel,env.testrunName)
	testrunNameNew = (env.testrunName+"测试").decode('utf-8')
	cc().editTestRun(self,sel,env.testrunName,summary=testrunNameNew)

	cc().searchTestRun(self,sel,summary=testrunNameNew,testrunIdNames={env.testrunId:testrunNameNew})

	#Restore test data
	cc().clickLink(self,sel,env.testrunId)
	cc().editTestRun(self,sel,testrunNameNew,summary=env.testrunName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
