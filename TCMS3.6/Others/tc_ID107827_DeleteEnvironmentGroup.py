from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class DeleteEnvironmentGroup(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_DeleteEnvironmentGroup(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openEnvGroupsPage(self,sel)

	groupName="Auto-NewGroup-"+time.strftime('%Y%m%d%H%M%S')
	cc().addGroupInEnvGroupsPage(self,sel,groupName)

	cc().openEnvGroupsPage(self,sel)
	cc().removeGroupInEnvGroupsPage(self,sel,groupName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
