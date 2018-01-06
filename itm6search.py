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

def itm6openf(raslog):
    with open(raslog, 'r') as reviewraslog:
        itmhost(reviewraslog)
        itmtype(reviewraslog)



def itmhost(raslog):
    print("\n#######################################################")
    itmemptylist = []
    print("debug fileinfo:", raslog)
    for my_line in raslog:
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
        print("Hostname, Operating System, Start Date/Time:\n", "debug: ", itmout)


def itmtype(raslog):
    itmemptylist = []
    print("debug fileinfo:", raslog)
    for my_line in raslog:
        if re.search(searchType, my_line):
            itmemptylist.append(my_line)
        else:
            pass
    a = len(itmemptylist)
    print("debug Value(a)", a)
    if a <= 0:
        print("System Type: NOT FOUND")
    else:
        itmout = itmemptylist.pop()
        itmout = re.sub('\n', '', itmout)
        print("debug: ", itmout)

