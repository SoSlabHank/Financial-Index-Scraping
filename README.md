#Financial Index Scraping:

This project can make you get the indices of three main financial indices and save results into files in the 'indices' directory.  
The data is scraped from the web [FINANCIAL TIMES](https://markets.ft.com/data/). 

##Getting Started:

###Prerequisites:

The development enviroment of this project is *Ubuntu 16.04 LTS*

###Dependencies:

*python2.7*  
*Beautifulsoup4*  
*Requests*  
(See the requirements.txt in the same directory for detail)

###Code Example:

####for S&P 500 INDEX:
    $cd {the path to 'Financial-Index-Scraping'}/src
    $python dump_indices.py sp500

####for FTSE 100 INDEX:
    $cd {the path to 'Financial-Index-Scraping'}/src
    $python dump_indices.py ftse

####for FTSE 250 MID INDEX:
    $cd {the path to 'Financial-Index-Scraping'}/src
    $python dump_indices.py ftsm

##Motivation:

Learning some scraping skills and familiar with git operations.

##Installation

    $git clone https://github.com/SoSlabHank/Financial-Index-Scraping.git
    $cd Financial-Index-Scraping
    $pip install -r requirements.txt

##Contributors:

You can learn about *beautifulsoup4 library* (https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for scraping skills.

##License:

These code can be copied for everyone who want to use it and needn't to ask me.

