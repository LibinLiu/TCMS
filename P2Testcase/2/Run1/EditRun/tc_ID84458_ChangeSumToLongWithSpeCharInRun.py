#coding=utf-8
from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class ChangeSumToLongWithSpeCharInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ChangeSumToLongWithSpeCharInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#open Test Run From Plan
	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)

	#Change the run summary
	runNameNew="测试abcdefghijklmopqrstuvwxyz#12345678!90~!@#$%^&*()_+测试测试abcdefghijklmopqrstuvwxyz#12345678!90~!@#$%^&*()_+测试测试abcdefghijklmopqrstuvwxyz#12345678!90~!@#$%^&*()_+测试".decode('utf-8')
	cc().editTestRun(self,sel,env.testrunName,summary=runNameNew)

	#Restore the run summary
	cc().editTestRun(self,sel,runNameNew,summary=env.testrunName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
