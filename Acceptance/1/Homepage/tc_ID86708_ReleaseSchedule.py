from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ReleaseSchedule(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_ReleaseSchedule(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().clickActionLinkInHomePage(self,sel,"Release schedule")
	cc().verifyReleaseSchedulePageIsReady(self,sel)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
