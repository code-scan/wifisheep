import SimpleHTTPServer
import SocketServer
import threading
import os
import json
from time import sleep
class back(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def cmd(self,c):
		c=os.popen(c).read()
		return c
	def run(self):
		while True:
			cmd=self.cmd("cat ../nohup.out |grep -|awk -F 'from ' '{print$2}'|sort |uniq ").replace('"','').split('\n')
			nohup=''
			self.cmd("echo > ../nohup.out  ")
			x=0
			for i in cmd:
				j='  "%d":"%s",' %(x,i)				
				nohup+= j
				x+=1
				
			nohup='{%s}'%nohup[:len(nohup)-1]
			cmd_h=self.cmd("cat /var/lib/dhcp/dhcpd.leases|grep host|awk '{print$2}' ").replace('"','').split('\n')
			x=0
			dhcp=''
			for i in cmd_h:
				j='  "%d":"%s",' %(x,i)				
				dhcp+= j
				x+=1
			dhcp='{%s}'%dhcp[:len(dhcp)-1]
			open('d.json','w').write(dhcp)
			open('o.json','w').write(nohup)
			print dhcp,nohup
			print "reading .."
			sleep(5)
back().start()

PORT = 8009
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
