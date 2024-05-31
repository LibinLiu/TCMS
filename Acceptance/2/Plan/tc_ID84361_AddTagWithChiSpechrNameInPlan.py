#coding=utf-8
from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddTagWithChiSpechrNameInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddTagWithChiSpechrNameInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	#(1) Add a new tag with chinese name
	tagName = "测试".decode('utf-8')
	cc().addTagInPlan(self,sel,tagName)

	#(2) Add a new tag with special character such as "!~<>.%&*^()"
	tagName = "!~<>.%&*^()"
	cc().addTagInPlan(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
