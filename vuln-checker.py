#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'Recep Gunes'

import requests, sys

def file_open(file_name):
    list = []
    file = open(file_name,"r")
    file_in = file.readlines()
    for value in file_in:
        if value not in " ":
            list.append(value.replace("\n", ""))
        else:
            pass
    file.close()
    return list

def checker(vuln_list):
    error_list = file_open("error.conf")
    sites = []
    value = False
    for vuln in vuln_list:
        sites.append(vuln+"'")
    for site in sites:
        try:
            request = requests.get(url=site.encode("UTF-8"))
            source_code = str(request.content)
            for error in error_list:
                if error in source_code:
                    value = True
                    break
                elif error not in source_code:
                    value = False
                    continue
            if value == True:
                print("[+] {} ----> Vuln Found.".format(site))
            elif value == False:
                print("[-] {} ----> Vuln Not Found.".format(site))
        except requests.ConnectionError:
            print("[!] {} ----> Connection Error!".format(site))
    print("{}".format("=" * 75))

def banner():
    banner = """{}
\t  ___  ___  _    _  __   __    _        
\t / __|/ _ \| |  (_) \ \ / /  _| |_ _    
\t \__ \ (_) | |__| |  \ V / || | | ' \ _ 
\t |___/\__\_\____|_|_  \_/ \_,_|_|_||_(_)
\t  / __| |_  ___ __| |_____ _ _          
\t | (__| ' \/ -_) _| / / -_) '_|         
\t  \___|_||_\___\__|_\_\___|_|           

\t How To Use: \n \t python3 vuln-checker.py [target_list]
{}""".format("="*75, "="*75)
    return banner

if __name__ == "__main__":
    try:
        print(banner())
        target_file = file_open(sys.argv[1])
        checker(target_file)
        sys.exit()
    except IndexError:
        print("Please Entry A Target File Name.\n")
        sys.exit()