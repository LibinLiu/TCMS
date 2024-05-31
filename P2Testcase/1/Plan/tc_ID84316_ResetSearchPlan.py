from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ResetSearchPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ResetSearchPlan(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openSearchPlanPage(self,sel)

	cc().fillDataForSearchPlan(self,sel,planName=env.testplanName,author=env.user,owner=env.user,\
		planType=env.plantype11,tag="xxx",caseDefaultTester=env.user,product=env.product1,\
		prodversion=env.prodversion11,envgroup=env.envgroup1,createdAfter="2000-01-01",\
		createdBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'),active="off")

	cc().clickActionInSearchPlan(self,sel,"Reset")
	time.sleep(env.ts)

	cc().verifySearchPlanPageIsReady(self,sel,planName='',author='',owner='',\
		planType='---------',tag='',caseDefaultTester='',product='---------',\
		prodversion='---------',envgroup='---------',createdAfter='',\
		createdBefore='',active="on")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
