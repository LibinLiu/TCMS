from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreateNewCaseAndBack(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateNewCaseAndBack(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)
	
	cc().clickCaseActionInPlan(self,sel,"Write new case")
	cc().verifyCreateTestCasePageIsReady(self,sel)

	absPath = os.path.abspath(__file__)
	testcaseName=cc().getFormatName(self,sel,absPath,"testcaseName")
	cc().fillDataForTestCase(self,sel,summary=testcaseName,product=env.product1,component=[env.component11],\
		category=env.category11,manual="off",auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")

	cc().clickActionInCreateCase(self,sel,"Cancel")

	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName)
	cc().verifyLinkNotPresent(self,sel,testcaseName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
