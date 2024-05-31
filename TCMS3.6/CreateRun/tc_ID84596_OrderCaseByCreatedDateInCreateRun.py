from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class OrderCaseByCreatedDateInCreateRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_OrderCaseByCreatedDateInCreateRun(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId41,env.testcaseName41)
	testcaseCD1=cc().getTestCaseCreatedDate(self,sel,env.testcaseName41)

	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	testcaseCD2=cc().getTestCaseCreatedDate(self,sel,env.testcaseName42)

	#(2)Execute test
	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,filterCase=False,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41,env.testcaseId42:env.testcaseName42})

	dataList=[testcaseCD1,testcaseCD2]
	dataList.sort()

	#click the Title 'Created Date' to sort the test case
	cc().clickActionInCreateRun(self,sel,"Title Created Date")
	cc().verifyCaseOrder(self,sel,"By Created Date",dataList)

	#click the Title 'Created Date' to sort the test case again
	cc().clickActionInCreateRun(self,sel,"Title Created Date")
	cc().verifyCaseOrder(self,sel,"By Created Date",dataList)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
