
import os,sys,time

class AndroidAm():
	def startBrowser(self,url,dev_n):
		cmd_line = "adb -s "+dev_n+" shell am start -n com.android.browser/com.android.browser.BrowserActivity "+url 
 		os.system(cmd_line)
	def stopBrowser(self,dev_n):
		cmd_line = "adb -s "+dev_n+" shell am force-stop com.android.browser"
		os.system(cmd_line)
	def startPlayer(self,url,dev_n):
		cmd_line = "adb -s "+dev_n+" shell am start -n org.crazyit.sound/org.crazyit.sound.VedioViewTest -d "+url
		os.system(cmd_line)
	def stopPlayer(self,dev_n):
		cmd_line = "adb -s "+dev_n+" shell am force-stop org.crazyit.sound"
		os.system(cmd_line)
	def startEndpoint(self,dev_n):
		cmd_line2 = "adb -s "+dev_n+" shell am force-stop com.ixia.ixchariot"
		os.system(cmd_line2)
		time.sleep(5)
		cmd_line = "adb -s "+dev_n+" shell am start -n com.ixia.ixchariot/com.ixia.ixchariot.Endpoint"
		os.system(cmd_line)
	def stopEndpoint(self,dev_n):
		cmd_line = "adb -s "+dev_n+" shell am force-stop com.ixia.ixchariot/com.ixia.ixchariot.Endpoint"
		os.system(cmd_line)
	def ConnectWifi(self,dev_n,ssid,password):
		cmd_line2= "adb -s "+dev_n+" shell am force-stop com.example.autoconnectwifi"
		os.system(cmd_line2)
		time.sleep(2)
		cmd_line = "adb -s "+dev_n+" shell am start -n com.example.autoconnectwifi/com.example.autoconnectwifi.MainActivity -d "+ ssid+":"+password
		os.system(cmd_line)
		#os.system(cmd_line2)
	def stopConnect(self,dev_n):
		cmd_line = "adb -s "+dev_n+" shell am force-stop com.example.autoconnectwifi"
		os.system(cmd_line)
	def disConnectWifi(self,dev_n):
		cmd_line2= "adb -s "+dev_n+" shell am force-stop com.example.autoconnectwifi"
		os.system(cmd_line2)
		time.sleep(2)
		cmd_line = "adb -s "+dev_n+" shell am start -n com.example.autoconnectwifi/com.example.autoconnectwifi.MainActivity -d stop"
		os.system(cmd_line)
	def installApk(self,dev_n,apk):
		cmd_line = "adb -s "+dev_n+ " install " + apk
		os.system(cmd_line)
	
