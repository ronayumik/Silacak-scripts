import pymssql

connectstring = 'mssql+pyodbc://sa:ar4rfv.@10.199.14.30/pelacakan'
connectstring2 = 'DRIVER={ODBC Driver 13 for SQL Server};SERVER=10.199.14.30;DATABASE=pelacakan;UID=sa;PWD=ar4rfv.'
cnxn = pymssql.connect(host='10.199.14.30', user='sa', password='ar4rfv.',database='pelacakan')
cursor = cnxn.cursor()

# SET NOCOUNT ON should be added to prevent errors thrown by cursor

sql='select pub_judul from publikasi_dosen'

cursor.execute(sql)
print cursor.fetchone()

# print result.fetchall()

# result.nextset()
# print result.fetchall()
# result.nextset()
# print result.fetchall()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      