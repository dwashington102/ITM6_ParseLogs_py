import os
import re
import itm6common

cq_raslog = r"/home/washingd/Desktop/Temp/apptuv0018_cq_KfwServices_5a1da33c-01.log"

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
    print("Logs reviewed: ", cq_raslog)
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
        itm6common.itmIpaddr(cq_raslog)
        itm6common.itmprotocol(cq_raslog)
        itm6common.itmPort(cq_raslog)
        itm6common.itmMsindex(cq_raslog)
        itm6common.itmcms(cq_raslog)

def get_tepsinfo():
    teps_db()
    tepsonline()
    teps_ewas()
    teps_embed()
    teps_jvm()
    teps_fips()
    teps_tdw()


def teps_db():
    with open(cq_raslog, 'r') as reviewras:
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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("\nTEPS Database Type (KFW_DSN): ", itmout, "\n")


def teps_ewas():
    with open(cq_raslog, 'r') as reviewras:
        itmemptylist = []
        for my_line in reviewras:
            if re.search(searchEwas, my_line):
                itmemptylist.append(my_line)
            else:
                pass
        a = len(itmemptylist)
        if a <= 0:
            print("KFW_AUTHORIZATiON_USE_EWAS: NOT FOUND")
        else:
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("KFW_AUTHORIZATION_USE_EWAS: ", itmout, "\n")


def teps_embed():
    with open(cq_raslog, 'r') as reviewras:
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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("KFW_USE_EMBEDDED=", itmout)


def teps_jvm():
    with open(cq_raslog, 'r') as reviewras:
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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("KFW_STARTJVM=", itmout)


def teps_fips():
    with open(cq_raslog, 'r') as reviewras:
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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("KFW_FIPS_ENFORCED=", itmout)


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
            itmout = itmemptylist.pop()
            itmout = re.sub('\n', '', itmout)
            print("\nTEPS settings regarding connection to the Data Warehouse")
            print(itmout)


def tepsonline():
    tepsup_matchlist = []
    with open(cq_raslog, 'r') as reviewras:
        for my_line in reviewras:
            for match in re.finditer(cqonline, my_line, re.S):
                cqup_text = match.group()
                #cqup_text = re.sub(r'\n', '', cqup_text)
                tepsup_matchlist.append(cqup_text)
                print("debug tesponline: ", cqup_text)


def tepsearch():
    with open(cq_raslog, 'r') as reviewraslog:
        for my_line in reviewraslog:
            if re.search(cqonline, my_line, re.I):
                print("debug tepsearch:", my_line)
            else:
                pass

display_menu()
get_itm6common()
get_tepsinfo()

