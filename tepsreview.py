"""
Testing my limited knowledge of Python to parse TEPS logs.
It may not be pretty, but it's faster than digging through the logs to pull out settings.

Also -> using global variables is bad and I am using them throughout so I'm bad to the bone!
"""

from __future__ import print_function
from builtins import input
import os
import re
import itm6common
import datetime as DT

cq_raslog = input("Filename: ")

#TEPS config searches
searchKfwdsn = '.*\sKFW_DSN='
searchEwas = '.*KFW_AUTHORIZATION_USE_EWAS=.*'
searchEmbed = '.*KFW_USE_EMBEDDED=.*'
searchJvm = '.*KFW_STARTJVM=.*'
searchFips = '.*KFW_FIPS_ENFORCED=.*'
searchTdw = '.*fetchWarehouse"\)'
cqonline  = '.*Waiting\sfor\srequests.*'


def display_menu():
    os.system('clear')
    print("#######################################################")
    print("Logs reviewed:\n", cq_raslog)
    print("#######################################################")


def get_itm6common():
        itm6common.itmKbbras1(cq_raslog)
        itm6common.itmdynamic(cq_raslog)
        itm6common.itmhost(cq_raslog)
        itm6common.itmtype(cq_raslog)
        itm6common.itmSdate(cq_raslog)
        itm6common.itmStime(cq_raslog)
        itm6common.itmUser(cq_raslog)
        itm6common.itmPid(cq_raslog)
        itm6common.itmChome(cq_raslog)
        itm6common.itmnofile(cq_raslog)
        itm6common.itmIpaddr(cq_raslog)
        itm6common.itmprotocol(cq_raslog)
        itm6common.itmPort(cq_raslog)
        itm6common.itmMsindex(cq_raslog)
        itm6common.itmcms(cq_raslog)


#def get_itm6common():
#    itm6search.itm6openf(cq_raslog)

def get_tepsinfo():
    print("\n#######################################################")
    print("TEPS Configuration Information: ")
    tepsonline()
    teps_db()
    teps_ewas()
    teps_embed()
    teps_jvm()
    teps_fips()
    teps_tdw()
    print("#######################################################\n")


def teps_db():
    with open(cq_raslog, 'r') as reviewras:
        global itmemptylist
        itmemptylist = []
        for my_line in reviewras:
            if re.search(searchKfwdsn, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("\nTEPS Database Type: NOT FOUND")
        else:
            bssenv(itmemptylist)
            #itmout = itmemptylist.pop(0)
            #itmout = re.sub('\n', '', itmout)
            #itmout = re.sub('^.*GetEnv"\)\s', '', itmout)
            #print("\nTEPS Database Type (KFW_DSN):\n", itmout, "\n")


def teps_ewas():
    with open(cq_raslog, 'r') as reviewras:
        global itmemptylist
        itmemptylist = []
        for my_line in reviewras:
            if re.search(searchEwas, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("KFW_AUTHORIZATION_USE_EWAS: NOT FOUND")
        else:
            bssenv(itmemptylist)
            #itmout = itmemptylist.pop(0)
            #itmout = re.sub('\n', '', itmout)
            #itmout = re.sub('^.*GetEnv"\)\s', '', itmout)
            #print("KFW_AUTHORIZATION_USE_EWAS: ", itmout, "\n")


def teps_embed():
    with open(cq_raslog, 'r') as reviewras:
        global itmemptylist
        itmemptylist = []
        for my_line in reviewras:
            if re.search(searchEmbed, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("KFW_USE_EMBEDDED: NOT FOUND")
        else:
            bssenv(itmemptylist)
#            itmout = itmemptylist.pop(0)
#            itmout = re.sub('\n', '', itmout)
#            itmout = re.sub('^.*GetEnv"\)\s', '', itmout)
#            print(itmout)


def teps_jvm():
    with open(cq_raslog, 'r') as reviewras:
        global itmemptylist
        itmemptylist = []
        for my_line in reviewras:
            if re.search(searchJvm, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print ("KFW_STARTJVM: NOT FOUND")
        else:
            bssenv(itmemptylist)
            #itmout = itmemptylist.pop(0)
            #itmout = re.sub('\n', '', itmout)
            #itmout = re.sub('^.*GetEnv"\)\s', '', itmout)
            #print(itmout)


def teps_fips():
    with open(cq_raslog, 'r') as reviewras:
        global itmemptylist
        itmemptylist = []
        for my_line in reviewras:
            if re.search(searchFips, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print ("KFW_FIPS_ENFORCED: NOT FOUND")
        else:
            bssenv(itmemptylist)
            #itmout = itmemptylist.pop(0)
            #itmout = re.sub('\n', '', itmout)
            #print("KFW_FIPS_ENFORCED=", itmout)


def teps_tdw():
    with open(cq_raslog, 'r') as reviewras:
        itmemptylist = []
        for my_line in reviewras:
            if re.search(searchTdw, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print ("KFW_FIPS_ENFORCED: NOT FOUND")
        else:
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            itmout = re.sub('^.*"\)\s', '', itmout)
            print("\nTEPS settings regarding connection to the Data Warehouse")
            print(itmout)


def tepsonline():
    itmemptylist = []
    with open(cq_raslog, 'r') as reviewras:
        for my_line in reviewras:
            if re.search(cqonline, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print('TEPS "Waiting for requests" message NOT FOUND')
        else:
            print("\n^^^^^BELOW IS CRITICAL^^^^^^^")
            itmout = itmemptylist.pop(0)
            itmout = re.sub('\n', '', itmout)
            hexts = itmout.split(":")
            hexts0 = hexts[0]
            hexts0 = re.sub('\(', '', hexts0)
            hexts0 = re.sub('\.', '', hexts0)
            hexts0 = re.sub('-.*', '', hexts0)
            converted_hex = DT.datetime.utcfromtimestamp(float(int(hexts0, 16))/16**4)
            print("TEPS startup completed at (UTC): ", converted_hex)
            itmout = re.sub('^.*"\)\s', '', itmout)
            print(itmout)
            print("^^^^^ABOVE IS CRITICAL^^^^^^^\n")

def tepsearch():
    with open(cq_raslog, 'r') as reviewraslog:
        for my_line in reviewraslog:
            if re.search(cqonline, my_line, re.I):
                print("debug tepsearch:", my_line)
            else:
                pass


def bssenv(bsslist):
    itmout = itmemptylist.pop(0)
    itmout = re.sub('\n', '', itmout)
    itmout = re.sub('^.*GetEnv"\)\s', '', itmout)
    print(itmout)

display_menu()
get_itm6common()
get_tepsinfo()

