from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class CloneSingleRunWithCancelBtn(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneSingleRunWithCancelBtn(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data
	cc().openTestRun(self,sel,env.testrunName)

	#Execute test
	cc().selectCaseInRun(self,sel,"All")
	cc().clickActionInRun(self,sel,"Clone")
	cc().verifyCloneTestRunPageIsReady(self,sel,env.testrunName)

	cc().fillDataForTestRun(self,sel,summary="aaaaaaxxxxxxxx",product=env.product2,prodversion=env.prodversion2,build=env.build2)
	cc().clickActionInCloneTestRun(self,sel,"Cancel")
	cc().verifyTestRunPageIsReady(self,sel,env.testrunName,product=env.product1,prodversion=env.prodversion11,build=env.build11)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
