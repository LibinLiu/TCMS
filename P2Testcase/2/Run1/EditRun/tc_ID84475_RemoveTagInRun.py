#coding=utf-8
from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class RemoveTagInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveTagInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)
	
	tagName="测试abcdefghijklmopqrstuvwxyz#12345678!90~!@#$%^&*()_+测试".decode('utf-8')
	cc().addTagInRun(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
