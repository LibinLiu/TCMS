from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class InputDetailInformation(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_InputDetailInformation(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	#Input the correct Name / Phone number / IM / web / Address / Notes and then save it
	cc().editBasicinfo(self,sel,firstName="libin",lastName="liu",phoneNumber="13900000000",IMType="IRC",\
		IMValue="liliu",webURL="http://www.baidu.com",address="No.33 Fucheng Road",notes="This is just a notes test!!!")

	#Clear off the data
	cc().editBasicinfo(self,sel,firstName="",lastName="",phoneNumber="",\
		IMType="IRC",IMValue="",webURL="",address="",notes="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
