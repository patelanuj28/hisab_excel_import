

from xlrd import open_workbook, cellname
import MySQLdb

db_host = "127.0.0.1"
db_user = "root"
db_passwd = ""
db_database = "hisab_oct_dec"


file_to_import = "files/oct/all.xls"

column_count=2

book = open_workbook(file_to_import)
no_of_sheet = book.sheet_names()

conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_passwd,db=db_database)
cursor = conn.cursor()
query = """insert into transaction  (id, bank_name, tran_date, description, amount) values (%s, %s, %s, %s, %s)"""
j = 1
for i in no_of_sheet:
	#sheet = book.sheet_loaded(i)
	sheet = book.sheet_by_name(i)
	print "Workbook Sheet Name : %s" % i
	print "Number of rows in sheet : %s " % sheet.nrows
	for row_index in range(sheet.nrows):
		bank_name = i
		tran_date = sheet.cell(row_index,0).value
		description = sheet.cell(row_index,1).value
		amount = sheet.cell(row_index,2).value

		values = (j, bank_name, tran_date, description, amount)
		res = cursor.execute(query,values)
		j = j+1

	print "\n\n"
	#j = j+1





#for row_index in range(sheet.nrows):
#	row_num = row_index
#	user_id = sheet.cell(row_index, 0).value
#	user_name = sheet.cell(row_index,1).value
#
#	values = (user_name)
#
#	res = cursor.execute(query, values)



cursor.close()
conn.commit()
conn.close()


