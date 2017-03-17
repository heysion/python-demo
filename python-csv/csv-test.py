#! /usr/bin/env python3

import csv
import os
import re
import apt_pkg
from pprint import pprint

file='deepin-appstore-app-list.csv'

matched_packages=[]
noname_packages=[]
not_found_packages=[]

def match_pkg(cache, serial, pkg):
        """
        search package from apt cache
        """
        if pkg in cache:
                matched_packages.append([serial, pkg])
        elif ' ' in pkg:
                pkg2 = pkg.replace(' ', '-')
                match_pkg(cache,serial,pkg2)
                # # if pkg2 in cache:
                #         matched_packages.append([serial, pkg2]) #
        else:
                not_found_packages.append([serial, pkg])

def main():
        apt_pkg.init_config()
        apt_pkg.init_system()
        cache = apt_pkg.Cache()

        with open(file) as f:
               csvreader=csv.reader(f)
               for row in csvreader:
                        pkgname = row[2].strip().lower()
                        snumber = row[1]
                        if pkgname.endswith("网页版"):
                                not_found_packages.append([snumber, pkgname])
                        elif re.match("^[0-9a-zA-Z\s]+$", pkgname):
                                match_pkg(cache, snumber, pkgname)
                        else:
                                noname_packages.append([snumber, pkgname])


def save_file(file,buffer):
        with open(file,"a+") as f:
                f.writelines(buffer+"\n")
        pass
if __name__ == '__main__':
        main()
        out_file = "match.out"
        save_file(out_file,"matched %s"%(len(matched_packages)))
        save_file(out_file,"===== matched packages =====")
        save_file(out_file,"\n".join("%s %s"%(x[0],x[1]) for x in matched_packages))

        out_file = "notfound.out"
        save_file(out_file,"not found %s"%(len(not_found_packages)))
        save_file(out_file,"===== not found packages =====")
        save_file(out_file,"\n".join("%s %s"%(x[0],x[1]) for x in not_found_packages))

        out_file = "noname.out"
        save_file(out_file,"not name %s"%(len(noname_packages)))
        save_file(out_file,"===== not name packages =====")
        save_file(out_file,"\n".join("%s %s"%(x[0],x[1]) for x in noname_packages))


