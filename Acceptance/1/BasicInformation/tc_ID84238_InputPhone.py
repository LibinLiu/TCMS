from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class InputPhone(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_InputPhone(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().editBasicinfo(self,sel,phoneNumber="13900000000")

	#Clear off the data
	cc().editBasicinfo(self,sel,phoneNumber="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
