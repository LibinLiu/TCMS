from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AnalysisResultCheckShowAllBugsInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AnalysisResultCheckShowAllBugsInRun(self):
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

	bugNo1 = "123456"
	bugNo2 = "112233"
	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().clickAddBug(self,sel,bugNo1)
	cc().selectCaseInRun(self,sel,[testcaserunId2])
	cc().clickAddBug(self,sel,bugNo2)

	cc().clickActionInRun(self,sel,"Show All Bugs")
	cc().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList=[bugNo1,bugNo2])

	cc().openTestRun(self,sel,testrunName)
	cc().selectCaseInRun(self,sel,[testcaserunId1])
	cc().clickRemoveBug(self,sel,bugNo1)
	cc().selectCaseInRun(self,sel,[testcaserunId2])
	cc().clickRemoveBug(self,sel,bugNo2)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
