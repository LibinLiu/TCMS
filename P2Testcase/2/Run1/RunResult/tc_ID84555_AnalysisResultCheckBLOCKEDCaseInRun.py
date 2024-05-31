from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AnalysisResultCheckBLOCKEDCaseInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AnalysisResultCheckBLOCKEDCaseInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestRun(self,sel,env.testrunName4)

	#(1)change status to BLOCKED
	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().alterCaseRunStatus(self,sel,"BLOCKED")
	
	#Verify if the status has been changed successfully and the report info shown in run is correct
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"BLOCKED")
	cc().verifyReportInfoInRun(self,sel,IDLE="1",BLOCKED="1",TOTAL="2")
	
	#(2)restore status to IDLE
	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().alterCaseRunStatus(self,sel,"IDLE")

	#Verify if the status has been changed successfully and the report info shown in run is correct
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"IDLE")
	cc().verifyReportInfoInRun(self,sel,IDLE="2",TOTAL="2")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
