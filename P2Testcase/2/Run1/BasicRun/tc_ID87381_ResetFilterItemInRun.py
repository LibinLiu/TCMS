from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class ResetFilterItemInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ResetFilterItemInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Open Test Run From Plan
	cc().openTestRun(self,sel,env.testrunName)

	cc().clickActionInRun(self,sel,"Show filter options")

	#verify the test run filter item info is showing setting by default
	cc().verifyFilterItemDataInRun(self,sel,summary="",defaulttester="",assignee="",\
				bugno="",status="--------",priority="--------")

	#Fill the data for a new test run form with provided data.
	cc().fillDataForFilterItemInRun(self,sel,summary="xxx",defaulttester="aaa",assignee="bbb",\
				bugno="ccc",status="PASSED",priority="P2")
	cc().clickActionInRun(self,sel,"Reset")

	#verify the test run filter item info is not changed
	cc().verifyFilterItemDataInRun(self,sel,summary="",defaulttester="",assignee="",\
				bugno="",status="--------",priority="--------")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
