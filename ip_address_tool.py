#coding: utf-8
import re

class IpAddressTool(object):
    # check ip_address is valid ip address (means like "192.168.0.1/24 or 192.168.0.1 255.255.255.240")
    def is_valid_ip(self,ip_address):
        ip_pattern = r"(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
        short_subnet_pattern = r"(\/([1-9]|[1-2][0-9]|3[0-2]))"
        long_subnet_pattern = r"( ({0}))".format(ip_pattern)
        marged_pattern = r"^(({0}{1})|({0}{2}))$".format(ip_pattern,short_subnet_pattern,long_subnet_pattern)
        # pattern = r"^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/([1-9]|[1-2][0-9]|3[0-2]))$"
        match_result = re.match(marged_pattern,ip_address)
        if match_result:
            return True
        else:
            return False
    
    # print network, minimam host, maximam host, broadcast ip address
    def print_special_ip(self,ip_address):
        def long_address_mode(ip_address):
            pass

        def slash_mode(ip_address):
            # split ip_address
            (address, subnet_mask) = ip_address.split("/")
            address = address.split(".")

            # make network address
            target = (int(subnet_mask)-1)//8
            bitmask = 255 << (8-int(subnet_mask))%8
            bitmask = bitmask & 255
            address[target] = str(int(address[target]) & bitmask)
            for i in range(target+1,4):
                address[i] = "0"
            network_address = ".".join(address)
            network_address = network_address + "/" + subnet_mask

            # make youngest host address
            address[3] = str(int(address[3])+1)
            youngest_host_address = ".".join(address)
            youngest_host_address = youngest_host_address + "/" + subnet_mask

            # make broadcast address
            address[3] = str(int(address[3])-1)
            bitmask = 255 - bitmask
            address[target] = str(int(address[target]) | bitmask)
            for i in range(target+1,4):
                address[i] = "255"
            broadcast_address = ".".join(address)
            broadcast_address = broadcast_address + "/" + subnet_mask

            # make oldest host address
            address[3] = str(int(address[3])-1)
            oldest_host_address = ".".join(address)
            oldest_host_address = oldest_host_address + "/" + subnet_mask

            # print special addresses
            print("Network address: %s" % network_address)
            print("Youngest host address: %s" % youngest_host_address)
            print("Oldest host address: %s" % oldest_host_address)
            print("Broadcast address: %s" % broadcast_address)

        # check ip_address is valid
        if not self.is_valid_ip(ip_address):
            raise ValueError()

        if "/" in ip_address:
            slash_mode(ip_address)
        else:
            pass



def main():
    iat = IpAddressTool()
    while(True):
        ip_address = input()
        if iat.is_valid_ip(ip_address):
            iat.print_special_ip(ip_address)
        else:
            print("Invald IP address.")

if __name__ == '__main__':
    main()
