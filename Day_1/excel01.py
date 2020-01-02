#Tulis excel
import xlsxwriter
#python -m pip install xlsxwriter
file = xlsxwriter.Workbook('chartlagu.xlsx')
sheet = file.add_worksheet('ChartLagu')
sheet.write(0,0, 'Artist') #row, col, data
sheet.write(0,1, 'Tittle')
sheet.write(0,2, 'Position')
sheet.write(1,0, "NU'EST")
sheet.write(1,1, "LOVE ME")
sheet.write(1,2, 1)
file.close()