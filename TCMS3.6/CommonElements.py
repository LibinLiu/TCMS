from selenium import selenium
import unittest, time, re

from env import *

class CCommonElements:

	#===================================================================
	# 	Common basic functions (1) - Action
	#===================================================================

	def inputText(self,myself,sel,fieldIdOrNameOrTarget,inputString):
		''' Input string into text field. Example of call: CCommonUtils().inputText(self,sel,"id_plan","test")'''

		self.verifyElement(myself,sel,fieldIdOrNameOrTarget)
		sel.type(fieldIdOrNameOrTarget, inputString)
		time.sleep(1)

	def clickBtn(self,myself,sel,btnType,btnValue):
		''' click a common button. '''

		self.clickElement(myself,sel,"//input[@type='"+btnType+"' and @value='"+btnValue+"']")

	def clickBtnAndWait(self,myself,sel,btnType,btnValue):
		''' click a common button and wait for the page to load. '''

		self.clickElementAndWait(myself,sel,"//input[@type='"+btnType+"' and @value='"+btnValue+"']")

	def clickLink(self,myself,sel,linkText):
		''' click a link. '''

		self.clickElement(myself,sel,"link="+linkText)

	def clickLinkAndWait(self,myself,sel,linkText):
		''' click a link and wait for the page to load. '''

		self.clickElementAndWait(myself,sel,"link="+linkText)

	def clickElement(self,myself,sel,elementTarget):
		''' click an element. '''

		self.verifyElement(myself,sel,elementTarget)   # An example for 'elementTarget': "//a[@onclick='showCommentForm();']"
		sel.click(elementTarget)
		time.sleep(env.ts)

	def clickElementAndWait(self,myself,sel,elementTarget):
		''' click an element and wait for the page to load. '''

		self.verifyElement(myself,sel,elementTarget)   # An example for 'elementTarget': "//a[@onclick='showCommentForm();']"
		sel.click(elementTarget)
		sel.wait_for_page_to_load("30000")
		time.sleep(env.ts)

	def clickAt(self,myself,sel,elementTarget):
		''' click an location. '''

		self.verifyElement(myself,sel,elementTarget)   # An example for 'elementTarget': "//table[@id='testcases']/thead/tr/th[6]"
		sel.click_at(elementTarget, "")
		time.sleep(env.ts)

	def clickAtAndWait(self,myself,sel,elementTarget):
		''' click an location and wait for the page to load. '''

		self.verifyElement(myself,sel,elementTarget)   # An example for 'elementTarget': "//table[@id='testcases']/thead/tr/th[6]"
		sel.click_at(elementTarget, "")
		sel.wait_for_page_to_load("30000")
		time.sleep(env.ts)

	def clickCheckBox(self,myself,sel,fieldIdOrName,fieldValue,fieldTarget="<default>",onoff="<default>"):
		''' click check box to select it or not. The value of onoff should be one of them: 'on' or 'off'. '''

		elementTarget = ""
		if fieldValue != "":
			if fieldIdOrName == "":
				elementTarget="//input[@value='"+fieldValue+"']"
			elif  fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
				elementTarget="//input[@id='"+fieldIdOrName+"' and @value='"+fieldValue+"']"
			elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
				elementTarget="//input[@id='"+fieldIdOrName[3:]+"' and @value='"+fieldValue+"']"
			else: elementTarget="//input[@name='"+fieldIdOrName+"' and @value='"+fieldValue+"']"
		else:
			if fieldIdOrName == "":
				if fieldTarget!="<default>":
					elementTarget=fieldTarget
			elif fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
				elementTarget="//input[@id='"+fieldIdOrName+"']"
			elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
				elementTarget="//input[@id='"+fieldIdOrName[3:]+"']"
			else: elementTarget="//input[@name='"+fieldIdOrName+"']"

		self.verifyElement(myself,sel,elementTarget)
		if onoff!="<default>":
			for i in range(3):
			    try:
				if onoff == sel.get_value(elementTarget): break
			    except: pass
			    time.sleep(1)
			else: sel.click(elementTarget)
		else: sel.click(elementTarget)
		time.sleep(1)

	def clickRadioBtn(self,myself,sel,fieldIdOrName,fieldValue,fieldTarget="<default>",onoff="<default>"):
		''' click radio button to select it. The value of onoff should be one of them: 'on' or 'off'. '''
	
		#The process of clicking check box and radio btton is totally the same
		self.clickCheckBox(myself,sel,fieldIdOrName,fieldValue,fieldTarget,onoff)

	def selectOptionInList(self,myself,sel,fieldIdOrNameOrTarget,optionText):
		''' Select an option in a list field. '''

		time.sleep(env.ts-2)
		self.verifyElement(myself,sel,fieldIdOrNameOrTarget)
		sel.add_selection(fieldIdOrNameOrTarget, "label="+optionText)
		time.sleep(env.ts-2)

	def unselectOptionInList(self,myself,sel,fieldIdOrNameOrTarget,optionText):
		''' Unselect an option in a list field. '''

		time.sleep(env.ts-2)
		self.verifyElement(myself,sel,fieldIdOrNameOrTarget)
		sel.remove_selection(fieldIdOrNameOrTarget, "label="+optionText)
		time.sleep(env.ts-2)

	def selectOptionInDropDownList(self,myself,sel,fieldIdOrNameOrTarget,optionText):
		''' Select option in a drop down list field. '''

		time.sleep(env.ts)
		self.verifyElement(myself,sel,fieldIdOrNameOrTarget)
		sel.select(fieldIdOrNameOrTarget, "label="+optionText)
		time.sleep(env.ts)


	#===================================================================
	# 	Common basic functions (2) - Verify
	#===================================================================

	def verifyPageTitle(self,myself,sel, titleName):
		''' Verify page title is correct and ready. '''

		for i in range(60):
		    try:
		        if titleName == sel.get_title(): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.assertEqual(titleName, sel.get_title())
		except AssertionError, e: myself.verificationErrors.append(str(e))
	
	def verifyText(self,myself,sel,textContent):
		''' Verify the text is correct and ready. '''

		for i in range(60):
		    try:
		        if sel.is_text_present(textContent): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.failUnless(sel.is_text_present(textContent))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifyTextNotPresent(self,myself,sel,textContent):
		''' Verify the text is not present. '''

		for i in range(60):
		    try:
		        if not sel.is_text_present(textContent): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.failIf(sel.is_text_present(textContent))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifyTargetText(self,myself,sel,textContent,textTarget):
		''' Verify the text of a target is ready. '''

		for i in range(60):
		    try:
		        if textContent == sel.get_text(textTarget): break   # An example for 'textTarget': "css=h2"
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.assertEqual(textContent, sel.get_text(textTarget))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifyValue(self,myself,sel,textContent,fieldIdOrNameOrTarget):
		''' Verify the value of a text field is ready. '''

		for i in range(60):
		    try:
		        if textContent == sel.get_value(fieldIdOrNameOrTarget): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.assertEqual(textContent, sel.get_value(fieldIdOrNameOrTarget))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifyBtn(self,myself,sel,btnType,btnValue):
		''' Verify a button is present. '''

		self.verifyElement(myself,sel,"//input[@type='"+btnType+"' and @value='"+btnValue+"']")

	def verifyBtnNotPresent(self,myself,sel,btnType,btnValue):
		''' Verify a button is not present. '''

		self.verifyElementNotPresent(myself,sel,"//input[@type='"+btnType+"' and @value='"+btnValue+"']")

	def verifyLink(self,myself,sel,linkText):
		''' Verify a link is present. '''

		self.verifyElement(myself,sel,"link="+linkText)

	def verifyLinkNotPresent(self,myself,sel,linkText):
		''' Verify a link is not present. '''

		self.verifyElementNotPresent(myself,sel,"link="+linkText)

	def verifyElement(self,myself,sel,elementTarget):
		''' Verify the element is ready. '''

		for i in range(60):
		    try:
		        if sel.is_element_present(elementTarget): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.failUnless(sel.is_element_present(elementTarget))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifyElementNotPresent(self,myself,sel,elementTarget):
		''' Verify the element is not present. '''

		for i in range(60):
		    try:
		        if not sel.is_element_present(elementTarget): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.failIf(sel.is_element_present(elementTarget))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifySelectedLabel(self,myself,sel,labelText,fieldIdOrName,fieldTarget="<default>"):
		''' Verify the element is ready. '''

		elementTarget = ""
		if fieldIdOrName == "":
			if fieldTarget!="<default>":
				elementTarget=fieldTarget
		elif  fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
			elementTarget="//select[@id='"+fieldIdOrName+"']"
		elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
			elementTarget="//select[@id='"+fieldIdOrName+"']"
		else: elementTarget="//select[@name='"+fieldIdOrName+"']"

		for i in range(60):
		    try:
		        if labelText == sel.get_selected_label(elementTarget): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.assertEqual(labelText, sel.get_selected_label(elementTarget))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifySelectedLabels(self,myself,sel,labelTextList,fieldIdOrName,fieldTarget="<default>"):
		''' Verify the element is ready. '''

		elementTarget = ""
		if fieldIdOrName == "":
			if fieldTarget!="<default>":
				elementTarget=fieldTarget
		elif  fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
			elementTarget="//select[@id='"+fieldIdOrName+"']"
		elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
			elementTarget="//select[@id='"+fieldIdOrName+"']"
		else: elementTarget="//select[@name='"+fieldIdOrName+"']"

		if labelTextList=="":
			for i in range(60):
			    try:
				if not sel.is_something_selected(elementTarget): break
			    except: pass
			    time.sleep(1)
			else: myself.fail("time out")

		else:
			labelList=0
			for i in range(60):
			    try:
				labelList = sel.get_selected_labels(elementTarget)
				if len(labelList)>0: break
			    except: pass
			    time.sleep(1)
			else: myself.fail("time out")
			try: myself.failUnless(len(labelList)>0)
			except AssertionError, e: myself.verificationErrors.append(str(e))

			for checkLabel in labelTextList:
				for getLabel in labelList:
					if checkLabel == getLabel: break
				else: myself.fail("The option '"+checkLabel+"' is not selected.")

	def verifyCheckBox(self,myself,sel,onoff,fieldIdOrName,fieldValue,fieldTarget="<default>"):
		''' Verify if the check box checked or not. The value of onoff should be one of them: 'on' or 'off'. '''

		elementTarget = ""
		if fieldValue != "":
			if fieldIdOrName == "":
				elementTarget="//input[@value='"+fieldValue+"']"
			elif  fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
				elementTarget="//input[@id='"+fieldIdOrName+"' and @value='"+fieldValue+"']"
			elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
				elementTarget="//input[@id='"+fieldIdOrName[3:]+"' and @value='"+fieldValue+"']"
			else: elementTarget="//input[@name='"+fieldIdOrName+"' and @value='"+fieldValue+"']"
		else:
			if fieldIdOrName == "":
				if fieldTarget!="<default>":
					elementTarget=fieldTarget
			elif fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
				elementTarget="//input[@id='"+fieldIdOrName+"']"
			elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
				elementTarget="//input[@id='"+fieldIdOrName[3:]+"']"
			else: elementTarget="//input[@name='"+fieldIdOrName+"']"

		for i in range(60):
		    try:
		        if onoff == sel.get_value(elementTarget): break
		    except: pass
		    time.sleep(1)
		else: myself.fail("time out")
		try: myself.assertEqual(onoff, sel.get_value(elementTarget))
		except AssertionError, e: myself.verificationErrors.append(str(e))

	def verifyRadioBtn(self,myself,sel,onoff,fieldIdOrName,fieldValue,fieldTarget="<default>"):
		''' Verify if the radio button checked or not. The value of onoff should be one of them: 'on' or 'off'. '''
	
		#The process of verifying check box and radio btton is totally the same
		self.verifyCheckBox(myself,sel,onoff,fieldIdOrName,fieldValue,fieldTarget)


	#===================================================================
	# 	Common basic functions (3) - Assert
	#===================================================================

	def isPageTitle(self,myself,sel, titleName):
		''' To tell if the page title is present and correct. '''

		for i in range(5):
		    try:
		        if titleName == sel.get_title(): return True
		    except: pass
		    time.sleep(1)
		else: return False
	
	def isText(self,myself,sel,textContent):
		''' To tell if the text is present and correct. '''

		for i in range(5):
		    try:
		        if sel.is_text_present(textContent): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isTextNotPresent(self,myself,sel,textContent):
		''' To tell if the text is not present. '''

		for i in range(5):
		    try:
		        if not sel.is_text_present(textContent): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isTargetText(self,myself,sel,textContent,textTarget):
		''' To tell if the text of a target is present. '''

		for i in range(5):
		    try:
		        if textContent == sel.get_text(textTarget): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isValue(self,myself,sel,textContent,fieldIdOrNameOrTarget):
		''' To tell if the value of a text field is present. '''

		for i in range(5):
		    try:
		        if textContent == sel.get_value(fieldIdOrNameOrTarget): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isBtn(self,myself,sel,btnType,btnValue):
		''' To tell if the button is present. '''

		self.isElement(myself,sel,"//input[@type='"+btnType+"' and @value='"+btnValue+"']")

	def isBtnNotPresent(self,myself,sel,btnType,btnValue):
		''' To tell if the button is not present. '''

		self.isElementNotPresent(myself,sel,"//input[@type='"+btnType+"' and @value='"+btnValue+"']")

	def isLink(self,myself,sel,linkText):
		''' To tell if the link is present. '''

		return self.isElement(myself,sel,"link="+linkText)

	def isLinkNotPresent(self,myself,sel,linkText):
		''' To tell if the link is not present. '''

		self.isElementNotPresent(myself,sel,"link="+linkText)

	def isElement(self,myself,sel,elementTarget):
		''' To tell if the element is present. '''

		for i in range(5):
		    try:
		        if sel.is_element_present(elementTarget): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isElementNotPresent(self,myself,sel,elementTarget):
		''' To tell if the element is not present. '''

		for i in range(5):
		    try:
		        if not sel.is_element_present(elementTarget): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isSelectedLabel(self,myself,sel,labelText,fieldIdOrName,fieldTarget="<default>"):
		''' To tell if the Label is selected. '''

		elementTarget = ""
		if fieldIdOrName == "":
			if fieldTarget!="<default>":
				elementTarget=fieldTarget
		elif  fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
			elementTarget="//select[@id='"+fieldIdOrName+"']"
		elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
			elementTarget="//select[@id='"+fieldIdOrName+"']"
		else: elementTarget="//select[@name='"+fieldIdOrName+"']"

		for i in range(5):
		    try:
		        if labelText == sel.get_selected_label(elementTarget): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isCheckBox(self,myself,sel,onoff,fieldIdOrName,fieldValue,fieldTarget="<default>"):
		''' To tell if if the check box checked or not. The value of onoff should be one of them: 'on' or 'off'. '''

		elementTarget = ""
		if fieldValue != "":
			if fieldIdOrName == "":
				elementTarget="//input[@value='"+fieldValue+"']"
			elif  fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
				elementTarget="//input[@id='"+fieldIdOrName+"' and @value='"+fieldValue+"']"
			elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
				elementTarget="//input[@id='"+fieldIdOrName[3:]+"' and @value='"+fieldValue+"']"
			else: elementTarget="//input[@name='"+fieldIdOrName+"' and @value='"+fieldValue+"']"
		else:
			if fieldIdOrName == "":
				if fieldTarget!="<default>":
					elementTarget=fieldTarget
			elif fieldIdOrName.find('id_') != -1 and fieldIdOrName.find('id_') == 0:
				elementTarget="//input[@id='"+fieldIdOrName+"']"
			elif fieldIdOrName.find('ID:') != -1 and fieldIdOrName.find('ID:') == 0:
				elementTarget="//input[@id='"+fieldIdOrName[3:]+"']"
			else: elementTarget="//input[@name='"+fieldIdOrName+"']"

		for i in range(5):
		    try:
		        if onoff == sel.get_value(elementTarget): return True
		    except: pass
		    time.sleep(1)
		else: return False

	def isRadioBtn(self,myself,sel,onoff,fieldIdOrName,fieldValue,fieldTarget="<default>"):
		''' To tell if if the radio button checked or not. The value of onoff should be one of them: 'on' or 'off'. '''
	
		#The process of judging the check box and the radio btton is totally the same
		self.isCheckBox(myself,sel,onoff,fieldIdOrName,fieldValue,fieldTarget)


