from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class OrderCaseBySummaryInCreateRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_OrderCaseBySummaryInCreateRun(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#Execute test
	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,filterCase=False,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41,env.testcaseId42:env.testcaseName42})

	dataList=[env.testcaseName41,env.testcaseName42]
	dataList.sort()

	#click the Title 'Test Case Summary' to sort the test case
	cc().clickActionInCreateRun(self,sel,"Title Test Case Summary")
	cc().verifyCaseOrder(self,sel,"By Test Case Summary",dataList)

	#click the Title 'Test Case Summary' to sort the test case again
	cc().clickActionInCreateRun(self,sel,"Title Test Case Summary")
	cc().verifyCaseOrder(self,sel,"By Test Case Summary",dataList)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
