from Classes.InitValues import  InitValues as iv

class MergeFiles():

    def mergeFiles(self) -> None:
        file_count = True
        for file in iv.merge_file_names:
            if file_count:
                with open(file, mode='r', encoding='utf-8') as fh, open(iv.merge_file_name, mode='w', encoding='utf-8') as mfh:
                    mfile = fh.read()
                    mfh.write(mfile)
                    file_count = False
            else:
                with open(file, mode='r', encoding='utf-8') as fh, open(iv.merge_file_name, mode='a', encoding='utf-8', newline='') as mfh:
                    for line in fh:
                        if "ITEM SKU" in line and "BRAND NAME" in line:
                            continue
                        else:
                            mfh.write(line)
        
        pass