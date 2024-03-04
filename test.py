import scapy
from scapy.all import *

packet = IP(dst="192.168.1.77") / ICMP()

response = sr1(packet, timeout=2)

if response:
    print("YOOOO I GOT IT")
    print(response.summary())
else:
    print("THERE WAS NOTHGING")










