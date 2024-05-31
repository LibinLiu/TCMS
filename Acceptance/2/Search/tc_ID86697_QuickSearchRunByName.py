from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class QuickSearchRunByName(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_QuickSearchRunByName(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Accurate search
	cc().quickSearch(self,sel,"Test Run",env.testrunName)
	cc().verifySearchRunPageIsReady(self,sel,testrunIdNames={env.testrunId:env.testrunName})

	#(2)Fuzzy search
	cc().quickSearch(self,sel,"Test Run",(env.testrunName)[:8])
	cc().verifySearchRunPageIsReady(self,sel,testrunIdNames={env.testrunId:env.testrunName})

	#(3)False search
	cc().quickSearch(self,sel,"Test Run",(env.testrunName)[:8]+"88888")
	cc().verifySearchRunPageIsReady(self,sel,testrunIdNames="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
