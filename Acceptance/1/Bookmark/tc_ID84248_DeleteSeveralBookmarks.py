from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class DeleteSeveralBookmarks(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_DeleteSeveralBookmarks(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#(1)Delete Several Bookmarks
	cc().openTestRun(self,sel,env.testrunName)
	cc().addBookmark(self,sel,bookmarkName=env.testrunName)
	cc().openTestRun(self,sel,env.testrunName2)
	cc().addBookmark(self,sel,bookmarkName=env.testrunName2)

	cc().openBookmarksPage(self,sel)
	cc().deleteBookmarks(self,sel,[env.testrunName,env.testrunName2],delete=True)

	#(2)Cancel to Delete Several Bookmarks
	cc().openTestRun(self,sel,env.testrunName)
	cc().addBookmark(self,sel,bookmarkName=env.testrunName)
	cc().openTestRun(self,sel,env.testrunName2)
	cc().addBookmark(self,sel,bookmarkName=env.testrunName2)

	cc().openBookmarksPage(self,sel)
	cc().deleteBookmarks(self,sel,[env.testrunName,env.testrunName2],delete=False)

	#Clear up the bookmarks data
	cc().deleteBookmarks(self,sel,[env.testrunName,env.testrunName2],delete=True)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
