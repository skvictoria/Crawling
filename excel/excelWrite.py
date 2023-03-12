import xlsxwriter as xw

wb = xw.Workbook(r"구구단.xlsx")
ws = wb.add_worksheet("exercise sheet")

for j in range(2,10):
    for i in range (1,10):
        ws.write(0,j-2,f"{j}단")
        ws.write(i,j-2,j*i)

wb.close()   ## ws.close가 아니다.
