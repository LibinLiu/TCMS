from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class CreatePlanToAddClassification(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreatePlanToAddClassification(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().clickMenu(self,sel,"PLANNING","New Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)

	rdmNum=random.uniform(1, 10000)
	classificationName="Auto"+(str(rdmNum))
        descriptionStr="Just for auto test."

	cc().clickActionInCreateTestPlan(self,sel,"Add Product")
	cc().verifyAddProductPageIsReady(self,sel)

	cc().clickActionInAddProductPage(self,sel,"Add Classification")
	cc().verifyAddClassificationPageIsReady(self,sel)

	cc().fillDataForAddClassificationPage(self,sel,classification=classificationName,description=descriptionStr)
	cc().clickActionInAddClassificationPage(self,sel,"Save")

	cc().verifyAddProductPageIsReady(self,sel,classification=classificationName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
