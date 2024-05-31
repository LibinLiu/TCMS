from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class AddProdVerWithOtherProdFromCreateRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddProdVerWithOtherProdFromCreateRun(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,caseSummary=env.testcaseName41,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41},\
		testcaseResultNoIdNames={env.testcaseId42:env.testcaseName42})

	rdmNum1=random.uniform(1, 10000)
	prodversionStr="Auto"+(str(rdmNum1))

	cc().clickActionInCreateRun(self,sel,"Add Product Version")
	cc().verifyAddProductVersionPageIsReady(self,sel,prodverPageId="product_version")

	#save the new product version
	cc().fillDataForAddProductVersionPage(self,sel,prodversion=prodversionStr,product=env.product2)

	cc().clickActionInAddProductVersionPage(self,sel,"Save")
	cc().verifyCreateTestRunPageIsReady(self,sel,prodversion=prodversionStr)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
