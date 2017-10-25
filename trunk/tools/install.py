import os,sys,time
sys.path.append("../")
from am import AndroidAm

if __name__=='__main__':
	am=AndroidAm()
	
	os.system("adb devices > device_t")
	
	f=open('./device_t','r')
	for line in iter(f):
		if line.find("List")==-1 and line.find('device')!=-1:
			dev_id=line.split()[0]
			print dev_id
			am.installApk(dev_id,sys.argv[1])
	time.sleep(5)
	f.close()
	os.system("del device_t")