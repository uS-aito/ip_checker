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
            slash_subnet = self._convert_subnet_type(ip_address.split(" ")[1])
            slash_address_mode(ip_address.split(" ")[0]+slash_subnet)

        def slash_address_mode(ip_address):
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
            print("Subnet mask: %s or %s" % ("/"+subnet_mask,self._convert_subnet_type("/"+subnet_mask)))
            print("Network address: %s" % network_address)
            print("Youngest host address: %s" % youngest_host_address)
            print("Oldest host address: %s" % oldest_host_address)
            print("Broadcast address: %s" % broadcast_address)
        
        # check ip_address is valid
        if not self.is_valid_ip(ip_address):
            raise ValueError()

        if "/" in ip_address:
            slash_address_mode(ip_address)
        else:
            long_address_mode(ip_address)

    def _convert_subnet_type(self,subnet):
        slash_to_long = {
            '/22': '255.255.252.0', 
            '/23': '255.255.254.0', 
            '/6': '252.0.0.0', 
            '/10': '255.192.0.0', 
            '/8': '255.0.0.0', 
            '/5': '248.0.0.0', 
            '/16': '255.255.0.0', 
            '/12': '255.240.0.0', 
            '/28': '255.255.255.240', 
            '/26': '255.255.255.192', 
            '/13': '255.248.0.0', 
            '/7': '254.0.0.0', 
            '/3': '224.0.0.0', 
            '/21': '255.255.248.0', 
            '/14': '255.252.0.0', 
            '/30': '255.255.255.252', 
            '/15': '255.254.0.0', 
            '/1': '128.0.0.0', 
            '/17': '255.255.128.0', 
            '/29': '255.255.255.248', 
            '/27': '255.255.255.224', 
            '/9': '255.128.0.0', 
            '/18': '255.255.192.0', 
            '/20': '255.255.240.0', 
            '/25': '255.255.255.128', 
            '/31': '255.255.255.254', 
            '/4': '240.0.0.0', 
            '/19': '255.255.224.0', 
            '/2': '192.0.0.0', 
            '/11': '255.224.0.0', 
            '/32': '255.255.255.255', 
            '/24': '255.255.255.0'
        }
        long_to_slash = {
            '255.255.192.0': '/18', 
            '255.252.0.0': '/14', 
            '255.255.224.0': '/19', 
            '255.255.240.0': '/20', 
            '255.255.255.252': '/30', 
            '255.248.0.0': '/13', 
            '255.255.0.0': '/16', 
            '240.0.0.0': '/4', 
            '255.255.255.224': '/27', 
            '255.255.252.0': '/22', 
            '255.224.0.0': '/11', 
            '255.254.0.0': '/15', 
            '255.128.0.0': '/9', 
            '248.0.0.0': '/5', 
            '252.0.0.0': '/6', 
            '192.0.0.0': '/2', 
            '255.255.255.240': '/28', 
            '255.255.255.192': '/26', 
            '255.255.248.0': '/21', 
            '255.255.254.0': '/23', 
            '128.0.0.0': '/1', 
            '255.255.255.128': '/25', 
            '224.0.0.0': '/3', 
            '255.255.255.254': '/31', 
            '254.0.0.0': '/7', 
            '255.0.0.0': '/8', 
            '255.255.255.248': '/29', 
            '255.192.0.0': '/10', 
            '255.240.0.0': '/12', 
            '255.255.128.0': '/17', 
            '255.255.255.255': '/32', 
            '255.255.255.0': '/24'
        }
        def long_address_mode(subnet):
            return long_to_slash[subnet]

        def slash_address_mode(subnet):
            return slash_to_long[subnet]

        if "/" in subnet:
            return slash_address_mode(subnet)
        else:
            return long_address_mode(subnet)


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
