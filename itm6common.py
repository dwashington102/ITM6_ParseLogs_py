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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("Hostname, Operating System, Start Date/Time: ", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("debug: ", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("debug: ", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("debug: ", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("debug: ", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("debug: ", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("CANDLEHOME: ", itmout)
    print("#######################################################\n")


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("Debug Setting (KBB_RAS): ", itmout)


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
            itmout = itmemptylist.pop()
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
            for nic in itmemptylist:
                nic = re.sub('\n', '', nic)
                print("Network Interface Card:", nic)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("\nKDC_FAMILIES setting:", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("\nPort Agent is connected to (KDEBP_AssignPort):\n", itmout)


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
            print("TEMS connection NOT FOUND")
        else:
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("debug: ", itmout)

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
            print ("\nAgent Registered with Monitoring Service Index Using Port (add_listener):\n")
            for ms_port in itmemptylist:
                ms_port = re.sub('\n', '', ms_port)
                print(ms_port)
