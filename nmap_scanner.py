import nmap

scanner = nmap.PortScanner()

print("Welcome, This is a Simple NMap Automation Tool")
print("NMap Version: " , scanner.nmap_version())
print("<--------------------------------------------->")

ip_addr = input("Enter a IP Address you want to scan: ")
print("IP Entered: " , ip_addr)

type(ip_addr)

resp = input("""\n Enter the type of scan you want to run
1) SYN ACK Scan
2) UDP Scan
3) Comprehensive Scan\n""")

if resp == '1':
    print("You want to conduct a SYN ACK Scan")
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("You want to conduct a UDP Scan")
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open UDP Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    print("You want to conduct a Comprehensive Scan")
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open TCP Ports: ", scanner[ip_addr]['tcp'].keys())
else:
    print("You Entered an Invalid Scan Option")
    print("Please Run the Program Again")
