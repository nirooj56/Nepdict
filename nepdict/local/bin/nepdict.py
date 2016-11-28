#!/usr/bin/python3
# -*- coding: utf-8 -*-
import signal
import re


# when the set time is up, it display a output and exits the programs
def handler(signum, frame):
    print("\n")
    print(color.BOLD + "Times UP! See you next time.")
    print("Thank you for using Nepdict." + color.END)
    exit(0)


# adds color to the output
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Install signal handler
signal.signal(signal.SIGALRM, handler)
# Set alarm for 1 minutes
signal.alarm(60)

# General Information to the end user
print("\n")
print(
    color.DARKCYAN + "The information provided here doesn't claim to be complete, accurate or reliable. However, We have tried our best for correctness and completeness with our resources and capability. You will be at your own risk and liable for any direct, indirect or consequential damage cause by the use of this content." + color.END + color.RED + " If you found any error or problem with the meaning or couldnot find words looking for, please kindly email the details to 'info@nepdict.com'." + color.END)
print("\n")


def fillUpDict(nepdict):
    '''
    :param nepdict: is a dict for database storage
    :return:
    '''
    s = '(.*\s),\s(.*)\s,(.*)'
    prg = re.compile(s)

    with open('../../../database/nirmal.csv') as fp:
        for line in fp:
            # print(line)
            m = prg.match(line)
            # print(line)
            # group2 is the noun/verb/adj, group3 is the meaning
            s = m.group(2).strip() , m.group(3).strip()
            nepdict[m.group(1).strip()]= s


def runScript():
    '''
        runs the script
    :return:
    '''

    while True:
        search = input("What are you looking for : ")
        search = search.strip().lower()
        looking = nepdict.get(search)

        if looking is not None:
            print(
                "Meaning of" + color.BLUE + search + color.END + " is: "
                + color.PURPLE + "(" + looking[0] + ")" + looking[1] + color.END)
        else:
            print(
                "There are no results for: " + "'" + color.RED + search + color.END + "'" + ", but we are adding new words daily.")

        print(color.BOLD + color.CYAN + "\n")
        cont = input("Do you want to continue? (y/n) : " + color.END)
        if cont == "y":
            continue
        else:
            print(color.BOLD + "Thank you for using Nepdict." + color.END)
            break



if __name__ == '__main__':
    # Word & Meaning Databases
    nepdict = dict()
    fillUpDict(nepdict)
    runScript()

