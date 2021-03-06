from __future__ import print_function
import re

searchHost = '.*System\sName:\s'
searchType = '.*System\sType:\s'
searchDate = '.*Start\sDate:\s'
searchTime = '.*Start\sTime:\s'
searchUser = '.*User\sName:\s'
searchPid = '.*Process\sID:\s\d'
searchNofile = '.*Nofile\sLimit:\s'
searchChome = '.*ITM\sHome:\s'
searchKbbras1 = '.*KBB_RAS1:\s'
searchipaddr = '\d:\ssource=.*'
searchPort = '.*KDEBP_AssignPort.*'
searchMsindex = '.*listening:.*'

# BSS1_GetEnv Variables
searchDynamic = 'BSS1_GetEnv.*KBBRA_ChangeLogging'
searchprotocol = 'BSS1_GetEnv.*KDC_FAMILIES='
searchCms = 'BSS1_GetEnv.*CMSLIST=".*'

# Header Functions


def itmhost(raslog):
    print("\n#######################################################")
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchHost, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("Hostname NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('^.*Name:', '', itmout)
            itmout = re.sub('Process\sID.*$\n', '', itmout)
            print("Hostname, System Type, Start Date/Time Process Info:\n", "HOSTNAME: ", itmout)


def itmtype(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchType, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("System Type: NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('^.*Type:', '', itmout)
            itmout = re.sub('\n', '', itmout)
            print("System Type: ", itmout)


def itmSdate(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchDate, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <=0:
            print("Start Date NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*Date:', '', itmout)
            #itmout = re.sub(r'St.*\n', '', itmout)
            print("Start Date: ", itmout)


def itmStime(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchTime, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("Start Time NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*Time:', '', itmout)
            print("Start Time: ", itmout)


def itmPid(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchPid, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("Process ID NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*\s+Process\sID:', '', itmout)
            print("Process ID: ", itmout)


def itmUser(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchUser, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("Userid NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*\s+User\sName:', '', itmout)
            print("UserID: ", itmout)


def itmChome(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchChome, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("CANDLEHOME NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*ITM\sHome:\s', '', itmout)
            itmout = re.sub('ITM\sProcess:.*', '', itmout)
            print("CANDLEHOME: ", itmout)


def itmnofile(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchNofile, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("ULIMIT NOFILE SETTING NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*Nofile\sLimit:\s', '', itmout)
            itmout = re.sub('Stack\s.*$', '', itmout)
            print("ulimit nofile setting: ", itmout)
    print("#######################################################\n")

# End of Header Functions


def itmKbbras1(raslog):
    print("\n#######################################################")
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchKbbras1, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print ("KBB_RAS1 trace setting NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('^.*RAS1:', '', itmout)
            itmout = re.sub(r'\n', '', itmout)
            print("Debug Setting (KBB_RAS):", itmout)


def itmdynamic(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchDynamic, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print ("Dynamic debug trace not set")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
    print("#######################################################")


def itmIpaddr(raslog):
    print("#######################################################")
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchipaddr, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("Network Interfaces NOT FOUND")
        else:
            print("Network Information:")
            nic = 1
            for itmout in itmemptylist:
                itmout = re.sub('\n', '', itmout)
                itmout = re.sub('^.*\d+\s+', '', itmout)
                print("Network Interface Card["+ str(nic)+ "]:", itmout)
                nic += 1


def itmprotocol(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchprotocol, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("\nKDC_FAMILIES NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('"\n', '', itmout)
            itmout = re.sub('\(.*\).*="', '', itmout)
            print("\nKDC_FAMILIES Network Protocol Setting:\n", itmout)


def itmPort(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchPort, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("Agent's Port Assignment NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*AssignPort"\)', '', itmout)
            print("\nAgent is bound to Port (KDEBP_AssignPort):\n", itmout)


def itmcms(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchCms, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("TEMS Connection NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('\(.*\).*="', '', itmout)
            print("\nAgent configured to connect to TEMS: ", itmout)

def itmMsindex(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmemptylist = []
        for my_line in reviewraslog:
            if re.search(searchMsindex, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("\nMonitoring Agent registration with Monitoring Service Index NOT FOUND")
        else:
            print ("\nAgent Registered with Monitoring Service Index Using Port (add_listener):")
            for itmout in itmemptylist:
                itmout = re.sub('\n', '', itmout)
                itmout = re.sub('\(.*\)', '', itmout)
                print(itmout)
