from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchRunByProdVerInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchRunByProdVerInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openAdvancedSearchPage(self,sel)
	cc().fillDataForRunItemsInASearch(self,sel,runId=env.testrunId,productList=[env.product1],prodversionList=[env.prodversion11])

	cc().clickActionInAdvancedSearch(self,sel,"Search Run")
	cc().verifyAdvancedSearchRunResultIsReady(self,sel,tIdNames={env.testrunId:env.testrunName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
