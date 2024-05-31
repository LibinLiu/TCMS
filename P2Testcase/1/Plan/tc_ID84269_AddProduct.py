from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class AddProduct(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddProduct(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().clickMenu(self,sel,"PLANNING","New Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)

	rdmNum=random.uniform(1, 10000)
	productName="Auto"+(str(rdmNum))
        descriptionStr="Just for auto test."

	cc().clickActionInCreateTestPlan(self,sel,"Add Product")
	cc().verifyAddProductPageIsReady(self,sel)

	cc().fillDataForAddProductPage(self,sel,product=productName,\
		classification=env.classification1,description=descriptionStr)
	cc().clickActionInAddProductPage(self,sel,"Save")

	cc().verifyCreateTestPlanPageIsReady(self,sel,product=productName)
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
