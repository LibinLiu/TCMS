from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class QuickSearchRunById(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_QuickSearchRunById(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Accurate search
	cc().quickSearch(self,sel,"Test Run",env.testrunId)
	cc().verifyTestRunPageIsReady(self,sel,env.testrunName)

	#(2)Fuzzy search
	''' -- remove this part due to fuzzy search by auto is not accurate now
	cc().quickSearch(self,sel,"Test Run",(env.testrunId)[:4])
	cc().verifySearchRunPageIsReady(self,sel,testrunIdNames={env.testrunId:env.testrunName})
	'''

	#(3)False search
	cc().quickSearch(self,sel,"Test Run",(env.testrunId)[:4]+"88888")
	cc().verifySearchRunPageIsReady(self,sel,testrunIdNames="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
