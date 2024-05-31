import unittest
import HTMLTestRunner
import ts_TCMSRegTestSuite
import sys

# output to a file
'''
We need to make the result filename, title and decription as parameters transferred from command line as follows:

filename ---> browser type ,eg:Firefox4.html
title    ---> component version,eg:rhc-site-0.72.9-1
description ---> Detail information of platform,browser type and component version.

E.g.
python TCMSRegTestHTMLRunner.py --filename="my_report.html" --title="My unit test" --description="This demonstrates the report output by HTMLTestRunner."

'''

if len(sys.argv) != 4:
	print 'Please provide 3 parameters.'
	sys.exit()

for i in range(1,len(sys.argv)):
	if sys.argv[i].startswith("--filename="):
		argv_filename=sys.argv[i][11:]
		print "The report filename is: "+argv_filename
	elif sys.argv[i].startswith("--title="):
		argv_title=sys.argv[i][8:]
		print "The report title is: "+argv_title
	elif sys.argv[i].startswith("--description="):
		argv_description=sys.argv[i][14:]
		print "The report description is: "+argv_description
	else:
		print 'Unknown parameter: '+sys.argv[i]
		sys.exit()

fp = file(argv_filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=argv_title,
        description=argv_description
        )

# Use an external stylesheet.
# See the Template_mixin class for more customizable options
#runner.STYLESHEET_TMPL = '<link rel="stylesheet" href="my_stylesheet.css" type="text/css">'

# run the test
runner.run(ts_TCMSRegTestSuite.suite())

