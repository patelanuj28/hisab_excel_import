from pylab import *
import MySQLdb

db_host = "127.0.0.1"
db_user = "root"
db_passwd = ""
db_database = "hisab"

conn = MySQLdb.connect(host=db_host,user=db_user,passwd=db_passwd,db=db_database)

cursor = conn.cursor()

query = """select u.name , round(sum(`individual_amount`),2) as give_anuj from individual i, transaction t, user u where i.user_id = u.id and i.transaction_id = t.id group by i.user_id """

res = cursor.execute(query)
data = cursor.fetchall()
#print(data)
Labels = list()
Individual = list()
for i in data:
	Labels.append(i[0])
	Individual.append(i[1])

cursor.close()
#conn.commit()
conn.close()
print Labels
print Individual

# make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

#labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
#fracs = [15,30,45, 10]
#print labels
#print fracs
explode=(0, 0.05, 0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,5)
pie(Individual, explode=explode, labels=Labels, autopct='%1.1f%%', shadow=True)
title('Hisab per head', bbox={'facecolor':'0.8', 'pad':5})

show()
