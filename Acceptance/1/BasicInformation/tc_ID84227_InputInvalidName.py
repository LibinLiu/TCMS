from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class InputInvalidName(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_InputInvalidName(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().editBasicinfo(self,sel,firstName="FFFFFFFFFFFFFFFFFFFFFFFFFFFFFX",lastName="LLLLLLLLLLLLLLLLLLLLLLLLLLLLLX")

	#Clear off the data
	cc().editBasicinfo(self,sel,firstName="",lastName="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
