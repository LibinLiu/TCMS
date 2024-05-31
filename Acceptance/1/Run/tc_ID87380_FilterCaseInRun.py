from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class FilterCaseInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_FilterCaseInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	cc().openTestRun(self,sel,env.testrunName4)

	#Add bugs to the case
	bugList=[]
	bugStr=""
	for i in range(100000,100005):
		bugList.append(str(i))
		bugStr+=str(i)+","
	bugStr=bugStr[:-1]

	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().clickAddBug(self,sel,bugStr)

	#change the case's status to BLOCKED
	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().alterCaseRunStatus(self,sel,"BLOCKED")
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"BLOCKED")

	#(2)Execute test
	cc().filterCaseInRun(self,sel,summary=env.testcaseName41,defaulttester=env.useremail,\
		assignee=env.useremail,bugno=bugStr,status="BLOCKED",priority="P1",\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41},\
		testcaseResultNoIdNames={env.testcaseId42:env.testcaseName42})

	#(3)Restore test data
	#remove bug
	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().clickRemoveBug(self,sel,bugStr)

	#restore status to IDLE
	cc().openHomePage(self,sel)
	cc().openTestRun(self,sel,env.testrunName4)
	cc().selectCaseInRun(self,sel,[env.testcaserunId41])
	cc().alterCaseRunStatus(self,sel,"IDLE")
 	cc().verifyCaseRunStatus(self,sel,env.testcaseName41,"IDLE")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
