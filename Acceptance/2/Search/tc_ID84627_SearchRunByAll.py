from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchRunByAll(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchRunByAll(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Add a tag in run
	cc().openTestRun(self,sel,env.testrunName)

	rdm=random.uniform(1, 1000)
	tagName = "mytag@xx"+str(rdm)
	cc().addTagInRun(self,sel,tagName,needRemove=False)

	#Search Run By all search conditions
	cc().searchTestRun(self,sel,summary=env.testrunName,plan=env.testplanName,product=env.product1,prodversion=env.prodversion11,\
			build=env.build11,status="Running",ownertype="Manager | Tester",owner=env.user+"@redhat.com",\
			caserunassignee=env.user,tag=tagName,testrunIdNames={env.testrunId:env.testrunName})

	#Remove the tag from run
	cc().clickLink(self,sel,env.testrunId)
	cc().removeTagInRun(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
