from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddRemoveInvalidBugInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddRemoveInvalidBugInRun(self):
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

	bugStr="tuvwxyz/#12345678!90~!@#$%^&*()_+"

	#Execute test
	#(1) select 1 case
	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().clickAddBug(self,sel,bugStr,bugNoIsValid=False)

	cc().verifyReportInfoInRun(self,sel,bugNum="0")
	cc().clickActionInRun(self,sel,"Report")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList="")

	cc().openTestRun(self,sel,testrunName)
	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().clickRemoveBug(self,sel,bugStr,bugNoIsValid=False)

	cc().verifyReportInfoInRun(self,sel,bugNum="0")
	cc().clickActionInRun(self,sel,"Report")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList="")

	#(2) select 2 cases
	cc().openTestRun(self,sel,testrunName)
	cc().selectCaseInRun(self,sel,[testcaserunId1,testcaserunId2])
	cc().clickAddBug(self,sel,bugStr,bugNoIsValid=False)

	cc().verifyReportInfoInRun(self,sel,bugNum="0")
	cc().clickActionInRun(self,sel,"Report")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList="")

	cc().openTestRun(self,sel,testrunName)
	cc().selectCaseInRun(self,sel,[testcaserunId1,testcaserunId2])
	cc().clickRemoveBug(self,sel,bugStr,bugNoIsValid=False)

	cc().verifyReportInfoInRun(self,sel,bugNum="0")
	cc().clickActionInRun(self,sel,"Report")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList="")

	#(3) select all cases
	cc().openTestRun(self,sel,testrunName)
	cc().selectCaseInRun(self,sel,"All")
	cc().clickAddBug(self,sel,bugStr,bugNoIsValid=False)

	cc().verifyReportInfoInRun(self,sel,bugNum="0")
	cc().clickActionInRun(self,sel,"Report")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList="")

	cc().openTestRun(self,sel,testrunName)
	cc().selectCaseInRun(self,sel,"All")
	cc().clickRemoveBug(self,sel,bugStr,bugNoIsValid=False)

	cc().verifyReportInfoInRun(self,sel,bugNum="0")
	cc().clickActionInRun(self,sel,"Report")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
