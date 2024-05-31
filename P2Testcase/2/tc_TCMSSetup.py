from selenium import selenium
import unittest, time, re, os

from env import *
from CommonUtils import CCommonUtils as cc

class TCMSSetup(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_TCMSSetup(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	setupDataFile = os.path.dirname(os.path.abspath(__file__)) + os.sep + (dataSuite.__name__).replace(".",os.sep)+".py"

	dataSuiteSymbol = "0"+datasuiteno

	###---(A)To create Test Plan/Case/Run 1 ---###
	testplanName=cc().getAutoDataFormatName(self,sel,"testplanName","1",dataSuiteSymbol)
	testcaseName=cc().getAutoDataFormatName(self,sel,"testcaseName","1",dataSuiteSymbol)
	testrunName=cc().getAutoDataFormatName(self,sel,"testrunName","1",dataSuiteSymbol)

	testplanId=cc().createTestPlan(self,sel,testplanName)
	testcaseId=cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName)
	testrunId=cc().createTestRunFromPlan(self,sel,testplanName,testrunName)
	testcaserunId=cc().getCaseRunIDInRun(self,sel,testrunName,testcaseName)

	#write data into data file
	cc().replaceStrInFile(self,sel,setupDataFile,{"<testplanName>":testplanName, "<testplanId>":testplanId, \
		"<testcaseName>":testcaseName, "<testcaseId>":testcaseId, \
		"<testrunName>":testrunName, "<testrunId>":testrunId, "<testcaserunId>":testcaserunId})

	###---(B)To create Test Plan/Case/Run 2 ---###
	testplanName2=cc().getAutoDataFormatName(self,sel,"testplanName","2",dataSuiteSymbol)
	testcaseName2=cc().getAutoDataFormatName(self,sel,"testcaseName","2",dataSuiteSymbol)
	testrunName2=cc().getAutoDataFormatName(self,sel,"testrunName","2",dataSuiteSymbol)

	testplanId2=cc().createTestPlan(self,sel,testplanName2)
	testcaseId2=cc().createTestCaseFromPlan(self,sel,testplanName2,testcaseName2)
	testrunId2=cc().createTestRunFromPlan(self,sel,testplanName2,testrunName2)
	testcaserunId2=cc().getCaseRunIDInRun(self,sel,testrunName2,testcaseName2)

	#write data into data file
	cc().replaceStrInFile(self,sel,setupDataFile,{"<testplanName2>":testplanName2, "<testplanId2>":testplanId2, \
		"<testcaseName2>":testcaseName2, "<testcaseId2>":testcaseId2, \
		"<testrunName2>":testrunName2, "<testrunId2>":testrunId2, "<testcaserunId2>":testcaserunId2})

	###---(C)To create Test Plan/Case/Run 3 ---###
	testplanName3=cc().getAutoDataFormatName(self,sel,"testplanName","3",dataSuiteSymbol)
	testcaseName3=cc().getAutoDataFormatName(self,sel,"testcaseName","3",dataSuiteSymbol)
	testrunName3=cc().getAutoDataFormatName(self,sel,"testrunName","3",dataSuiteSymbol)

	testplanId3=cc().createTestPlan(self,sel,testplanName3)
	testcaseId3=cc().createTestCaseFromPlan(self,sel,testplanName3,testcaseName3)
	testrunId3=cc().createTestRunFromPlan(self,sel,testplanName3,testrunName3)
	testcaserunId3=cc().getCaseRunIDInRun(self,sel,testrunName3,testcaseName3)

	#write data into data file
	cc().replaceStrInFile(self,sel,setupDataFile,{"<testplanName3>":testplanName3, "<testplanId3>":testplanId3, \
		"<testcaseName3>":testcaseName3, "<testcaseId3>":testcaseId3, \
		"<testrunName3>":testrunName3, "<testrunId3>":testrunId3, "<testcaserunId3>":testcaserunId3})

	###---(D)To create Test Plan/Case/Run 4 ---###
	testplanName4=cc().getAutoDataFormatName(self,sel,"testplanName","4",dataSuiteSymbol)
	testcaseName41=cc().getAutoDataFormatName(self,sel,"testcaseName","41",dataSuiteSymbol)
	testcaseName42=cc().getAutoDataFormatName(self,sel,"testcaseName","41",dataSuiteSymbol)
	testrunName4=cc().getAutoDataFormatName(self,sel,"testrunName","4",dataSuiteSymbol)
	testrunName42=cc().getAutoDataFormatName(self,sel,"testrunName","42",dataSuiteSymbol)

	testplanId4=cc().createTestPlan(self,sel,testplanName4)
	testcaseId41=cc().createCustomizedTestCaseFromPlan(self,sel,testplanName4,summary=testcaseName41,product=env.product1,component=[env.component41],\
		category=env.category11,manual="off",auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")
	testcaseId42=cc().createCustomizedTestCaseFromPlan(self,sel,testplanName4,summary=testcaseName42,product=env.product1,component=[env.component42],\
		category=env.category11,manual="off",auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")
	
	testrunId4=cc().createTestRunFromPlan(self,sel,testplanName4,testrunName4)
	testrunId42=cc().createTestRunFromPlan(self,sel,testplanName4,testrunName42)
	testcaserunId41=cc().getCaseRunIDInRun(self,sel,testrunName4,testcaseName41)
	testcaserunId42=cc().getCaseRunIDInRun(self,sel,testrunName4,testcaseName42)
	testcaserunId421=cc().getCaseRunIDInRun(self,sel,testrunName42,testcaseName41)
	testcaserunId422=cc().getCaseRunIDInRun(self,sel,testrunName42,testcaseName42)

	#write data into data file
	cc().replaceStrInFile(self,sel,setupDataFile,{"<testplanName4>":testplanName4, "<testplanId4>":testplanId4, \
		"<testcaseName41>":testcaseName41, "<testcaseId41>":testcaseId41, "<testcaseName41>":testcaseName42, \
		"<testcaseId41>":testcaseId42, "<testrunName4>":testrunName4, "<testrunId4>":testrunId4, \
		"<testrunName42>":testrunName42, "<testrunId42>":testrunId42, "<testcaserunId41>":testcaserunId41, \
		"<testcaserunId42>":testcaserunId42, "<testcaserunId421>":testcaserunId421, "<testcaserunId422>":testcaserunId422})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
