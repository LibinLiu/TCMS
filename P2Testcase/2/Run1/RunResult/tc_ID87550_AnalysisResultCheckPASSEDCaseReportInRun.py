from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AnalysisResultCheckPASSEDCaseReportInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AnalysisResultCheckPASSEDCaseReportInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data
	testcaseName1=env.testcaseName41
	testcaseName2=env.testcaseName42
	testrunName=env.testrunName4
	testrunId=env.testrunId4
	testcaserunId1=env.testcaserunId41
	testcaserunId2=env.testcaserunId42

	cc().openTestRun(self,sel,testrunName)

	if cc().getCaseRunLineNoInRun(self,sel,testrunName,env.testcaseName41)==2 and \
		cc().getCaseRunLineNoInRun(self,sel,testrunName,env.testcaseName42)==1 :
		
		testcaseName1=env.testcaseName42
		testcaserunId1=env.testcaserunId42

		testcaseName2=env.testcaseName41
		testcaserunId2=env.testcaserunId41

	#Execute test
	#(1)change status to PASSED
	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().alterCaseRunStatus(self,sel,"PASSED")
	
	#Verify if the status has been changed successfully and the report info shown in run is correct
 	cc().verifyCaseRunStatus(self,sel,testcaseName1,"PASSED")
	cc().verifyReportInfoInRun(self,sel,IDLE="1",PASSED="1",TOTAL="2")
	
	cc().clickActionInRun(self,sel,"Report")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["PASSED","IDLE"])

	#(2)restore status to IDLE
	cc().openTestRun(self,sel,testrunName)
	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().alterCaseRunStatus(self,sel,"IDLE")

	#Verify if the status has been changed successfully and the report info shown in run is correct
 	cc().verifyCaseRunStatus(self,sel,testcaseName1,"IDLE")
	cc().verifyReportInfoInRun(self,sel,IDLE="2",TOTAL="2")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
