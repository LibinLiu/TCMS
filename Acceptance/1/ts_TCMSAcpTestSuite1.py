from selenium import selenium
import unittest, time, re

from env import *

#(Total: 76)
#BasicInformation related test cases (total: 20)
import BasicInformation.tc_ID79133_InputDetailInformation, BasicInformation.tc_ID84222_ChooseIM, BasicInformation.tc_ID84223_InputAddress, BasicInformation.tc_ID84224_InputIM, BasicInformation.tc_ID84225_InputInvalidAddress, BasicInformation.tc_ID84226_InputInvalidIM, BasicInformation.tc_ID84227_InputInvalidName, BasicInformation.tc_ID84228_InputInvalidPhone, BasicInformation.tc_ID84229_InputLongAddress, BasicInformation.tc_ID84230_InputLongIM, BasicInformation.tc_ID84231_InputLongName, BasicInformation.tc_ID84232_InputLongNote, BasicInformation.tc_ID84233_InputLongPhone, BasicInformation.tc_ID84234_InputLongValidWebURL, BasicInformation.tc_ID84235_InputName, BasicInformation.tc_ID84236_InputNote, BasicInformation.tc_ID84237_InputNothing, BasicInformation.tc_ID84238_InputPhone, BasicInformation.tc_ID84239_InputWeb, BasicInformation.tc_ID84240_InputInvalidWebURL

#Batch related test cases (total: 1)
import Batch.tc_ID89853_BatchAddTagToCasesInPlan

#Bookmark related test cases (total: 5)
import Bookmark.tc_ID84214_DeleteBookmarksWithoutChoose, Bookmark.tc_ID84241_SingleClickBookmark, Bookmark.tc_ID84243_BookmarkThisPage, Bookmark.tc_ID84248_DeleteSeveralBookmarks, Bookmark.tc_ID84254_SubmitThisBookmark

#Case related test cases (total: 27)
import Case.tc_ID84394_AddBugInCase, Case.tc_ID84397_AddTagInCase, Case.tc_ID84399_AddCasesOfOtherPlan, Case.tc_ID84400_AddComponentInCase, Case.tc_ID84402_AddTagToSomeCases, Case.tc_ID84403_VerifyCaseRunListInCase, Case.tc_ID84407_EditAutomated, Case.tc_ID84412_EditPriority, Case.tc_ID84413_EditStatus, Case.tc_ID84414_RemoveBugInCase, Case.tc_ID84415_RemoveTagInCase, Case.tc_ID84417_RemoveComponentInCase, Case.tc_ID84420_RemoveTagFromSomeCases, Case.tc_ID84424_RemoveCases, Case.tc_ID84431_PrintCasesInPlan, Case.tc_ID84441_SetConfirmed, Case.tc_ID84442_SetDisable, Case.tc_ID84443_SetNeedUpdate, Case.tc_ID84444_SetProposed, Case.tc_ID84533_AddCaseForRun, Case.tc_ID87274_AddSeveralTagsToSomeCases, Case.tc_ID87286_AddCommentForReviewingCase, Case.tc_ID87287_RemoveCommentForReviewingCase, Case.tc_ID87345_AddPlanToCase, Case.tc_ID87362_RemoveNoComponentInCase, Case.tc_ID87379_ExpandAllCasesInRun, Case.tc_ID87567_ChangeCaseSortNumToNoneInPlan

#Environment related test cases (total: 1)
import Environment.tc_ID84653_AddEnvironmentGroup

#Homepage related test cases (total: 1)
import Homepage.tc_ID86708_ReleaseSchedule

#Management related test cases (total: 1)
import Management.tc_ID84698_AddBuild

#Report related test cases (total: 9)
import Report.tc_ID93888_SelectOneBuildAndByCaseRunTester, Report.tc_ID93889_SelectMoreBuildsAndByCaseRunTester, Report.tc_ID93890_SelectNoBuildAndByCaseRunTester, Report.tc_ID93891_SelectMoreBuildsAndByCasePriority, Report.tc_ID93892_SelectOneBuildAndByCasePriority, Report.tc_ID93893_SelectNoBuildAndByCasePriority, Report.tc_ID93894_SelectOneBuildAndByPlanTag, Report.tc_ID93895_SelectMoreBuildsAndByPlanTag, Report.tc_ID93896_SelectNoBuildAndByPlanTag

#Run related test cases (total: 8)
import Run.tc_ID84452_AddTagForRun, Run.tc_ID84580_CreateRunInPlan, Run.tc_ID84588_CreateLongNameRunInPlan, Run.tc_ID87375_OpenCaseFromRun, Run.tc_ID87379_ExpColCaseInRun, Run.tc_ID87380_FilterCaseInRun, Run.tc_ID87427_AlterCaseRunStatusInRun, Run.tc_ID87432_AddComForCaseInRun

#TreeView related test cases (total: 3)
import TreeView.tc_ID84371_AddChildNode, TreeView.tc_ID84372_ChangeParentNode, TreeView.tc_ID84374_CreateParentNode

def suite():

	suite = unittest.TestSuite()

	#BasicInformation related test cases (total: 20)
	suite.addTest(BasicInformation.tc_ID79133_InputDetailInformation.InputDetailInformation("test_InputDetailInformation"))
	suite.addTest(BasicInformation.tc_ID84222_ChooseIM.ChooseIM("test_ChooseIM"))
	suite.addTest(BasicInformation.tc_ID84223_InputAddress.InputAddress("test_InputAddress"))
	suite.addTest(BasicInformation.tc_ID84224_InputIM.InputIM("test_InputIM"))
	suite.addTest(BasicInformation.tc_ID84225_InputInvalidAddress.InputInvalidAddress("test_InputInvalidAddress"))
	suite.addTest(BasicInformation.tc_ID84226_InputInvalidIM.InputInvalidIM("test_InputInvalidIM"))
	suite.addTest(BasicInformation.tc_ID84227_InputInvalidName.InputInvalidName("test_InputInvalidName"))
	suite.addTest(BasicInformation.tc_ID84228_InputInvalidPhone.InputInvalidPhone("test_InputInvalidPhone"))
	suite.addTest(BasicInformation.tc_ID84229_InputLongAddress.InputLongAddress("test_InputLongAddress"))
	suite.addTest(BasicInformation.tc_ID84230_InputLongIM.InputLongIM("test_InputLongIM"))
	suite.addTest(BasicInformation.tc_ID84231_InputLongName.InputLongName("test_InputLongName"))
	suite.addTest(BasicInformation.tc_ID84232_InputLongNote.InputLongNote("test_InputLongNote"))
	suite.addTest(BasicInformation.tc_ID84233_InputLongPhone.InputLongPhone("test_InputLongPhone"))
	suite.addTest(BasicInformation.tc_ID84234_InputLongValidWebURL.InputLongValidWebURL("test_InputLongValidWebURL"))
	suite.addTest(BasicInformation.tc_ID84235_InputName.InputName("test_InputName"))
	suite.addTest(BasicInformation.tc_ID84236_InputNote.InputNote("test_InputNote"))
	suite.addTest(BasicInformation.tc_ID84237_InputNothing.InputNothing("test_InputNothing"))
	suite.addTest(BasicInformation.tc_ID84238_InputPhone.InputPhone("test_InputPhone"))
	suite.addTest(BasicInformation.tc_ID84239_InputWeb.InputWeb("test_InputWeb"))
	suite.addTest(BasicInformation.tc_ID84240_InputInvalidWebURL.InputInvalidWebURL("test_InputInvalidWebURL"))

	#Batch related test cases (total: 1)
	suite.addTest(Batch.tc_ID89853_BatchAddTagToCasesInPlan.BatchAddTagToCasesInPlan("test_BatchAddTagToCasesInPlan"))

	#Bookmark related test cases (total: 5)
	suite.addTest(Bookmark.tc_ID84214_DeleteBookmarksWithoutChoose.DeleteBookmarksWithoutChoose("test_DeleteBookmarksWithoutChoose"))
	suite.addTest(Bookmark.tc_ID84241_SingleClickBookmark.SingleClickBookmark("test_SingleClickBookmark"))
	suite.addTest(Bookmark.tc_ID84243_BookmarkThisPage.BookmarkThisPage("test_BookmarkThisPage"))
	suite.addTest(Bookmark.tc_ID84248_DeleteSeveralBookmarks.DeleteSeveralBookmarks("test_DeleteSeveralBookmarks"))
	suite.addTest(Bookmark.tc_ID84254_SubmitThisBookmark.SubmitThisBookmark("test_SubmitThisBookmark"))

	#Case related test cases (total: 27)
	suite.addTest(Case.tc_ID84394_AddBugInCase.AddBugInCase("test_AddBugInCase"))
	suite.addTest(Case.tc_ID84397_AddTagInCase.AddTagInCase("test_AddTagInCase"))
	suite.addTest(Case.tc_ID84399_AddCasesOfOtherPlan.AddCasesOfOtherPlan("test_AddCasesOfOtherPlan"))
	suite.addTest(Case.tc_ID84400_AddComponentInCase.AddComponentInCase("test_AddComponentInCase"))
	suite.addTest(Case.tc_ID84402_AddTagToSomeCases.AddTagToSomeCases("test_AddTagToSomeCases"))
	suite.addTest(Case.tc_ID84403_VerifyCaseRunListInCase.VerifyCaseRunListInCase("test_VerifyCaseRunListInCase"))
	suite.addTest(Case.tc_ID84407_EditAutomated.EditAutomated("test_EditAutomated"))
	suite.addTest(Case.tc_ID84412_EditPriority.EditPriority("test_EditPriority"))
	suite.addTest(Case.tc_ID84413_EditStatus.EditStatus("test_EditStatus"))
	suite.addTest(Case.tc_ID84414_RemoveBugInCase.RemoveBugInCase("test_RemoveBugInCase"))
	suite.addTest(Case.tc_ID84415_RemoveTagInCase.RemoveTagInCase("test_RemoveTagInCase"))
	suite.addTest(Case.tc_ID84417_RemoveComponentInCase.RemoveComponentInCase("test_RemoveComponentInCase"))
	suite.addTest(Case.tc_ID84420_RemoveTagFromSomeCases.RemoveTagFromSomeCases("test_RemoveTagFromSomeCases"))
	suite.addTest(Case.tc_ID84424_RemoveCases.RemoveCases("test_RemoveCases"))
	suite.addTest(Case.tc_ID84431_PrintCasesInPlan.PrintCasesInPlan("test_PrintCasesInPlan"))
	suite.addTest(Case.tc_ID84441_SetConfirmed.SetConfirmed("test_SetConfirmed"))
	suite.addTest(Case.tc_ID84442_SetDisable.SetDisable("test_SetDisable"))
	suite.addTest(Case.tc_ID84443_SetNeedUpdate.SetNeedUpdate("test_SetNeedUpdate"))
	suite.addTest(Case.tc_ID84444_SetProposed.SetProposed("test_SetProposed"))
	suite.addTest(Case.tc_ID84533_AddCaseForRun.AddCaseForRun("test_AddCaseForRun"))
	suite.addTest(Case.tc_ID87274_AddSeveralTagsToSomeCases.AddSeveralTagsToSomeCases("test_AddSeveralTagsToSomeCases"))
	suite.addTest(Case.tc_ID87286_AddCommentForReviewingCase.AddCommentForReviewingCase("test_AddCommentForReviewingCase"))
	suite.addTest(Case.tc_ID87287_RemoveCommentForReviewingCase.RemoveCommentForReviewingCase("test_RemoveCommentForReviewingCase"))
	suite.addTest(Case.tc_ID87345_AddPlanToCase.AddPlanToCase("test_AddPlanToCase"))
	suite.addTest(Case.tc_ID87362_RemoveNoComponentInCase.RemoveNoComponentInCase("test_RemoveNoComponentInCase"))
	suite.addTest(Case.tc_ID87379_ExpandAllCasesInRun.ExpandAllCasesInRun("test_ExpandAllCasesInRun"))
	suite.addTest(Case.tc_ID87567_ChangeCaseSortNumToNoneInPlan.ChangeCaseSortNumToNoneInPlan("test_ChangeCaseSortNumToNoneInPlan"))

	#Environment related test cases (total: 1)
	suite.addTest(Environment.tc_ID84653_AddEnvironmentGroup.AddEnvironmentGroup("test_AddEnvironmentGroup"))

	#Homepage related test cases (total: 1)
	suite.addTest(Homepage.tc_ID86708_ReleaseSchedule.ReleaseSchedule("test_ReleaseSchedule"))

	#Management related test cases (total: 1)
	suite.addTest(Management.tc_ID84698_AddBuild.AddBuild("test_AddBuild"))

	#Report related test cases (total: 9)
	suite.addTest(Report.tc_ID93888_SelectOneBuildAndByCaseRunTester.SelectOneBuildAndByCaseRunTester("test_SelectOneBuildAndByCaseRunTester"))
	suite.addTest(Report.tc_ID93889_SelectMoreBuildsAndByCaseRunTester.SelectMoreBuildsAndByCaseRunTester("test_SelectMoreBuildsAndByCaseRunTester"))
	suite.addTest(Report.tc_ID93890_SelectNoBuildAndByCaseRunTester.SelectNoBuildAndByCaseRunTester("test_SelectNoBuildAndByCaseRunTester"))
	suite.addTest(Report.tc_ID93891_SelectMoreBuildsAndByCasePriority.SelectMoreBuildsAndByCasePriority("test_SelectMoreBuildsAndByCasePriority"))
	suite.addTest(Report.tc_ID93892_SelectOneBuildAndByCasePriority.SelectOneBuildAndByCasePriority("test_SelectOneBuildAndByCasePriority"))
	suite.addTest(Report.tc_ID93893_SelectNoBuildAndByCasePriority.SelectNoBuildAndByCasePriority("test_SelectNoBuildAndByCasePriority"))
	suite.addTest(Report.tc_ID93894_SelectOneBuildAndByPlanTag.SelectOneBuildAndByPlanTag("test_SelectOneBuildAndByPlanTag"))
	suite.addTest(Report.tc_ID93895_SelectMoreBuildsAndByPlanTag.SelectMoreBuildsAndByPlanTag("test_SelectMoreBuildsAndByPlanTag"))
	suite.addTest(Report.tc_ID93896_SelectNoBuildAndByPlanTag.SelectNoBuildAndByPlanTag("test_SelectNoBuildAndByPlanTag"))

	#Run related test cases (total: 8)
	suite.addTest(Run.tc_ID84452_AddTagForRun.AddTagForRun("test_AddTagForRun"))
	suite.addTest(Run.tc_ID84580_CreateRunInPlan.CreateRunInPlan("test_CreateRunInPlan"))
	suite.addTest(Run.tc_ID84588_CreateLongNameRunInPlan.CreateLongNameRunInPlan("test_CreateLongNameRunInPlan"))
	suite.addTest(Run.tc_ID87375_OpenCaseFromRun.OpenCaseFromRun("test_OpenCaseFromRun"))
	suite.addTest(Run.tc_ID87379_ExpColCaseInRun.ExpColCaseInRun("test_ExpColCaseInRun"))
	suite.addTest(Run.tc_ID87380_FilterCaseInRun.FilterCaseInRun("test_FilterCaseInRun"))
	suite.addTest(Run.tc_ID87427_AlterCaseRunStatusInRun.AlterCaseRunStatusInRun("test_AlterCaseRunStatusInRun"))
	suite.addTest(Run.tc_ID87432_AddComForCaseInRun.AddComForCaseInRun("test_AddComForCaseInRun"))

	#TreeView related test cases (total: 3)
	suite.addTest(TreeView.tc_ID84371_AddChildNode.AddChildNode("test_AddChildNode"))
	suite.addTest(TreeView.tc_ID84372_ChangeParentNode.ChangeParentNode("test_ChangeParentNode"))
	suite.addTest(TreeView.tc_ID84374_CreateParentNode.CreateParentNode("test_CreateParentNode"))

	return suite

if __name__ == "__main__":   unittest.main(defaultTest = 'suite')