from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ResetSearchRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ResetSearchRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().openSearchRunPage(self,sel)
	
	#Fill data in Search Run page.
	cc().fillDataForSearchRun(self,sel,summary="runtest",plan="plantest",product=env.product1,prodversion=env.prodversion11,build=env.build11,\
			envgroup=env.envgroup2,status="Running",ownertype="Manager",owner=env.user,caserunassignee=env.user2,tag="tagtest")

	cc().clickActionInSearchRun(self,sel,"Reset")

	cc().verifySearchRunPageIsReady(self,sel,summary="",plan="",product="---------",prodversion="---------",build="---------",\
			envgroup="---------",status="---------",ownertype="Manager | Tester",owner="",caserunassignee="",tag="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
