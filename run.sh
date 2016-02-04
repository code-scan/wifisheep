echo 1 > /proc/sys/net/ipv4/ip_forward
airmon-ng check kill
airmon-ng start wlan0

nohup airbase-ng -P -C 30 -v mon0 &
ifconfig at0 up #启动interface
ifconfig at0 192.168.3.1 netmask 255.255.255.0 #分配IP和掩码
route add -net 192.168.3.0 netmask 255.255.255.0 gw 192.168.3.1 #增加路由项，统一由192.168.3.1(at0)来传输数据。
