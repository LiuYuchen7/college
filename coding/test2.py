import socket  #导入socket模块
import time #导入time模块

import datetime
      #server 接收端
      # 设置服务器默认端口号
PORT = 8888
PORT2=66
      # 创建一个套接字socket对象，用于进行通讯
      # socket.AF_INET 指明使用INET地址集，进行网间通讯
      # socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("10.2.44.222", PORT)
address2 = ("10.2.44.222", PORT2)
server_socket.bind(address)  # 为服务器绑定一个固定的地址，ip和端口
server_socket2.bind(address2)
server_socket.settimeout(10)  #设置一个时间提示，如果10秒钟没接到数据进行提示
data1=0.0
data2=0.0
data3=0.0
data4=0.0
import sqlite3

conn = sqlite3.connect('bishe.db')
c = conn.cursor()
print ("数据库打开成功")

c.execute("DROP TABLE COMPANY ")
conn.commit()
c.execute('''CREATE TABLE COMPANY
       (ID INT    NOT NULL,
       ChannelOne           FLOAT    NOT NULL,
       ChannelTwo            FLOAT     NOT NULL,
       ChannelThree        FLOAT  NOT NULL,
       ChannelFour           FLOAT   NOT NULL,
       TIME                FLOAT    NOT NULL);''')
conn.commit()
id=0
time1 = '2'
while True:

  try:
      now = time.time()  #获取当前时间

				      # 接收客户端传来的数据 recvfrom接收客户端的数据，默认是阻塞的，直到有客户端传来数据
				      # recvfrom 参数的意义，表示最大能接收多少数据，单位是字节
				      # recvfrom返回值说明
				      # receive_data表示接受到的传来的数据,是bytes类型
				      # client  表示传来数据的客户端的身份信息，客户端的ip和端口，元组

      # receive_data, client = server_socket.recvfrom(1024)
      server_socket=eval('server_socket'+time1)
      receive_data2, client2 = server_socket.recvfrom(1024)
      print(receive_data2)
      #print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now))) #以指定格式显示时间
      receive_data=receive_data.decode()
      print("来自客户端%s,发送的%s" % (client, receive_data))  #打印接收的内容
      data1=(float(receive_data[0:15]))
      data2=(float(receive_data[16:31]))
      data3=(float(receive_data[32:47]))
      data4=(float(receive_data[48:63]))
      dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
      #c.execute("INSERT INTO COMPANY  VALUES (0, data1, data2, data3, data4, dt_ms)")
      c.execute("insert into COMPANY (id,channelone,channeltwo,channelthree,channelfour,time) VALUES (?,?,?,?,?,?)", (id, data1,data2,data3,data4,dt_ms))
      id+=1
      #print(data2)
      conn.commit()
  except socket.timeout:  #如果10秒钟没有接收数据进行提示（打印 "time out"）
      print ("tme out")

conn.commit()
print ("数据插入成功")
conn.close()