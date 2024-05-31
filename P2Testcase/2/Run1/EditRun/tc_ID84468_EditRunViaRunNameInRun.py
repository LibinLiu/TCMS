from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class EditRunViaRunNameInRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_EditRunViaRunNameInRun(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#open Test Run From Plan by clicking test run name in plan
	cc().openTestRunFromPlan(self,sel,env.testplanName,env.testrunId,env.testrunName,clickRunIdOrName="name")

	#Change some test run info
	runNameNew="Changed "+env.testrunName
	cc().editTestRun(self,sel,env.testrunName,summary=runNameNew,product=env.product2,prodversion=env.prodversion2,build=env.build2,notes=env.longstring)

	#Restore the test run info
	cc().editTestRun(self,sel,runNameNew,summary=env.testrunName,product=env.product1,prodversion=env.prodversion11,build=env.build11,notes="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
