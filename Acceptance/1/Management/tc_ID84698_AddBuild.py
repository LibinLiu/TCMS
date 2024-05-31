from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class AddBuild(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_AddBuild(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openManagementPage(self,sel)

	buildName="Auto-NewBuild-"+time.strftime('%Y%m%d%H%M%S')
	cc().addBuildFromManagementPage(self,sel,buildName,env.product1)
	cc().verifySelectBuildToChangePageIsReady(self,sel)

	cc().searchBuildToVerify(self,sel,buildName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
