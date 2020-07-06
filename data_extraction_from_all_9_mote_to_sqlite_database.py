import serial
import sqlite3
import datetime
import time
import re
z1data = serial.Serial("COM13", 115200)
def add_db(time,t1,t2,t3,t4,t5,t6,t7,t8,t9,dt):
    conn = sqlite3.connect('falsedata112.db')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS data(Time TEXT,Temperature48 TEXT,Temperature31 TEXT,Temperature54 TEXT, Temperature32 TEXT,Temperature71 TEXT,Temperature65 TEXT,Temperature78 TEXT,Temperature37 TEXT, Temperature76 TEXT, Date TEXT)""")

    c.execute("""INSERT INTO data (Time, Temperature48, Temperature31, Temperature54, Temperature32, Temperature71, Temperature65, Temperature78, Temperature37, Temperature76, Date) VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (time, t1, t2, t3, t4, t5, t6, t7, t8, t9, dt))
    conn.commit()
    c.close()
    conn.close()

while 1:
 
    data1 = z1data.readline().decode('utf-8')
    try:
        t1 = re.search('Node_id:48=(.+?)junk', data1).group(1)
    except AttributeError:
        t1 = ''
    try:
        t2 = re.search('Node_id:31=(.+?)junk',data1).group(1)
    except AttributeError:
        t2 = ''
    try:
        t3 = re.search('Node_id:54=(.+?)junk', data1).group(1)
    except AttributeError:
        t3 = ''
    try:
        t4 = re.search('Node_id:32=(.+?)junk',data1).group(1)
    except AttributeError:
        t4 = ''
    try:
        t5 = re.search('Node_id:71=(.+?)junk',data1).group(1)
    except AttributeError:
        t5 = ''
    try:
        t6 = re.search('Node_id:65=(.+?)junk',data1).group(1)
    except AttributeError:
        t6 = ''
    try:
        t7 = re.search('Node_id:78=(.+?)junk',data1).group(1)
    except AttributeError:
        t7 = ''
    try:
        t8 = re.search('Node_id:37=(.+?)junk',data1).group(1)
    except AttributeError:
        t8 = ''
    try:
        t9 = re.search('Node_id:76=(.+?)junk',data1).group(1)
    except AttributeError:
        t9 = ''
   
    

    
    mytime=datetime.datetime.now()
    tm ='{}:{}:{}'.format(mytime.hour,mytime.minute,mytime.second)
    dt='{}/{}/{}'.format(mytime.month,mytime.day,mytime.year)
    
    print(tm,str(t1),str(t2),str(t3),str(t4),str(t5),str(t6),str(t7),str(t8),str(t9),str(dt))
    add_db(tm,str(t1),str(t2),str(t3),str(t4),str(t5),str(t6),str(t7),str(t8),str(t9),str(dt))



 
