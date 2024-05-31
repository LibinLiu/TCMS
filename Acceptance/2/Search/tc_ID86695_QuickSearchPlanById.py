from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class QuickSearchPlanById(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_QuickSearchPlanById(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Accurate search
	cc().quickSearch(self,sel,"Test Plan",env.testplanId)
	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName)

	#(2)Fuzzy search
	''' -- remove this part due to fuzzy search by auto is not accurate now
	cc().quickSearch(self,sel,"Test Plan",(env.testplanId)[:3])
	cc().verifySearchPlanPageIsReady(self,sel,testplanIdNames={env.testplanId:env.testplanName})
	'''

	#(3)False search
	cc().quickSearch(self,sel,"Test Plan",(env.testplanId)[:3]+"88888")
	cc().verifySearchPlanPageIsReady(self,sel,testplanIdNames="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
