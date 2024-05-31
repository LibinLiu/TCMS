from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class InputAddress(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_InputAddress(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().editBasicinfo(self,sel,address="No.33 Fucheng Road")

	#Clear off the data
	cc().editBasicinfo(self,sel,address="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
