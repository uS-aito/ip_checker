#coding: utf-8
import sys
import ip_address_tool

def main():
    def is_py3():
        if sys.version_info[0] == 3:
            return True
        else:
            return False

    def print_special_ip():
        iat = ip_address_tool.IpAddressTool()
        while(True):
            ip = input("> ")
            if iat.is_valid_ip(ip):
                iat.print_special_ip(ip)
            else:
                print("Invald IP address.")

    if not is_py3():
        sys.stdout.write("Sorry, this script is for only python 3.x.\n")
        exit(-1)
    else:
        print_special_ip()

if __name__ == '__main__':
    main()