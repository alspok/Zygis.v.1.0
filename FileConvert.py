from Classes.ModifyCSV import ModifyCSV
from Classes.MergeFiles import MergeFiles
from Classes.FilterCSV import FilterCSV
from Classes.InitValues import InitValues as iv

def FileConvert():
    for file_name in iv.input_file_names:
        ModifyCSV().modifyCSV(file_name)

    MergeFiles().mergeFiles()
    FilterCSV().filterCSV()


if __name__ == "__main__":
    FileConvert()