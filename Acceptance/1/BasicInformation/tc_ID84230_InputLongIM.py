from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class InputLongIM(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_InputLongIM(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openBasicinfoPage(self,sel)

	#Fill the data for the edit Basic information form with provided data.
	cc().fillDataForBasicinfoPage(self,sel,IMType="IRC",IMValue=env.longstring)

	cc().clickActionInBasicinfo(self,sel,"Save Change")

	cc().verifyBasicInformationPageIsReady(self,sel,IMType="IRC",IMValue=env.longstring[:128],isSaved=True)

	#Clear off the data
	cc().editBasicinfo(self,sel,IMType="IRC",IMValue="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
