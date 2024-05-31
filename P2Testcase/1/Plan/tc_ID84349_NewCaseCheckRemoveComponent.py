from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class NewCaseCheckRemoveComponent(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_NewCaseCheckRemoveComponent(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)
	cc().addComponentInPlan(self,sel,[env.component12,env.component13])

	cc().openHomePage(self,sel)
	cc().openTestPlan(self,sel,env.testplanName)
	cc().removeComponentInPlan(self,sel,{env.componentId12:env.component12})

	cc().clickCaseActionInPlan(self,sel,"Write new case")
	cc().verifyCreateTestCasePageIsReady(self,sel,chosenComponentIdNames={env.componentId13:env.component13},\
		notChosenComponentIdNames={env.componentId12:env.component12})

	cc().openTestPlan(self,sel,env.testplanName)
	cc().removeComponentInPlan(self,sel,{env.componentId13:env.component13})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
