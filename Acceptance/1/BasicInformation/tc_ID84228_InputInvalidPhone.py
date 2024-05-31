from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class InputInvalidPhone(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_InputInvalidPhone(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openBasicinfoPage(self,sel)

	#Fill the data for the edit Basic information form with provided data.
	cc().fillDataForBasicinfoPage(self,sel,phoneNumber=env.longstring[:120])

	cc().clickActionInBasicinfo(self,sel,"Save Change")

	cc().verifyBasicInformationPageIsReady(self,sel,phoneNumber=env.longstring[:120],isSaved=True)

	#Clear off the data
	cc().editBasicinfo(self,sel,phoneNumber="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
