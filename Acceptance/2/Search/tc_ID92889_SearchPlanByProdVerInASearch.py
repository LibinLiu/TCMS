from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SearchPlanByProdVerInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchPlanByProdVerInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#search via product & 'wrong prodversion' & caseid
	cc().searchPlanByPlanOptInASearch(self,sel,productList=[env.product1],\
		prodversionList=[env.prodversion12],planId=env.testplanId,resultIdNames="")

	#search via product & 'right prodversion' & caseid
	cc().searchPlanByPlanOptInASearch(self,sel,productList=[env.product1],\
		prodversionList=[env.prodversion11],planId=env.testplanId,resultIdNames={env.testplanId:env.testplanName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
