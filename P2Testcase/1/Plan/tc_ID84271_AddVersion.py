from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class AddVersion(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddVersion(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().clickMenu(self,sel,"PLANNING","New Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)

	rdmNum1=random.uniform(1, 10000)
	prodversionStr="Auto"+(str(rdmNum1))

	cc().clickActionInCreateTestPlan(self,sel,"Add Product Version")
	cc().verifyAddProductVersionPageIsReady(self,sel)

	cc().fillDataForAddProductVersionPage(self,sel,prodversion=prodversionStr,product=env.product1)
	cc().clickActionInAddProductVersionPage(self,sel,"Save")

	cc().verifyCreateTestPlanPageIsReady(self,sel,prodversion=prodversionStr)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
