import time, re, os

class AutoUtils():
    
	def generateInitSuiteFileWithSubDir(self):
	
		maindir=[] #For example: maindir=["./Run/EditRun","./Run/RunResult"]
		dirstr=[] #For example: dirstr=["Run.EditRun","Run.RunResult"]

		suitestr1=""
		suitestr2=""
		total=0

		tsfilename='ts_TCMSP2TestSuite_Run2.py'
		mydir="./Run2"

		#Remove the empty '__init__.py' file in 'mydir, if exists.'
		if os.path.isfile(mydir+os.sep+'__init__.py'):
			os.remove(mydir+os.sep+'__init__.py')

		ds=os.listdir(mydir)
		ds.sort()
		for k in range(len(ds)):
			maindir.append(mydir+os.sep+ds[k])
			dirstr.append(mydir[2:]+"."+ds[k])

		#(1)Generate '__init__.py' files
		for t in range(len(maindir)):
			tstr=""
			sstr=""

			if os.path.isfile(maindir[t]+os.sep+'__init__.py'):
				os.remove(maindir[t]+os.sep+'__init__.py')

			fs=os.listdir(maindir[t])
			fs.sort()
			for i in range(len(fs)):
				f=fs[i]

				t1=f.find('tc_ID')
				t2=f.find('.py')		
				f1=f[t1+5:t2]

				t3=f1.find('_')
				f1=f1[t3+1:]
		
				tstr+=dirstr[t]+"."+f[:t2]+", "
				sstr+="	suite.addTest("+dirstr[t]+"."+f[:t2]+"."+f1+"(\"test_"+f1+"\"))"+"\r\n"

			tstr="#"+dirstr[t]+" related test cases (total: "+str(len(fs))+")"+"\r\n"+"import "+tstr[:-2]
			sstr="	#"+dirstr[t]+" related test cases (total: "+str(len(fs))+")"+"\r\n"+sstr
			total+=len(fs)

			f = file(maindir[t]+os.sep+'__init__.py', 'w') # open for 'w'riting
			f.write(tstr) # write text to file
			f.close() # close the file

			suitestr1+=tstr+"\r\n\r\n"
			suitestr2+=sstr+"\r\n"

		#Generate an empty '__init__.py' file in 'mydir'
		f = file(mydir+os.sep+'__init__.py', 'w')
		f.write("")
		f.close()

		#(2)Generate test suite file
		suitestr="from selenium import selenium\r\n"+"import unittest, time, re\r\n\r\n"+"from env import *\r\n\r\n"+"#(Total: "+str(total)+")\r\n"
		suitestr+=suitestr1
		suitestr+="def suite():\r\n\r\n	suite = unittest.TestSuite()\r\n\r\n"
		suitestr+=suitestr2
		suitestr+="	return suite\r\n\r\nif __name__ == \"__main__\":\r   unittest.main(defaultTest = 'suite')"

		f = file(tsfilename, 'w')
		f.write(suitestr)
		f.close()

	def generateInitSuiteFileWithoutSubDir(self):

		suitestr1=""
		suitestr2=""
		total=0

		tsfilename='ts_TCMSP2TestSuite_Plan.py'

		mydir="./Plan"
		dirstr="Plan"

		#(1)Generate '__init__.py' files
		tstr=""
		sstr=""

		if os.path.isfile(mydir+os.sep+'__init__.py'):
			os.remove(mydir+os.sep+'__init__.py')

		fs=os.listdir(mydir)
		fs.sort()
		for i in range(len(fs)):
			f=fs[i]

			t1=f.find('tc_ID')
			t2=f.find('.py')		
			f1=f[t1+5:t2]

			t3=f1.find('_')
			f1=f1[t3+1:]
	
			tstr+=dirstr+"."+f[:t2]+", "
			sstr+="	suite.addTest("+dirstr+"."+f[:t2]+"."+f1+"(\"test_"+f1+"\"))"+"\r\n"

		tstr="#"+dirstr+" related test cases (total: "+str(len(fs))+")"+"\r\n"+"import "+tstr[:-2]
		sstr="	#"+dirstr+" related test cases (total: "+str(len(fs))+")"+"\r\n"+sstr
		total+=len(fs)

		f = file(mydir+os.sep+'__init__.py', 'w') # open for 'w'riting
		f.write(tstr) # write text to file
		f.close() # close the file

		suitestr1+=tstr+"\r\n\r\n"
		suitestr2+=sstr+"\r\n"

		#(2)Generate test suite file 'tsfilename'
		suitestr="from selenium import selenium\r\n"+"import unittest, time, re\r\n\r\n"+"from env import *\r\n\r\n"+"#(Total: "+str(total)+")\r\n"
		suitestr+=suitestr1
		suitestr+="def suite():\r\n\r\n	suite = unittest.TestSuite()\r\n\r\n"
		suitestr+=suitestr2
		suitestr+="	return suite\r\n\r\nif __name__ == \"__main__\":\r   unittest.main(defaultTest = 'suite')"

		f = file(tsfilename, 'w')
		f.write(suitestr)
		f.close()

	def generateInitSuiteFileWithoutSubDir2(self):

		rootdir="./Test"
		tsfilename=rootdir+os.sep+'ts_TCMSP2TestSuite.py'

		#----------------------------------------------------------------------------

		maindir=[] #For example: maindir=["./Run/EditRun","./Run/RunResult"]
		dirstr=[] #For example: dirstr=["Run.EditRun","Run.RunResult"]

		suitestr1=""
		suitestr2=""
		total=0


		ds=os.listdir(rootdir)
		ds.sort()
		for k in range(len(ds)):
			maindir.append(rootdir+os.sep+ds[k])
			dirstr.append(ds[k])

		#(1)Generate '__init__.py' files
		for t in range(len(maindir)):
			tstr=""
			sstr=""

			if os.path.isfile(maindir[t]+os.sep+'__init__.py'):
				os.remove(maindir[t]+os.sep+'__init__.py')

			fs=os.listdir(maindir[t])
			fs.sort()
			for i in range(len(fs)):
				f=fs[i]

				t1=f.find('tc_ID')
				t2=f.find('.py')		
				f1=f[t1+5:t2]

				t3=f1.find('_')
				f1=f1[t3+1:]
		
				tstr+=dirstr[t]+"."+f[:t2]+", "
				sstr+="	suite.addTest("+dirstr[t]+"."+f[:t2]+"."+f1+"(\"test_"+f1+"\"))"+"\r\n"

			tstr="#"+dirstr[t]+" related test cases (total: "+str(len(fs))+")"+"\r\n"+"import "+tstr[:-2]
			sstr="	#"+dirstr[t]+" related test cases (total: "+str(len(fs))+")"+"\r\n"+sstr
			total+=len(fs)

			f = file(maindir[t]+os.sep+'__init__.py', 'w') # open for 'w'riting
			f.write(tstr) # write text to file
			f.close() # close the file

			suitestr1+=tstr+"\r\n\r\n"
			suitestr2+=sstr+"\r\n"

		#(2)Generate test suite file
		suitestr="from selenium import selenium\r\n"+"import unittest, time, re\r\n\r\n"+"from env import *\r\n\r\n"+"#(Total: "+str(total)+")\r\n"
		suitestr+=suitestr1
		suitestr+="def suite():\r\n\r\n	suite = unittest.TestSuite()\r\n\r\n"
		suitestr+=suitestr2
		suitestr+="	return suite\r\n\r\nif __name__ == \"__main__\":\r   unittest.main(defaultTest = 'suite')"

		f = file(tsfilename, 'w')
		f.write(suitestr)
		f.close()

	def getTCIDList(self):
		''' This function is used for getting id list of all test cases in the 'dirPath'. '''

		dirPath="./Today"

		fs=os.listdir(dirPath)
		fs.sort()
		tstr=""
		for i in range(len(fs)):
			f=fs[i]

			t1=f.find('tc_ID')
			t2=f.find('.py')		
			f1=f[t1+5:t2]

			t3=f1.find('_')
			f1=f1[:t3]
	
			tstr+=f1+", "
	
		f = file(dirPath+os.sep+'list.py', 'w') # open for 'w'riting
		f.write(tstr) # write text to file
		f.close() # close the file

if __name__ == "__main__":
#    AutoUtils().generateInitSuiteFileWithSubDir()
#    AutoUtils().generateInitSuiteFileWithoutSubDir()
#    AutoUtils().generateInitSuiteFileWithoutSubDir2()
    AutoUtils().getTCIDList()

