class InitValues():
    input_path = "DataInputFiles\\"
    output_path = "DataOutputFiles\\"
    merge_path = "MergeFiles\\"

    input_file_names = [
        # "Action_PriceList_2_1_2023_EN.csv",
        # "eeteuroparts.csv",
        "stock_export_full_for_zygimantas@ademi.lt.xml"
    ]

    merge_file_names =[
        f"{output_path}Action_PriceList_2_1_2023_EN.csv.mod.csv",
        f"{output_path}eeteuroparts.csv.mod.csv",
        f"{output_path}stock_export_full_for_zygimantas@ademi.lt.mod.xml"
    ]

    merge_file_name = f"{merge_path}MergeFile.mod.csv"
    filter_file_name = f"{merge_path}MergeFile.filter.csv"

    csv_header = [
        "EAN",
        "ITEM SKU",
        "PRODUCT NAME",
        "BRAND NAME",
        "REQUIRED PRICE TO AMAZON" 
    ]

    csv_action_pricelist_head = [
        "Manufacturer\'s code",
        "Name of product",
        "Producer",
        "EAN",
        "Net price EUR"
    ]

    csv_eeteuroparts_head = [
        "Item Nr",
        "Description",
        "Brand Name",
        "EAN/UPC",
        "Price"
    ]

    min_stock = 10
    min_price = 10
    threshold_price = 25.0
    low_increase_price = 1.4
    large_increase_price = 1.8



