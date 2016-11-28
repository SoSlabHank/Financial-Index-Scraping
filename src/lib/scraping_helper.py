'''
Created on Nov 28, 2016

@author: hank
'''

import os
import os.path as op

from bs4 import BeautifulSoup



def parse_indices(html_bundle):
    
    soup = BeautifulSoup(html_bundle.encode('utf-8'), "html.parser")
    if soup.string == u"No constituents":
        return None


def save_to_file(idx_name, page_num, indices_list):
    pass

