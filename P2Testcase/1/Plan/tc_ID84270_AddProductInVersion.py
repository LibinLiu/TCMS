from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class AddProductInVersion(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddProductInVersion(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	cc().clickMenu(self,sel,"PLANNING","New Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)

	rdmNum1=random.uniform(1, 10000)
	prodversionStr="Auto"+(str(rdmNum1))

	rdmNum2=random.uniform(1, 10000)
	productName="Auto"+(str(rdmNum2))

        descriptionStr="Just for auto test."

	cc().clickActionInCreateTestPlan(self,sel,"Add Product Version")
	cc().verifyAddProductVersionPageIsReady(self,sel)

	#Add and save a new Product
	cc().clickActionInAddProductVersionPage(self,sel,"Add Product")
	cc().verifyAddProductPageIsReady(self,sel)

	cc().fillDataForAddProductPage(self,sel,product=productName,classification=env.classification1,\
		description=descriptionStr)

	cc().clickActionInAddProductPage(self,sel,"Save")
	cc().verifyAddProductVersionPageIsReady(self,sel,product=productName)

	#save the new product version
	cc().fillDataForAddProductVersionPage(self,sel,prodversion=prodversionStr)

	cc().clickActionInAddProductVersionPage(self,sel,"Save")
	cc().verifyCreateTestPlanPageIsReady(self,sel,prodversion=prodversionStr)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
