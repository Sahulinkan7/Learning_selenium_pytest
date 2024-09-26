import openpyxl
from openpyxl import Workbook

## writing data to excel file 
workbook=Workbook()
workbook.create_sheet("Data")

workbook.save("testdata.xlsx")

filepath="./testdata.xlsx"

workbook=openpyxl.load_workbook(filepath)