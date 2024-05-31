from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class UpdateSortNumForRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_UpdateSortNumForRun(self):
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

	cc().editCaseRunSortNumInRun(self,sel,testrunId,testcaserunId1,"10","30")
	cc().verifyTargetText(self,sel,testcaseName1,"link_2")

	cc().editCaseRunSortNumInRun(self,sel,testrunId,testcaserunId1,"30","10")
	cc().verifyTargetText(self,sel,testcaseName1,"link_1")


    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
