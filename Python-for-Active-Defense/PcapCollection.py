from scapy.all import *

decoys={
    "192.168.2.186":[443,8443],
    "192.168.2.185":[443,8443]
}

def analyzePackets(p):
    if p.haslayer(IP):
        decoyIP=[ip for ip in [p[IP].src,p[IP].dst] if ip in decoys]
        if len(decoyIP) >0:
            ports=None
            if p.haslayer(TCP):
                ports=[p[TCP].sport,p[TCP].dport]
            elif p.haslayer(UDP):
                ports=[p[UDP].sport,p[UDP].dport]
            decoyPort=[port for port in ports if port in decoys[decoyIP[0]]]
            if len(decoyPort)>0:
                wrpcap("out.pcap",p,append=True)


sniff(prn=analyzePackets)