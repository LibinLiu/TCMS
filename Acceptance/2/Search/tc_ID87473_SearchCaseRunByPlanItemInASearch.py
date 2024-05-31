from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class SearchCaseRunByPlanItemInASearch(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_SearchCaseRunByPlanItemInASearch(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	#Add a new tag and component in test plan
	cc().openTestPlan(self,sel,env.testplanName)

	rdm=random.uniform(1, 1000)
	tagName1 = "aa@@bb111"+str(rdm)
	cc().addTagInPlan(self,sel,tagName1,needRemove=False)
	cc().addComponentInPlan(self,sel,[env.component12])

	#--(B) Execute test
	#(1)Search test case
	cc().openAdvancedSearchPage(self,sel)

	#Fill in the test plan information
	cc().fillDataForPlanItemsInASearch(self,sel,productList=[env.product1],\
		componentList=[env.component12],planId=env.testplanId,\
		summary=env.testplanName,planTypeList=[env.plantype11],author=env.user,\
		owner=env.user,tag=tagName1,tagOption="Contains",active="Active",\
		createdAfter="2000-01-01",createdBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

        cc().clickActionInAdvancedSearch(self,sel,"Search Case")
	cc().verifyAdvancedSearchCaseResultIsReady(self,sel,tIdNames={env.testcaseId:env.testcaseName})
	
	#(2)Search test run
	cc().openAdvancedSearchPage(self,sel)

	#Fill in the test plan information
	cc().fillDataForPlanItemsInASearch(self,sel,productList=[env.product1],componentList=[env.component12],\
		prodversionList=[env.prodversion11],planId=env.testplanId,\
		summary=env.testplanName,planTypeList=[env.plantype11],author=env.user,\
		owner=env.user,tag=tagName1,tagOption="Contains",active="Active",\
		createdAfter="2000-01-01",createdBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'))

        cc().clickActionInAdvancedSearch(self,sel,"Search Run")
	cc().verifyAdvancedSearchRunResultIsReady(self,sel,tIdNames={env.testrunId:env.testrunName})

	#--(C) Remove test data
	#Remove the added tag and component from test plan
	cc().openTestPlan(self,sel,env.testplanName)
	cc().removeTagInPlan(self,sel,[tagName1])
	cc().removeComponentInPlan(self,sel,{env.componentId12:env.component12})
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
