# -*- coding:utf-8 -*-
# author: pcat
# http://pcat.cnblogs.com

import sys
import binwalk

if __name__ == "__main__":
    lst=sys.argv
    if len(lst)<2:
        print("No files.")
        exit()
    try:
        if lst[1][0]=='-':
            binwalk.scan(*lst[2:],signature=lst[1])
        elif lst[1][0]!='-':
            binwalk.scan(*lst[1:],signature=True)
    except:
        pass