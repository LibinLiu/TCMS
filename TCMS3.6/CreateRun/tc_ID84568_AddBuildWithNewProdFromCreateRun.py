from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class AddBuildWithNewProdFromCreateRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddBuildWithNewProdFromCreateRun(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,caseSummary=env.testcaseName41,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41},\
		testcaseResultNoIdNames={env.testcaseId42:env.testcaseName42})

	rdmNum=random.uniform(1, 10000)
	buildName="Auto"+(str(rdmNum))
        buildDescriptionStr="Just for auto test of build."

	rdmNum=random.uniform(1, 10000)
	productName="Auto"+(str(rdmNum))
        productDescriptionStr="Just for auto test of product."

	cc().clickActionInCreateRun(self,sel,"Add Build")
	cc().verifyAddBuildPageIsReady(self,sel)

	cc().fillDataForAddBuildPage(self,sel,build=buildName,description=buildDescriptionStr)

	cc().clickActionInAddBuildPage(self,sel,"Add Product")
	cc().verifyAddProductPageIsReady(self,sel)

	cc().fillDataForAddProductPage(self,sel,product=productName,\
		classification=env.classification1,description=productDescriptionStr)
	cc().clickActionInAddProductPage(self,sel,"Save")
	cc().verifyAddBuildPageIsReady(self,sel,build=buildName,product=productName,description=buildDescriptionStr)

	cc().clickActionInAddBuildPage(self,sel,"Save")
	cc().verifyCreateTestRunPageIsReady(self,sel,build=buildName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
