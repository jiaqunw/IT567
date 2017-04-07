import itertools
import sys
import socket
from array import array

# grab ip addresses range from user input
input_ip_string = raw_input("Please type in the ip addresses you would like to scan. (If you would like to scan a range of ip addresses, please use \"-\" in between the lower limit and upper limit): ")


try: # parse user input and create the list for the ip addresses
    def ip_range(input_ip_string):
        octets = input_ip_string.split('.')
        chunks = [map(int, octet.split('-')) for octet in octets]
        ranges = [range(c[0], c[1] + 1) if len(c) == 2 else c for c in chunks]
    
        for address in itertools.product(*ranges):
            yield '.'.join(map(str, address))

    iplist = []
    for address in ip_range(input_ip_string):
        iplist.append(address)
        #print(address)

except:
    print("Wrong IP addresses, program exiting.")
    sys.exit()



# grab ports range from user input
input_port_string = raw_input("Please type in the port you would like to scan. (If you would like to scan a range of ports, please use \"-\" in between the lower limit and upper limit): ")

#get the ports

ipports = [] #array of ports

try:
    try:  #generating list of ports, if given a range.
        iprange = input_port_string.split('-')
        range1 = int(iprange[0])
        range2 = int(iprange[1])
        range0 = range2-range1+1
    
    
        for nums in range(range0):
            ipports.append(range1)
            range1 = range1+1
    except: # the only input will be the list, if given one number
        ipports.append(int(input_port_string))

except:
    print("Wrong ports, program exiting")
    sys.exit()



# scan the hosts with the specified ports
for x in iplist:
    print ("Scanning host: " + str(x))
    for y in ipports:
        try: #scan using socket library
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            result = s.connect_ex((x, y))
            if result == 0:
                print("Port " + str(y) + " open!")
            s.close()
        
        except KeyboardInterrupt: # CTRL + C
            print ("User closed the program")
            sys.exit()

        except socket.gaierror:
            print ("Hostname could not be resolved. Exiting")
            sys.exit()

        except socket.error:
            print ("Couldn't connect to server")
            sys.exit()











