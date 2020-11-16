#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os.path import getsize
from time import perf_counter
from zipfile import ZipFile
from datetime import date


all_files = []
size = 0
zipfilename = str(date.today())+'.zip'          # Bydefault today's date
PATH = '/home/pi'                               # Enter Path Here
#z = ZipFile(zipfilename, 'w')                  # ZipObject for creating zipfile


start = perf_counter()
for root, dirs, files in os.walk(PATH):       
    if '.' not in root:                                # This is for hidden directories
        for y in files:                             
            if not y.startswith('.'):                  # This is for hidden files in non-hidden directories
                complete_path = root+'/'+y
                all_files.append(complete_path)        # Complete path for every file
                size+=getsize(complete_path)           # Just for Size Comparison
                #z.write(complete_path)                # For Writing To ZipFiles


#z.close()
print('Total Number Of Files: '+str(len(all_files)))        
print('Total FileSize Of All Files: '+str(round(size/(1024*1024),2))+ 'MB')
print(f"Total Time Taken: {round(perf_counter()-start, 2)} seconds")






