#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import walk
from os.path import getsize
from time import perf_counter
from zipfile import ZipFile
from datetime import date


def search():
    '''
    Search All Non-Hidden Files 
    '''
    PATH = '/home/pi'
    all_files = []
    start = perf_counter()
    print('Scanning For File System...Please Wait')
    for root, dirs, files in walk(PATH):       
        if '.' not in root:
            for y in files:
                if not y.startswith('.'):
                    complete_path = root+'/'+y
                    all_files.append(complete_path)
    print(f"Total Time Taken To Scan all files: {round(perf_counter()-start, 2)} seconds")
    return all_files


def showFilesGreaterMB(all_files,MB=10):
    '''    
    Top Files Size Greater Than, bydefault=10MB
    '''
    for x in all_files:
        size = getsize(x)
        if size > (MB*1024*1024):
            print(x,str(round(size/(1024*1024),2))+ 'MB')


def createArchive():
    '''
    Create Archive with Date as Name
    '''
    zip_filename = str(date.today())+'.zip'
    print('Starting Backup....It might take some time')
    with ZipFile(zip_filename,'w') as z:
        for x in all_files:
            z.write(x)


if __name__ == "__main__":
    all_files = search()
    while True:    
        choose = input('\nPress 1 - To Search Again\nPress 2 - To Find Files Size Greater than 10MB \nPress 3 - To Take Backup \n')
        if int(choose) == 1:
            all_files = search()
        elif int(choose) == 2:
            MB = input('Enter size number in MB, default is 10MB')
            try:
                showFilesGreaterMB(all_files,int(MB))
            except:
                print('Please Enter size in MB... Showing Files Greater than 10MB - ')
                showFilesGreaterMB(all_files)
        elif int(choose) == 3:
            createArchive(all_files)
            break
        else:
            print('Please Choose Proper Option')

