# -*- coding: utf-8 -*- 
import xmlrpclib
from StaDev import StaDev
import time,os,sys,string
import getopt,csv

StaDevArray=[]
server_list=[]
period=0
interval=0
stop=0
mode=1
flag=''


#-p 每一轮的间隔时间 -i 不同优先级之间的间隔时间
if __name__=='__main__':

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hp:i:sm:", ["help","period=","interval=","stop=","mode="])
	except getopt.GetoptError:
		print "getopt error!"
	for o,a in opts:
		if o in ("-p","--period"):
			period=a
			print period
		elif o in ("-i","--interval"):
			interval=a
			print interval
		elif o in ("-m","--"):
			mode=a
			print mode
		elif o in ("-s","--stop"):
			stop=1
		


	f=open('./server_list.txt','r')
		while True:
			line=f.readline()
			if line and line.find('end')==-1:
				print line.strip()
				print "http://"+line.strip()+":28888"
				server_list.append(xmlrpclib.ServerProxy("http://"+line.strip()+":28888"))
			else:
				f.close()
				break 
	f.close()
	
	if mode == "1"
		f=open('./devices.csv','r')
		lines=f.readlines()
		for server in server_list:
			if stop==1:
				print 'stop dev'
				print server.stopDev()
			else:
				print 'start dev'
				print server.startDev(lines,period,interval,mode)
	elif mode == '2'
		f=open('./devices.csv','r')
		reader = csv.reader(f)
		#从配置文件读取设备信息，将其写入设备列表中
		for row in reader:
			StaDevArray.append(StaDev(row[0],row[1],row[2],row[3]),row[4],row[5])
		
		while True:
			
			for dev_entity in StaDevArray:
				if dev_entity.GetPriority()=='1':
					for server in server_list:
						print server.addDevice(dev_entity.GetId(),dev_entity.GetDevName(),dev_entity.GetPlayUrl(),dev_entity.GetPriority(),dev_entity.GetWifiSsid(),dev_entity.GetWifiPassword())
			
			time.sleep(string.atoi(interval))
			
			for dev_entity in StaDevArray:
				if dev_entity.GetPriority()=='2':
					for server in server_list:
						print server.addDevice(dev_entity.GetId(),dev_entity.GetDevName(),dev_entity.GetPlayUrl(),dev_entity.GetPriority(),dev_entity.GetWifiSsid(),dev_entity.GetWifiPassword())
					time.sleep(string.atoi(interval))
					
			time.sleep(string.atoi(period)*60)
			
			for dev_entity in StaDevArray:
				if dev_entity.GetPriority()=='2':
					for server in server_list:
						print server.stopDevice(dev_entity.GetId())
					time.sleep(string.atoi(interval))
					
			
			for dev_entity in StaDevArray:
				if dev_entity.GetPriority()=='1':
					for server in server_list:
						print server.stopDevice(dev_entity.GetId())
			
			time.sleep(20)
		
		
		