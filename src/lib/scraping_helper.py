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
    file_name = idx_name + "_" + page_num
    root_dir_path = op.abspath(op.join(__file__, op.pardir, op.pardir, op.pardir))
    scraped_files_dir = op.join(root_dir_path, "indices")
    target_dir = op.join(scraped_files_dir, idx_name)
    if not op.exists(target_dir):
        os.mkdir(target_dir)
    with open(op.join(target_dir, file_name), "w") as f:
        for index in indices_list:
            f.write(index)
            f.write("\n")

