import csv
import xmltodict
import pprint
from Classes.InitValues import InitValues as iv
from xml.etree import ElementTree


class ModifyCSV():

    def modifyCSV(self, file_name: str) -> None:
        #File to modify DataInputFiles\Action_PriceList_2_1_2023_EN.csv
        if "Action_PriceList" in file_name:
            with open(f"{iv.input_path}{file_name}", mode='r', encoding='utf-8') as csv_fh:
                dictReader_obj = csv.DictReader(csv_fh)
                sub_dict_list = []
                for item in dictReader_obj:
                    if float(item['Net price EUR']) >= iv.min_price:
                        sub_dict_list.append(item)

            msub_dict_list = []
            for item in sub_dict_list:
                sub_dict = {}
                if item['EAN'] == '':
                    continue
                else:
                    sub_dict['EAN'] = int(item['EAN'])

                sub_dict['ITEM SKU'] = item['Manufacturer\'s code']
                sub_dict['PRODUCT NAME'] = item['Name of product']
                sub_dict['BRAND NAME'] = item['Producer']

                if float(item['Net price EUR']) <= iv.threshold_price:
                    sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['Net price EUR']) * iv.large_increase_price, 2)
                else:
                    sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item['Net price EUR']) * iv.low_increase_price, 2)
                
                msub_dict_list.append(sub_dict)

            with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
                writer = csv.DictWriter(tcsv_fh, fieldnames=iv.csv_header)
                writer.writeheader()
                writer.writerows(msub_dict_list)
        
        #Filie to modify DataInputFiles\eeteuroparts.csv
        elif "eeteuroparts" in file_name:
            with open(f"{iv.input_path}{file_name}", mode='r') as ssv_fh, \
                 open(f"{iv.output_path}{file_name}.temp.csv", mode='w', encoding='utf-8') as csv_fh:
                for line in ssv_fh:
                    # mod_line = line.replace('\";\"', ',')
                    mod_line = line.replace(',', '.').replace(';', ',')
                    csv_fh.write(mod_line)

            with open(f"{iv.output_path}{file_name}.temp.csv", mode='r', encoding='utf-8') as ssv_fh:
                dictReader_obj = csv.DictReader(ssv_fh)
                sub_dict_list = []
                for item in dictReader_obj:
                    if float(item['Price']) >= iv.min_price:
                        sub_dict_list.append(item)

            msub_dict_list = []
            for item in sub_dict_list:
                sub_dict = {}
                if item['EAN/UPC'] == '':
                    continue
                else:
                    sub_dict['EAN'] = int(item["EAN/UPC"])

                sub_dict['ITEM SKU'] = item["Item Nr"]
                sub_dict['PRODUCT NAME'] = item["Description"]
                sub_dict['BRAND NAME'] = item["Brand Name"]
                if float(item['Price']) <= float(iv.threshold_price):
                    sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item["Price"]) * iv.large_increase_price, 2)
                else:
                    sub_dict['REQUIRED PRICE TO AMAZON'] = round(float(item["Price"]) * iv.low_increase_price, 2)
                msub_dict_list.append(sub_dict)

            with open(f"{iv.output_path}{file_name}.mod.csv", mode='w', encoding='utf-8', newline='') as tcsv_fh:
                writer = csv.DictWriter(tcsv_fh, fieldnames=iv.csv_header)
                writer.writeheader()
                writer.writerows(msub_dict_list)

        # xml file to modify
        elif "ademi.lt.xml" in file_name:
            with open(file_name, mode='r', encoding='utf-8') as xml_fh:
                xml_date = xml_fh.read()

            xml_dict = xmltodict.parse(xml_date)

            xml_dict_list =[]
            [xml_dict_list.append(dict(x)) for x in xml_dict['offer']['products']['product']]
            for item in xml_dict_list:
                pprint.pprint(item)

        else:
            print(f"No file {file_name} in directory")
    pass