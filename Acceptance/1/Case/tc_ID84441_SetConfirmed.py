from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class SetConfirmed(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SetConfirmed(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)
	cc().changeCaseStatusInPlan(self,sel,"PROPOSED")

	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Reviewing Cases")

	cc().changeReviewCaseStatusInPlan(self,sel,"CONFIRMED")

	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Cases")
	cc().verifyLink(self,sel,env.testcaseId)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
