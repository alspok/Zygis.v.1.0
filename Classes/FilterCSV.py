import csv
from Classes.InitValues import InitValues as iv

class FilterCSV():

    def filterCSV(self) -> None:
        with open(iv.merge_file_name, mode='r', encoding='utf-8') as mfh:
            dictReader_obj = csv.DictReader(mfh)

            fsub_dict_list = []
            fean_list = []
            for item in dictReader_obj:
                if item['EAN'] not in fean_list:
                    fsub_dict_list.append(item)
                    fean_list.append(item['EAN'])
                else:
                    continue
        
        with open(iv.filter_file_name, mode='w', encoding='utf-8', newline='') as fcsv_fh:
            writer = csv.DictWriter(fcsv_fh, fieldnames=iv.csv_header)
            writer.writeheader()
            writer.writerows(fsub_dict_list)

        pass