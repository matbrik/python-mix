import xlsxwriter

workbook = xlsxwriter.Workbook(r'C:\Users\matbr\Source\Repos\python-mix\Python Mix\Python Mix\BuoniMatteo.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Hello world')
workbook.close()
