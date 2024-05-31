from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchRunBySingleMultiStatus(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchRunBySingleMultiStatus(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data: Add a tag in runs & change the status of run
	rdm=random.uniform(1, 1000)
	tagName = "mytag@xx"+str(rdm)
	cc().openTestRun(self,sel,env.testrunName4)
	cc().addTagInRun(self,sel,tagName,needRemove=False)

	cc().openTestRun(self,sel,env.testrunName42)
	cc().addTagInRun(self,sel,tagName,needRemove=False)
	cc().setStatusToFinishedOrRunningInRun(self,sel,"Set to Finished")

	#Search Run By Single Status
	cc().searchRunByRunOptInASearch(self,sel,tag=tagName,status="Running",\
		resultIdNames={env.testrunId4:env.testrunName4},resultNoIdNames={env.testrunId42:env.testrunName42})
	cc().searchRunByRunOptInASearch(self,sel,tag=tagName,status="Finished",\
		resultIdNames={env.testrunId42:env.testrunName42},resultNoIdNames={env.testrunId4:env.testrunName4})

	#Search Run By Multiple Status
	cc().searchRunByRunOptInASearch(self,sel,tag=tagName,status="All",\
		resultIdNames={env.testrunId4:env.testrunName4,env.testrunId42:env.testrunName42})

	#Restore test data: Remove the tag from runs & restore the status of run
	cc().clickLink(self,sel,env.testrunId4)
	cc().removeTagInRun(self,sel,tagName)

	cc().openTestRun(self,sel,env.testrunName42)
	cc().removeTagInRun(self,sel,tagName)
	cc().setStatusToFinishedOrRunningInRun(self,sel,"Set to Running")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
