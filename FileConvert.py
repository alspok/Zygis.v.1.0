from Classes.ModifyCSV import ModifyCSV
from Classes.MergeFiles import MergeFiles
from Classes.FilterCSV import FilterCSV
from Classes.InitValues import InitValues as iv

def FileConvert():
    ModifyCSV().actionPrice("Action_PriceList_2_1_2023_EN.csv")
    ModifyCSV().eeteuroparts("eeteuroparts.csv")
    ModifyCSV().stockExportFull("stock_export_full_for_zygimantas@ademi.lt.xml")


    # MergeFiles().mergeFiles()
    # FilterCSV().filterCSV()


if __name__ == "__main__":
    FileConvert()