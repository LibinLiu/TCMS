from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseByOverCreateTimeInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseByOverCreateTimeInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#search via just case id
	cc().searchCaseByCaseOptInASearch(self,sel,caseId=env.testcaseId,resultIdNames={env.testcaseId:env.testcaseName})

	#search via both case id and create time which is over
	cc().searchCaseByCaseOptInASearch(self,sel,caseId=env.testcaseId,\
		createdAfter=str(int(time.strftime('%Y'))+1)+'-'+time.strftime('%m'+'-'+'%d'),resultIdNames="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
