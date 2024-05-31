from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class OrderCaseByPriorityInCreateRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_OrderCaseByPriorityInCreateRun(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	cc().editTestCase(self,sel,env.testcaseName42,priority="P2")

	#(2)Execute test
	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,filterCase=False,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41,env.testcaseId42:env.testcaseName42})

	dataList=["P1","P2"]
	dataList.sort()

	#click the Title 'Priority' to sort the test case
	cc().clickActionInCreateRun(self,sel,"Title Priority")
	cc().verifyCaseOrder(self,sel,"By Priority",dataList)

	#click the Title 'Priority' to sort the test case again
	cc().clickActionInCreateRun(self,sel,"Title Priority")
	cc().verifyCaseOrder(self,sel,"By Priority",dataList)

	#(3)Restore test data
	cc().openTestCaseFromPlan(self,sel,env.testplanName4,env.testcaseId42,env.testcaseName42)
	cc().editTestCase(self,sel,env.testcaseName42,priority="P1")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
