from selenium import selenium
import unittest, time, re

from env import *

#(Total: 81)
#Run1.BasicRun related test cases (total: 12)
import Run1.BasicRun.tc_ID84570_AddCaseForRun, Run1.BasicRun.tc_ID87372_CheckAutomaticallyInRun, Run1.BasicRun.tc_ID87374_ClickCaserunidOrNameInRun, Run1.BasicRun.tc_ID87377_ClickCaserunidOrNameMTimesInRun, Run1.BasicRun.tc_ID87381_ResetFilterItemInRun, Run1.BasicRun.tc_ID87382_UpdateSortNumForRun, Run1.BasicRun.tc_ID87426_CheckCaseNumInRun, Run1.BasicRun.tc_ID87429_AddMoreThanOneBugInRun, Run1.BasicRun.tc_ID87431_RemoveMoreThanOneBugInRun, Run1.BasicRun.tc_ID87433_AlterUnselectedCaseStatusInRun, Run1.BasicRun.tc_ID87436_AddRemoveMultiBugsInRun, Run1.BasicRun.tc_ID87437_AddRemoveInvalidBugInRun

#Run1.EditRun related test cases (total: 28)
import Run1.EditRun.tc_ID84445_AddCCInRun, Run1.EditRun.tc_ID84447_AddInvalidCCInRun, Run1.EditRun.tc_ID84448_AddLongNotesInRun, Run1.EditRun.tc_ID84449_AddLongTagWithSpeCharInRun, Run1.EditRun.tc_ID84450_AddPropertyInRun, Run1.EditRun.tc_ID84454_ChangeProdAndBuildInRun, Run1.EditRun.tc_ID84455_ChangeProdVersionInRun, Run1.EditRun.tc_ID84456_ChangeSummaryInRun, Run1.EditRun.tc_ID84457_ChangeSummaryToBlankInRun, Run1.EditRun.tc_ID84458_ChangeSumToLongWithSpeCharInRun, Run1.EditRun.tc_ID84459_ChangeSomeInfoInRun, Run1.EditRun.tc_ID84460_CheckFinishedInRun, Run1.EditRun.tc_ID84461_ClickBackAfterEditInRun, Run1.EditRun.tc_ID84462_UnCheckFinishedInRun, Run1.EditRun.tc_ID84464_EditEstTimeInRun, Run1.EditRun.tc_ID84465_EditNotesInRun, Run1.EditRun.tc_ID84466_EditPropertyInRun, Run1.EditRun.tc_ID84467_EditRunViaRunIdInRun, Run1.EditRun.tc_ID84468_EditRunViaRunNameInRun, Run1.EditRun.tc_ID84469_EditDefaultTesterInRun, Run1.EditRun.tc_ID84470_EditStatusToFinishedOrRunningInRun, Run1.EditRun.tc_ID84472_InputInvalidDefTesterInRun, Run1.EditRun.tc_ID84473_RemoveCCInRun, Run1.EditRun.tc_ID84474_RemovePropertyInRun, Run1.EditRun.tc_ID84475_RemoveTagInRun, Run1.EditRun.tc_ID84476_ResetEditAfterEditInRun, Run1.EditRun.tc_ID84477_CancelAddingPropertyInRun, Run1.EditRun.tc_ID84648_EditRunFromMyRuns

#Run1.RunResult related test cases (total: 30)
import Run1.RunResult.tc_ID84480_AnalysisResultCheckReportInRun, Run1.RunResult.tc_ID84481_AnalysisResultCheckShowAllBugsInRun, Run1.RunResult.tc_ID84538_MarkRunToRemoveComForCaseInRun, Run1.RunResult.tc_ID84541_MarkRunToBeBLOCKEDInRun, Run1.RunResult.tc_ID84542_MarkRunToBeERRORInRun, Run1.RunResult.tc_ID84543_MarkRunToBeFAILEDInRun, Run1.RunResult.tc_ID84544_MarkRunToBeIDLEInRun, Run1.RunResult.tc_ID84545_MarkRunToBePASSEDInRun, Run1.RunResult.tc_ID84546_MarkRunToBePAUSEDInRun, Run1.RunResult.tc_ID84547_MarkRunToBeRUNNINGInRun, Run1.RunResult.tc_ID84548_MarkRunToBeWAIVEDInRun, Run1.RunResult.tc_ID84551_RemoveCaseForRun, Run1.RunResult.tc_ID84553_UpdateCaseForRunWithoutCase, Run1.RunResult.tc_ID84555_AnalysisResultCheckBLOCKEDCaseInRun, Run1.RunResult.tc_ID84556_AnalysisResultCheckERRORCaseInRun, Run1.RunResult.tc_ID84557_AnalysisResultCheckFAILEDCaseInRun, Run1.RunResult.tc_ID84558_AnalysisResultCheckIDLECaseInRun, Run1.RunResult.tc_ID84559_AnalysisResultCheckPASSEDCaseInRun, Run1.RunResult.tc_ID84560_AnalysisResultCheckPAUSEDCaseInRun, Run1.RunResult.tc_ID84561_AnalysisResultCheckRUNNINGCaseInRun, Run1.RunResult.tc_ID84562_AnalysisResultCheckTOTALECaseInRun, Run1.RunResult.tc_ID84563_AnalysisResultCheckWAIVEDCaseInRun, Run1.RunResult.tc_ID87545_AnalysisResultCheckWAIVEDCaseReportInRun, Run1.RunResult.tc_ID87546_AnalysisResultCheckRUNNINGCaseReportInRun, Run1.RunResult.tc_ID87547_AnalysisResultCheckPAUSEDCaseReportInRun, Run1.RunResult.tc_ID87548_AnalysisResultCheckFAILEDCaseReportInRun, Run1.RunResult.tc_ID87549_AnalysisResultCheckIDLECaseReportInRun, Run1.RunResult.tc_ID87550_AnalysisResultCheckPASSEDCaseReportInRun, Run1.RunResult.tc_ID87551_AnalysisResultCheckERRORCaseReportInRun, Run1.RunResult.tc_ID87552_AnalysisResultCheckBLOCKEDCaseReportInRun

#Run1.SearchRun related test cases (total: 11)
import Run1.SearchRun.tc_ID84624_ResetSearchRun, Run1.SearchRun.tc_ID84625_ResetAfterSearchingRun, Run1.SearchRun.tc_ID84631_SearchRunByDefaultTester, Run1.SearchRun.tc_ID84633_SearchRunByManager, Run1.SearchRun.tc_ID84635_SearchRunByPlan, Run1.SearchRun.tc_ID84636_SearchRunByProdWithVer, Run1.SearchRun.tc_ID84637_SearchRunByProdWithoutVer, Run1.SearchRun.tc_ID84640_SearchRunBySpecialSummary, Run1.SearchRun.tc_ID84642_SearchRunByStatus, Run1.SearchRun.tc_ID84643_SearchRunBySummary, Run1.SearchRun.tc_ID84649_SearchMyRuns

def suite():

	suite = unittest.TestSuite()

	#Run1.BasicRun related test cases (total: 12)
	suite.addTest(Run1.BasicRun.tc_ID84570_AddCaseForRun.AddCaseForRun("test_AddCaseForRun"))
	suite.addTest(Run1.BasicRun.tc_ID87372_CheckAutomaticallyInRun.CheckAutomaticallyInRun("test_CheckAutomaticallyInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87374_ClickCaserunidOrNameInRun.ClickCaserunidOrNameInRun("test_ClickCaserunidOrNameInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87377_ClickCaserunidOrNameMTimesInRun.ClickCaserunidOrNameMTimesInRun("test_ClickCaserunidOrNameMTimesInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87381_ResetFilterItemInRun.ResetFilterItemInRun("test_ResetFilterItemInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87382_UpdateSortNumForRun.UpdateSortNumForRun("test_UpdateSortNumForRun"))
	suite.addTest(Run1.BasicRun.tc_ID87426_CheckCaseNumInRun.CheckCaseNumInRun("test_CheckCaseNumInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87429_AddMoreThanOneBugInRun.AddMoreThanOneBugInRun("test_AddMoreThanOneBugInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87431_RemoveMoreThanOneBugInRun.RemoveMoreThanOneBugInRun("test_RemoveMoreThanOneBugInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87433_AlterUnselectedCaseStatusInRun.AlterUnselectedCaseStatusInRun("test_AlterUnselectedCaseStatusInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87436_AddRemoveMultiBugsInRun.AddRemoveMultiBugsInRun("test_AddRemoveMultiBugsInRun"))
	suite.addTest(Run1.BasicRun.tc_ID87437_AddRemoveInvalidBugInRun.AddRemoveInvalidBugInRun("test_AddRemoveInvalidBugInRun"))

	#Run1.EditRun related test cases (total: 28)
	suite.addTest(Run1.EditRun.tc_ID84445_AddCCInRun.AddCCInRun("test_AddCCInRun"))
	suite.addTest(Run1.EditRun.tc_ID84447_AddInvalidCCInRun.AddInvalidCCInRun("test_AddInvalidCCInRun"))
	suite.addTest(Run1.EditRun.tc_ID84448_AddLongNotesInRun.AddLongNotesInRun("test_AddLongNotesInRun"))
	suite.addTest(Run1.EditRun.tc_ID84449_AddLongTagWithSpeCharInRun.AddLongTagWithSpeCharInRun("test_AddLongTagWithSpeCharInRun"))
	suite.addTest(Run1.EditRun.tc_ID84450_AddPropertyInRun.AddPropertyInRun("test_AddPropertyInRun"))
	suite.addTest(Run1.EditRun.tc_ID84454_ChangeProdAndBuildInRun.ChangeProdAndBuildInRun("test_ChangeProdAndBuildInRun"))
	suite.addTest(Run1.EditRun.tc_ID84455_ChangeProdVersionInRun.ChangeProdVersionInRun("test_ChangeProdVersionInRun"))
	suite.addTest(Run1.EditRun.tc_ID84456_ChangeSummaryInRun.ChangeSummaryInRun("test_ChangeSummaryInRun"))
	suite.addTest(Run1.EditRun.tc_ID84457_ChangeSummaryToBlankInRun.ChangeSummaryToBlankInRun("test_ChangeSummaryToBlankInRun"))
	suite.addTest(Run1.EditRun.tc_ID84458_ChangeSumToLongWithSpeCharInRun.ChangeSumToLongWithSpeCharInRun("test_ChangeSumToLongWithSpeCharInRun"))
	suite.addTest(Run1.EditRun.tc_ID84459_ChangeSomeInfoInRun.ChangeSomeInfoInRun("test_ChangeSomeInfoInRun"))
	suite.addTest(Run1.EditRun.tc_ID84460_CheckFinishedInRun.CheckFinishedInRun("test_CheckFinishedInRun"))
	suite.addTest(Run1.EditRun.tc_ID84461_ClickBackAfterEditInRun.ClickBackAfterEditInRun("test_ClickBackAfterEditInRun"))
	suite.addTest(Run1.EditRun.tc_ID84462_UnCheckFinishedInRun.UnCheckFinishedInRun("test_UnCheckFinishedInRun"))
	suite.addTest(Run1.EditRun.tc_ID84464_EditEstTimeInRun.EditEstTimeInRun("test_EditEstTimeInRun"))
	suite.addTest(Run1.EditRun.tc_ID84465_EditNotesInRun.EditNotesInRun("test_EditNotesInRun"))
	suite.addTest(Run1.EditRun.tc_ID84466_EditPropertyInRun.EditPropertyInRun("test_EditPropertyInRun"))
	suite.addTest(Run1.EditRun.tc_ID84467_EditRunViaRunIdInRun.EditRunViaRunIdInRun("test_EditRunViaRunIdInRun"))
	suite.addTest(Run1.EditRun.tc_ID84468_EditRunViaRunNameInRun.EditRunViaRunNameInRun("test_EditRunViaRunNameInRun"))
	suite.addTest(Run1.EditRun.tc_ID84469_EditDefaultTesterInRun.EditDefaultTesterInRun("test_EditDefaultTesterInRun"))
	suite.addTest(Run1.EditRun.tc_ID84470_EditStatusToFinishedOrRunningInRun.EditStatusToFinishedOrRunningInRun("test_EditStatusToFinishedOrRunningInRun"))
	suite.addTest(Run1.EditRun.tc_ID84472_InputInvalidDefTesterInRun.InputInvalidDefTesterInRun("test_InputInvalidDefTesterInRun"))
	suite.addTest(Run1.EditRun.tc_ID84473_RemoveCCInRun.RemoveCCInRun("test_RemoveCCInRun"))
	suite.addTest(Run1.EditRun.tc_ID84474_RemovePropertyInRun.RemovePropertyInRun("test_RemovePropertyInRun"))
	suite.addTest(Run1.EditRun.tc_ID84475_RemoveTagInRun.RemoveTagInRun("test_RemoveTagInRun"))
	suite.addTest(Run1.EditRun.tc_ID84476_ResetEditAfterEditInRun.ResetEditAfterEditInRun("test_ResetEditAfterEditInRun"))
	suite.addTest(Run1.EditRun.tc_ID84477_CancelAddingPropertyInRun.CancelAddingPropertyInRun("test_CancelAddingPropertyInRun"))
	suite.addTest(Run1.EditRun.tc_ID84648_EditRunFromMyRuns.EditRunFromMyRuns("test_EditRunFromMyRuns"))

	#Run1.RunResult related test cases (total: 30)
	suite.addTest(Run1.RunResult.tc_ID84480_AnalysisResultCheckReportInRun.AnalysisResultCheckReportInRun("test_AnalysisResultCheckReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID84481_AnalysisResultCheckShowAllBugsInRun.AnalysisResultCheckShowAllBugsInRun("test_AnalysisResultCheckShowAllBugsInRun"))
	suite.addTest(Run1.RunResult.tc_ID84538_MarkRunToRemoveComForCaseInRun.MarkRunToRemoveComForCaseInRun("test_MarkRunToRemoveComForCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84541_MarkRunToBeBLOCKEDInRun.MarkRunToBeBLOCKEDInRun("test_MarkRunToBeBLOCKEDInRun"))
	suite.addTest(Run1.RunResult.tc_ID84542_MarkRunToBeERRORInRun.MarkRunToBeERRORInRun("test_MarkRunToBeERRORInRun"))
	suite.addTest(Run1.RunResult.tc_ID84543_MarkRunToBeFAILEDInRun.MarkRunToBeFAILEDInRun("test_MarkRunToBeFAILEDInRun"))
	suite.addTest(Run1.RunResult.tc_ID84544_MarkRunToBeIDLEInRun.MarkRunToBeIDLEInRun("test_MarkRunToBeIDLEInRun"))
	suite.addTest(Run1.RunResult.tc_ID84545_MarkRunToBePASSEDInRun.MarkRunToBePASSEDInRun("test_MarkRunToBePASSEDInRun"))
	suite.addTest(Run1.RunResult.tc_ID84546_MarkRunToBePAUSEDInRun.MarkRunToBePAUSEDInRun("test_MarkRunToBePAUSEDInRun"))
	suite.addTest(Run1.RunResult.tc_ID84547_MarkRunToBeRUNNINGInRun.MarkRunToBeRUNNINGInRun("test_MarkRunToBeRUNNINGInRun"))
	suite.addTest(Run1.RunResult.tc_ID84548_MarkRunToBeWAIVEDInRun.MarkRunToBeWAIVEDInRun("test_MarkRunToBeWAIVEDInRun"))
	suite.addTest(Run1.RunResult.tc_ID84551_RemoveCaseForRun.RemoveCaseForRun("test_RemoveCaseForRun"))
	suite.addTest(Run1.RunResult.tc_ID84553_UpdateCaseForRunWithoutCase.UpdateCaseForRunWithoutCase("test_UpdateCaseForRunWithoutCase"))
	suite.addTest(Run1.RunResult.tc_ID84555_AnalysisResultCheckBLOCKEDCaseInRun.AnalysisResultCheckBLOCKEDCaseInRun("test_AnalysisResultCheckBLOCKEDCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84556_AnalysisResultCheckERRORCaseInRun.AnalysisResultCheckERRORCaseInRun("test_AnalysisResultCheckERRORCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84557_AnalysisResultCheckFAILEDCaseInRun.AnalysisResultCheckFAILEDCaseInRun("test_AnalysisResultCheckFAILEDCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84558_AnalysisResultCheckIDLECaseInRun.AnalysisResultCheckIDLECaseInRun("test_AnalysisResultCheckIDLECaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84559_AnalysisResultCheckPASSEDCaseInRun.AnalysisResultCheckPASSEDCaseInRun("test_AnalysisResultCheckPASSEDCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84560_AnalysisResultCheckPAUSEDCaseInRun.AnalysisResultCheckPAUSEDCaseInRun("test_AnalysisResultCheckPAUSEDCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84561_AnalysisResultCheckRUNNINGCaseInRun.AnalysisResultCheckRUNNINGCaseInRun("test_AnalysisResultCheckRUNNINGCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84562_AnalysisResultCheckTOTALECaseInRun.AnalysisResultCheckTOTALECaseInRun("test_AnalysisResultCheckTOTALECaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID84563_AnalysisResultCheckWAIVEDCaseInRun.AnalysisResultCheckWAIVEDCaseInRun("test_AnalysisResultCheckWAIVEDCaseInRun"))
	suite.addTest(Run1.RunResult.tc_ID87545_AnalysisResultCheckWAIVEDCaseReportInRun.AnalysisResultCheckWAIVEDCaseReportInRun("test_AnalysisResultCheckWAIVEDCaseReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID87546_AnalysisResultCheckRUNNINGCaseReportInRun.AnalysisResultCheckRUNNINGCaseReportInRun("test_AnalysisResultCheckRUNNINGCaseReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID87547_AnalysisResultCheckPAUSEDCaseReportInRun.AnalysisResultCheckPAUSEDCaseReportInRun("test_AnalysisResultCheckPAUSEDCaseReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID87548_AnalysisResultCheckFAILEDCaseReportInRun.AnalysisResultCheckFAILEDCaseReportInRun("test_AnalysisResultCheckFAILEDCaseReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID87549_AnalysisResultCheckIDLECaseReportInRun.AnalysisResultCheckIDLECaseReportInRun("test_AnalysisResultCheckIDLECaseReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID87550_AnalysisResultCheckPASSEDCaseReportInRun.AnalysisResultCheckPASSEDCaseReportInRun("test_AnalysisResultCheckPASSEDCaseReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID87551_AnalysisResultCheckERRORCaseReportInRun.AnalysisResultCheckERRORCaseReportInRun("test_AnalysisResultCheckERRORCaseReportInRun"))
	suite.addTest(Run1.RunResult.tc_ID87552_AnalysisResultCheckBLOCKEDCaseReportInRun.AnalysisResultCheckBLOCKEDCaseReportInRun("test_AnalysisResultCheckBLOCKEDCaseReportInRun"))

	#Run1.SearchRun related test cases (total: 11)
	suite.addTest(Run1.SearchRun.tc_ID84624_ResetSearchRun.ResetSearchRun("test_ResetSearchRun"))
	suite.addTest(Run1.SearchRun.tc_ID84625_ResetAfterSearchingRun.ResetAfterSearchingRun("test_ResetAfterSearchingRun"))
	suite.addTest(Run1.SearchRun.tc_ID84631_SearchRunByDefaultTester.SearchRunByDefaultTester("test_SearchRunByDefaultTester"))
	suite.addTest(Run1.SearchRun.tc_ID84633_SearchRunByManager.SearchRunByManager("test_SearchRunByManager"))
	suite.addTest(Run1.SearchRun.tc_ID84635_SearchRunByPlan.SearchRunByPlan("test_SearchRunByPlan"))
	suite.addTest(Run1.SearchRun.tc_ID84636_SearchRunByProdWithVer.SearchRunByProdWithVer("test_SearchRunByProdWithVer"))
	suite.addTest(Run1.SearchRun.tc_ID84637_SearchRunByProdWithoutVer.SearchRunByProdWithoutVer("test_SearchRunByProdWithoutVer"))
	suite.addTest(Run1.SearchRun.tc_ID84640_SearchRunBySpecialSummary.SearchRunBySpecialSummary("test_SearchRunBySpecialSummary"))
	suite.addTest(Run1.SearchRun.tc_ID84642_SearchRunByStatus.SearchRunByStatus("test_SearchRunByStatus"))
	suite.addTest(Run1.SearchRun.tc_ID84643_SearchRunBySummary.SearchRunBySummary("test_SearchRunBySummary"))
	suite.addTest(Run1.SearchRun.tc_ID84649_SearchMyRuns.SearchMyRuns("test_SearchMyRuns"))

	return suite

if __name__ == "__main__":
   unittest.main(defaultTest = 'suite')
