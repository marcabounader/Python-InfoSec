from scapy.all import *

def transmit(message,host):
    for m in message:
        mac=get_if_hwaddr(conf.iface)
        packet=Ether(src=mac,dst=mac)/IP(dst=host)/ICMP(code=ord(m))
        sendp(packet,verbose=False)

host="127.0.0.1"
message="hello"
transmit(message,host)