from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ClearAllCompForNewCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ClearAllCompForNewCase(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	absPath = os.path.abspath(__file__)
	testcaseName=cc().getFormatName(self,sel,absPath,"testcaseName")

	cc().clickCaseActionInPlan(self,sel,"Write new case")
	cc().verifyCreateTestCasePageIsReady(self,sel)

	#Fill the data for a new test case form with provided data.
	cc().fillDataForTestCase(self,sel,summary=testcaseName,product=env.product1,category=env.category11)

	cc().addComponentInCreateCase(self,sel,"All",wayToAdd="Choose all")

	cc().removeComponentInCreateCase(self,sel,"All",wayToRemove="Clear all")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
