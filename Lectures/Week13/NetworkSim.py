import firewall as fw
import packet as p

# Initialize Firewall object and add some rules
myFirewall = fw.Firewall("myFirewall")

myFirewall.addRule("192.168.1.3","192.168.1.2","25","Block")
myFirewall.addRule("192.168.1.5","192.168.1.9","123","Allow")
print(myFirewall.rules)


# Simulate Network traffic
# Why does Packet a not match the rule?
a = p.Packet("192.168.1.3","192.168.1.2",25)
b = p.Packet("192.168.1.3","192.168.1.2","25")

myFirewall.inspectPacket(a)
myFirewall.inspectPacket(b)

#myFirewall.inspectPacket(Packet.Packet("192.168.1.5","192.168.1.10","443"))
