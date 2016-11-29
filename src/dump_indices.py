#!/usr/bin/python

'''
Created on Nov 28, 2016

@author: hank
'''

import sys
import json
import time
import requests

from lib.scraping_helper import parse_indices, save_to_file


ajax_get_base_urls = {"sp500": "https://markets.ft.com/data/indices/ajax/getindexconstituents?xid=575769&pagenum=%s",
                        "ftse": "https://markets.ft.com/data/indices/ajax/getindexconstituents?xid=572009&pagenum=%s",
                            "ftsm": "https://markets.ft.com/data/indices/ajax/getindexconstituents?xid=591836&pagenum=%s"}


def main(idx_name, base_url):

    page_num = 0
    while True:
        
        page_num += 1
        print "[System] Dumping page #" + str(page_num) + " ..."
        
        try:
            ###print base_url % str(page_num)
            response_data = json.loads(requests.get(base_url % str(page_num)).text)
            html_bundle = response_data["html"]
        except requests.exceptions.ConnectionError:
            page_num += -1
            print "[Warn] Try connecting again:", sys.exc_info()[0]
            time.sleep(1)
            continue
        except:
            print "[Error] Unexpected error:", sys.exc_info()[0]
            exit()
        
        indices_list = parse_indices(html_bundle)
        if not indices_list:
            break
        save_to_file(idx_name, str(page_num), indices_list)

    print "[System] Task is over."


if __name__ == '__main__':

    args = sys.argv
    if len(args) < 2 or not args[1] in ajax_get_base_urls:
        print "[Help] You should give a proper parameter ('sp500' or 'ftse' or 'ftsm'). Please read the README.md file for detail."
        exit()

    
    idx_name = args[1]
    main(idx_name, ajax_get_base_urls[idx_name])
    
    exit()
    
    
