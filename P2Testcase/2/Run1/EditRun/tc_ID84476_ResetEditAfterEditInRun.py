from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class ResetEditAfterEditInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ResetEditAfterEditInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#open Test Run From Plan
	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName)

	cc().clickActionInRun(self,sel,"Edit")
	cc().verifyEditTestRunPageIsReady(self,sel,env.testrunName)

	#Fill the data for a new test run form with provided data.
	runNameNew="Changed "+env.testrunName
	cc().fillDataForTestRun(self,sel,summary=runNameNew,product=env.product2,notes=env.longstring,finished="on")
	cc().clickActionInEditRun(self,sel,"Reset")

	#verify the test run info is not changed
	cc().verifyEditTestRunPageIsReady(self,sel,env.testrunName,summary=env.testrunName,product=env.product1,notes="",finished="off")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
