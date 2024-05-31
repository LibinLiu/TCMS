import unittest
import HTMLTestRunner
import sys

import ts_TCMSP2TestSuite_Plan, env

# output to a file
'''
We need to make the result filename, title and decription as parameters transferred from command line as follows:

filename ---> Test result file name
title ---> Test result file title
description ---> Test result file description

E.g.
python TCMSP2TestHTMLRunner.py --filename="my_report.html" --title="My unit test" --description="This demonstrates the report output by HTMLTestRunner."

'''

fp = file(env.filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=env.title,
        description=env.description
        )

# Use an external stylesheet.
# See the Template_mixin class for more customizable options
#runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

# run the test
runner.run(unittest.TestSuite([ts_TCMSP2TestSuite_Plan.suite()]))

