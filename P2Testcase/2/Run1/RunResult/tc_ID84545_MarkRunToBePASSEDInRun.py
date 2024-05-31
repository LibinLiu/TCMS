from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class MarkRunToBePASSEDInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_MarkRunToBePASSEDInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

	#Prepare test data
	testplanName=env.testplanName4
	testcaseName1=env.testcaseName41
	component1=env.component41
	testcaseName2=env.testcaseName42
	component2=env.component42
	testrunName=env.testrunName4
	testrunId=env.testrunId4
	testcaserunId1=env.testcaserunId41
	testcaserunId2=env.testcaserunId42

	cc().openTestRun(self,sel,testrunName)

	if cc().getCaseRunLineNoInRun(self,sel,testrunName,env.testcaseName41)==2 and \
		cc().getCaseRunLineNoInRun(self,sel,testrunName,env.testcaseName42)==1 :
		
		testcaseName1=env.testcaseName42
		component1=env.component42
		testcaserunId1=env.testcaserunId42

		testcaseName2=env.testcaseName41
		component2=env.component41
		testcaserunId2=env.testcaserunId41

	#Execute test
	#(A) - Mark the 1st case in run to be PASSED
	#expand test case 1
	cc().expandCaseInRun(self,sel,testcaseName1)
	cc().verifyText(self,sel,component1)
	cc().verifyTextNotPresent(self,sel,component2)

	#change test case 1's status to PASSED
	cc().alterCaseRunStatusByIcon(self,sel,testcaseName1,"PASSED")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,testcaseName1,"PASSED")
	
	#Verify the 1st case has been collapsed and the 2nd case has been expanded
	cc().verifyTextNotPresent(self,sel,component1)
	cc().verifyText(self,sel,component2)

	#----------------------------------------
	#(B) - Mark the 2nd case, that is, the last one in run to be PASSED
	cc().openTestRunFromPlan(self,sel,testplanName,testrunId,testrunName)
	
	#expand test case 2
	cc().expandCaseInRun(self,sel,testcaseName2)
	cc().verifyText(self,sel,component2)

	#change test case 2's status to PASSED
	cc().alterCaseRunStatusByIcon(self,sel,testcaseName2,"PASSED")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,testcaseName2,"PASSED")

	#Verify both cases have been collapsed
	cc().verifyTextNotPresent(self,sel,component1)
	cc().verifyTextNotPresent(self,sel,component2)

	#----------------------------------------
	#Restore 2 caseruns' status to IDLE
	cc().selectCaseInRun(self,sel,[testcaserunId1,testcaserunId2])
	cc().alterCaseRunStatus(self,sel,"IDLE")

	#Verify if the status has been changed successfully and the report info shown in run is correct
 	cc().verifyCaseRunStatus(self,sel,testcaseName1,"IDLE")
 	cc().verifyCaseRunStatus(self,sel,testcaseName2,"IDLE")
	cc().verifyReportInfoInRun(self,sel,IDLE="2",TOTAL="2")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
