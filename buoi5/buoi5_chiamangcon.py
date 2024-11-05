import ipaddress as ip

CLASS_C = '192.168.0.0'
prefix = 25     #24-30

if __name__=='__main__':
    net_addr = CLASS_C + '/' + str(prefix)
    print("netword address: %s"%net_addr)
    try:
        network = ip.ip_network(net_addr)
    except:
        raise Exception("Fail to create network")
    print("network configuration\n")
    print("\t network address: %s"%network.network_address)
    print("number of IP address: %s"%network.num_addresses)
    print("\t netmask: %s"%network.netmask)
    fist_ip, last_ip = list(network.hosts())[0], list(network.hosts())[-1]
    print("\t host IP from %s to %s"%(fist_ip, last_ip))
#list car 4 mang con