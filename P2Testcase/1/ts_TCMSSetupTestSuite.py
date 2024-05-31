from selenium import selenium
import unittest, time, re

from env import *

#(Total: 46)
#CreateRun related test cases (total: 31)
import tc_TCMSSetup

def suite():

	suite = unittest.TestSuite()

	suite.addTest(tc_TCMSSetup.TCMSSetup("test_TCMSSetup"))
	
	return suite

if __name__ == "__main__":
   unittest.main(defaultTest = 'suite')
