from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class MarkRunToBeIDLEInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_MarkRunToBeIDLEInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data
	testplanName=env.testplanName4
	testcaseName1=env.testcaseName41
	component1=env.component41
	testcaseName2=env.testcaseName42
	component2=env.component42
	testrunName=env.testrunName4
	testrunId=env.testrunId4

	cc().openTestRun(self,sel,testrunName)

	if cc().getCaseRunLineNoInRun(self,sel,testrunName,env.testcaseName41)==2 and \
		cc().getCaseRunLineNoInRun(self,sel,testrunName,env.testcaseName42)==1 :
		
		testcaseName1=env.testcaseName42
		component1=env.component42

		testcaseName2=env.testcaseName41
		component2=env.component41

	#Execute test
	#(A1) - Mark the 1st case in run to be BLOCKED
	#expand test case 1
	cc().expandCaseInRun(self,sel,testcaseName1)
	cc().verifyText(self,sel,component1)
	cc().verifyTextNotPresent(self,sel,component2)

	#change test case 1's status to BLOCKED
	cc().alterCaseRunStatusByIcon(self,sel,testcaseName1,"BLOCKED")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,testcaseName1,"BLOCKED")
	
	#Verify the 1st case has been collapsed and the 2nd case has been expanded
	cc().verifyTextNotPresent(self,sel,component1)
	cc().verifyText(self,sel,component2)

	#----------------------------------------
	#(B1) - Mark the 2nd case, that is, the last one in run to be BLOCKED
	cc().openTestRunFromPlan(self,sel,testplanName,testrunId,testrunName)
	
	#expand test case 2
	cc().expandCaseInRun(self,sel,testcaseName2)
	cc().verifyText(self,sel,component2)

	#change test case 2's status to BLOCKED
	cc().alterCaseRunStatusByIcon(self,sel,testcaseName2,"BLOCKED")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,testcaseName2,"BLOCKED")

	#Verify both cases have been collapsed
	cc().verifyTextNotPresent(self,sel,component1)
	cc().verifyTextNotPresent(self,sel,component2)

	#======================================================

	#(A2) - Mark the 1st case in run to be IDLE
	cc().openTestRunFromPlan(self,sel,testplanName,testrunId,testrunName)

	#expand test case 1
	cc().expandCaseInRun(self,sel,testcaseName1)
	cc().verifyText(self,sel,component1)
	cc().verifyTextNotPresent(self,sel,component2)

	#change test case 1's status to IDLE
	cc().alterCaseRunStatusByIcon(self,sel,testcaseName1,"IDLE")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,testcaseName1,"IDLE")
	
	#Verify the 1st case has been collapsed and the 2nd case has been expanded
	cc().verifyTextNotPresent(self,sel,component1)
	cc().verifyText(self,sel,component2)

	#----------------------------------------
	#(B2) - Mark the 2nd case, that is, the last one in run to be IDLE
	cc().openTestRunFromPlan(self,sel,testplanName,testrunId,testrunName)
	
	#expand test case 2
	cc().expandCaseInRun(self,sel,testcaseName2)
	cc().verifyText(self,sel,component2)

	#change test case 2's status to IDLE
	cc().alterCaseRunStatusByIcon(self,sel,testcaseName2,"IDLE")

	#Verify if the status has been changed successfully
 	cc().verifyCaseRunStatus(self,sel,testcaseName2,"IDLE")

	#Verify both cases have been collapsed
	cc().verifyTextNotPresent(self,sel,component1)
	cc().verifyTextNotPresent(self,sel,component2)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
