#!bin/python3
# 
# usage: 
# script_name.py logfile_name.txt size_in_kb number_of_logfiles
# example: 
# purge-log.py logfile.txt 10 5
# 

import os
import shutil
import sys

if (len(sys.argv) < 4):
    print("Missing arguments. Usage: script_name.py logfile_name.txt size_in_kb number_of_logfiles")
    exit(1)

file_name = sys.argv[1]
size_limit = int(sys.argv[2])
logs_number = int(sys.argv[3])

if (os.path.isfile(file_name) == True):
    logfile_size = os.stat(file_name).st_size / 1024

    if (logfile_size >= size_limit):
        if (logs_number > 0):
            for current_file_num in range(logs_number, 1, -1):
                src = file_name + "_" + str(current_file_num - 1)
                dst = file_name + "_" + str(current_file_num)
                if (os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("copied from " + src + " to " + dst)
            shutil.copyfile(file_name, file_name + "_1")
            print("Copied: " + file_name + " to " + file_name + "_1")
        reset_file = open(file_name, "w")
        reset_file.close()
