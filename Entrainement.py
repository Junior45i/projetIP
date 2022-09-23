import ipaddress
IP = '193.27.45.33'
MASK = '255.255.255.224'

host = ipaddress.IPv4Address(IP)
net = ipaddress.IPv4Network(IP + '/' + MASK, False)
print('IP:', IP)
print('Mask:', MASK)
print('Subnet:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Host:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Broadcast:', net.broadcast_address)

# import socket
# try: 
#     socket.inet_aton("1.0.0.0")
#     print("vrai")
# except socket.error:
#     print("faux")


import socket,struct

def makeMask(n):
    "return a mask of n bits as a long integer"
    return (2L<<n-1) - 1

def dottedQuadToNum(ip):
    "convert decimal dotted quad string to long integer"
    return struct.unpack('L',socket.inet_aton(ip))[0]

def networkMask(ip,bits):
    "Convert a network address to a long integer" 
    return dottedQuadToNum(ip) & makeMask(bits)

def addressInNetwork(ip,net):
   "Is an address in a network"
   return ip & net == net

address = dottedQuadToNum("192.168.1.1")
networka = networkMask("10.0.0.0",24)
networkb = networkMask("192.168.0.0",24)
print (address,networka,networkb)
print addressInNetwork(address,networka)
print addressInNetwork(address,networkb)