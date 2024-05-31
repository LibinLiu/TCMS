from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ResetAfterSearchingRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ResetAfterSearchingRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().searchTestRun(self,sel,summary=env.testrunName,plan=env.testplanName,product=env.product1,prodversion=env.prodversion11,\
			build=env.build11,envgroup="---------",status="Running",ownertype="Manager | Tester",owner=env.user+"@redhat.com",\
			caserunassignee=env.user,tag="",testrunIdNames={env.testrunId:env.testrunName})

	cc().clickActionInSearchRun(self,sel,"Reset")

	cc().verifySearchRunPageIsReady(self,sel,summary=env.testrunName,plan=env.testplanName,product=env.product1,prodversion=env.prodversion11,\
			build=env.build11,envgroup="---------",status="Running",ownertype="Manager | Tester",owner=env.user+"@redhat.com",\
			caserunassignee=env.user,tag="",testrunIdNames={env.testrunId:env.testrunName})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
