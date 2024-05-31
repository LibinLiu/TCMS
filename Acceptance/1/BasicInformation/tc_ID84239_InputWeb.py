from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class InputWeb(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_InputWeb(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#Input your web link to 'Web'
	cc().editBasicinfo(self,sel,webURL="http://www.baidu.com")

	#Clear off the data
	cc().editBasicinfo(self,sel,webURL="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
