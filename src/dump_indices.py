#!/usr/bin/python

'''
Created on Nov 28, 2016

@author: hank
'''

import sys
import json
import time
import requests

from src.lib.scraping_helper import parse_indices, save_to_file
from pip._vendor.requests.exceptions import ConnectionError



ajax_get_base_urls = {"sp500": "https://markets.ft.com/data/indices/ajax/getindexconstituents?xid=575769&pagenum=%s",
                        "ftse": "https://markets.ft.com/data/indices/ajax/getindexconstituents?xid=572009&pagenum=%s",
                            "ftsm": "https://markets.ft.com/data/indices/ajax/getindexconstituents?xid=591836&pagenum=%s"}


def main(idx_name, base_url):

    page_num = 100
    while True:
        
        page_num += 1
        print "[System] Dumping page #" + str(page_num) + " ..."
        
        try:
            ###print base_url % str(page_num)
            response_data = json.loads(requests.get(base_url % str(page_num)).text)
            html_bundle = response_data["html"]
        except ConnectionError:
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
    if len(args) < 1 and not args[0] in ajax_get_base_urls:
        print "[System] You should give proper parameter. Please see the readme file."
        exit()

    
    idx_name = args[0]
    main(idx_name, ajax_get_base_urls[idx_name])
    
    exit()
    
    