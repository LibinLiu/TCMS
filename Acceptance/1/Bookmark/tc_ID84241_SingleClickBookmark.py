from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SingleClickBookmark(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_SingleClickBookmark(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestRun(self,sel,env.testrunName)
	cc().addBookmark(self,sel,bookmarkName=env.testrunName)

	cc().openBookmarksPage(self,sel)

	cc().clickLink(self,sel,env.testrunName)
	cc().verifyTestRunPageIsReady(self,sel,env.testrunName)

	cc().openBookmarksPage(self,sel)
	cc().deleteBookmarks(self,sel,[env.testrunName])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
