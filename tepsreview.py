import os
import re
import itm6common

cq_raslog = r"/home/washingd/Desktop/Temp/apptuv0018_cq_KfwServices_5a1da33c-01.log"
cqonline  = '.*Waiting\sfor\srequests.*'

def display_menu():
    os.system('clear')
    print("Logs reviewed: ", cq_raslog, "\n")


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
        itm6common.itmcms(cq_raslog)


def tepsonline():
    tepsup_matchlist = []
    with open(cq_raslog, 'r') as reviewraslog:
        for my_line in reviewraslog:
            for match in re.finditer(cqonline, my_line, re.S):
                cqup_text = match.group()
                #cqup_text = re.sub(r'\n', '', cqup_text)
                tepsup_matchlist.append(cqup_text)
                print("debug tesponline: ", cqup_text)

#def tepscheck():
#    with open(cq_raslog, 'r') as reviewraslog:
#        for my_line in reviewraslog:
#            if re.search(cqonline, my_line):
#                print("TEPS Online Message Found2")
#            else:
#                print("TEPS Online Message NOT FOUND!")


def tepsearch():
    with open(cq_raslog, 'r') as reviewraslog:
        for my_line in reviewraslog:
            if re.search(cqonline, my_line, re.I):
                print("debug tepsearch:", my_line)
            else:
                pass

display_menu()
#tepsonline()
#tepsearch()
get_itm6common()









