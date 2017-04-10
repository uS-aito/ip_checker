# IpAddressTool
特殊IPアドレス、最若・最老IPアドレスを計算するツールです。

---
## Description
任意のIPアドレス及びサブネットマスクを入力すると、そのネットワークについて以下のアドレスを出力します。  
* /XX形式、XXX.XXX.XXX.XXX形式のサブネットマスク
* ネットワークアドレス
* 最若ホストアドレス
* 最老ホストアドレス
* ブロードキャストアドレス 

## Demo
```
$ python3 main.py
> 192.168.1.100/24
Subnet mask: /24 or 255.255.255.0
Network address: 192.168.1.0/24
Youngest host address: 192.168.1.1/24
Oldest host address: 192.168.1.254/24
Broadcast address: 192.168.1.255/24
> 192.168.1.100 255.255.255.0
Subnet mask: /24 or 255.255.255.0
Network address: 192.168.1.0/24
Youngest host address: 192.168.1.1/24
Oldest host address: 192.168.1.254/24
Broadcast address: 192.168.1.255/24
```

## Requirement
* python2.7 or python3.5

## License
本ソフトウェアはMITライセンスに準拠します。  
* [MIT License](http://opensource.org/licenses/mit-license.php)
