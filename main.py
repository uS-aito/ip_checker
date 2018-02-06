#!/usr/local/bin/python3
#coding: utf-8
import sys
import ip_address_tool
from cmd import Cmd

class ip_tool_class(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.iat = ip_address_tool.IpAddressTool()
        self.prompt = "> "

    def default(self,line):
        if self.iat.is_valid_ip(line):
            self.iat.print_special_ip(line)
        else:
            print("Invalid IP Address.")
    
    def do_exit(self,arg):
        return True

def main():
    def is_py3():
        if sys.version_info[0] == 3:
            return False
        else:
            return True

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
    itc = ip_tool_class()
    itc.cmdloop()
    # main()
