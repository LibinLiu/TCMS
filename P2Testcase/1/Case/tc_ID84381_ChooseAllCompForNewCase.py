from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ChooseAllCompForNewCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ChooseAllCompForNewCase(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName=cc().getFormatName(self,sel,absPath,"testcaseName")

	#(2)Execute test
	cc().clickCaseActionInPlan(self,sel,"Write new case")
	cc().verifyCreateTestCasePageIsReady(self,sel)

	#Fill the data for a new test case form with provided data.
	cc().fillDataForTestCase(self,sel,summary=testcaseName,product=env.product1,category=env.category11,manual="off",\
		auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")

	cc().addComponentInCreateCase(self,sel,"All",wayToAdd="Choose all")

	#save the test case
	cc().clickActionInCreateCase(self,sel,"Save")
	cc().verifyTestCasePageIsReady(self,sel,testcaseName,componentIdNames={env.componentId11:env.component11,env.componentId12:env.component12,\
		env.componentId13:env.component13,env.componentId14:env.component14,env.componentId15:env.component15})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
