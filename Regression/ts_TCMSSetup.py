from selenium import selenium
import unittest, time, re

from env import *

from CreatePlans import CreatePlans
from CreateCases import CreateCases
from CreateRuns import CreateRuns

def suite():

	suite = unittest.TestSuite()
	suite.addTest(CreatePlans("test_create_plans"))
	suite.addTest(CreateCases("test_create_cases"))
	suite.addTest(CreateRuns("test_create_runs"))

	return suite

if __name__ == "__main__":
   unittest.main(defaultTest = 'suite')
