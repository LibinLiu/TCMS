from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CreateNewCaseByTestingMenu(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreateNewCaseByTestingMenu(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	absPath = os.path.abspath(__file__)
	testcaseName=cc().getFormatName(self,sel,absPath,"testcaseName")

	cc().clickMenu(self,sel,"TESTING","New Case")
	cc().verifyCreateTestCasePageIsReady(self,sel)

	cc().fillDataForTestCase(self,sel,summary=testcaseName,product=env.product1,component=[env.component11],\
		category=env.category11,manual="off",auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")

	cc().clickActionInCreateCase(self,sel,"Save")
	cc().verifyTestCasePageIsReady(self,sel,testcaseName)


    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
