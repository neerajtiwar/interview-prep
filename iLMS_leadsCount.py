import psycopg2
import os
import sys
import datetime

def CountLeads():
	x = datetime.datetime.now()
	y = x - datetime.timedelta(minutes=60)
	starttime = x.strftime('%d %b %Y %H:%M:%S')
	endtime = y.strftime('%d %b %Y %H:%M:%S')

	connection = psycopg2.connect(user = "konnectmanager",password = "konnectAirtel2014@)!$",host = "10.5.244.243",port = "5431",database = "konnect")
	cur = connection.cursor()
	cur.execute("select count(id) from g.datainterfacelog where request->>'receivedFrom'='ilms' and request->>'appId'='app2' and requesttime>starttime and requesttime<endtime;")
	app2Data = cur.fetchall()
	cur.execute("select count(id) from g.datainterfacelog where request->>'receivedFrom'='ilms' and request->>'appId'='app3' and requesttime>starttime and requesttime<endtime;")
	app3Data = cur.fetchall()
	cur.execute("select count(id) from g.datainterfacelog where request->>'receivedFrom'='ilms' and request->>'appId'='app14' and requesttime>starttime and requesttime<endtime;")
    app4Data = cur1.fetchall()
    totalhits = (app2Data + app3Data + app4Data)
    print(totalhits)
    return totalhits
    cur.close()
    connection.close()

if __name__ == '__main__':
	leads = CountLeads()
	print(f"Total hits receivedFrom iLms are {leads}")