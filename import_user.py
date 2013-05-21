

from xlrd import open_workbook, cellname
import MySQLdb

db_host = "127.0.0.1"
db_user = "root"
db_passwd = ""
db_database = "hisab"


file_to_import = "files/user.xls"

column_count=2

book = open_workbook(file_to_import)
sheet = book.sheet_by_index(0)

print "Workbook Sheet Name : %s" % sheet.name
print "Number of rows in sheet : %s " % sheet.nrows


conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_passwd,db=db_database)

cursor = conn.cursor()

query = """insert into user (id, name) values (%s, %s)"""

for row_index in range(sheet.nrows):
	row_num = row_index
	user_id = sheet.cell(row_index, 0).value
	user_name = sheet.cell(row_index,1).value

	values = (row_num+1, user_name)

	res = cursor.execute(query, values)



cursor.close()
conn.commit()
conn.close()


