from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class AddExistProduct(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddExistProduct(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().clickMenu(self,sel,"PLANNING","New Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)

        descriptionStr="Just for auto test."

	cc().clickActionInCreateTestPlan(self,sel,"Add Product")
	cc().verifyAddProductPageIsReady(self,sel)

	cc().fillDataForAddProductPage(self,sel,product=env.product1,\
		classification=env.classification1,description=descriptionStr)
	cc().clickActionInAddProductPage(self,sel,"Save")

	cc().verifyErrWarningMsgInAddProductPage(self,sel,"Existing Product")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
