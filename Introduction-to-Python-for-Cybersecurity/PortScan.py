from scapy.all import *

ports=[25,53,80,443,445,8080,8443,10000]

def SynScan(host):
    ans,unans=sr(IP(dst=host)/TCP(sport=5555,dport=ports,flags="S"),timeout=2,verbose=0) #half connect scan
    print("Port scan result:")
    if ans:
        for(s,r,) in ans:
            if s[TCP].dport==r[TCP].sport:
                print(s[TCP].dport,"is open")
    if unans:
        for(s) in unans:
            print(s[TCP].dport,"is closed.")

def DNSScan(host):
    ans,unans=sr(IP(dst=host)/UDP(sport=5555,dport=53)/DNS(rd=1,qd=DNSQR(qname='google.com')),timeout=2,verbose=0)
    if ans:
        print("DNS Server at %s"%host)

host="8.8.8.8"

SynScan(host)
DNSScan(host)