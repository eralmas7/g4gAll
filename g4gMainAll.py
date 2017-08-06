#!/usr/bin/python

import requests
from os import system
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import gc

BASE_URL = 'http://www.geeksforgeeks.org/'
articles = []
allLinks = []

CHOICE_TO_CATEGORY_MAPPING = {
    1: 'category/algorithm/dynamic-programming/',
    2: 'category/algorithm/analysis/',
    3: 'category/searching/',
    4: 'category/sorting/',
    5: 'category/algorithm/greedy/',
    6: 'category/algorithm/pattern-searching/',
    7: 'category/c-strings/',
    8: 'category/algorithm/backtracking/',
    9: 'category/algorithm/divide-and-conquer/',
    10: 'category/algorithm/geometric/',
    11: 'category/algorithm/mathematical/',
    12: 'category/bit-magic/',
    13: 'category/algorithm/randomized/',
    14: 'category/algorithm/branch-and-bound/',
    15: 'category/linked-list/',
    16: 'category/stack/',
    17: 'category/queue/',
    18: 'category/tree/',
    19: 'category/binary-search-tree/',
    20: 'category/heap/',
    21: 'category/hash/',
    22: 'category/graph/',
    23: 'category/advanced-data-structure/',
    24: 'category/c-arrays/',
    25: 'category/matrix/',
    26: 'fundamentals-of-algorithms',
    27: 'array-data-structure',
    28: 'data-structures/linked-list',
    29: 'stack-data-structure',
    30: 'queue-data-structure',
    31: 'binary-tree-data-structure',
    32: 'binary-search-tree-data-structure',
    33: 'heap-data-structure',
    34: 'hashing-data-structure',
    35: 'graph-data-structure-and-algorithms',
    36: 'matrix',
    37: 'data-structures',
    38: 'bitwise-algorithms',
    39: 'randomized-algorithms'
}

def get_category_choice():
    list = []
    for x in xrange(1, 40):
       list.append(CHOICE_TO_CATEGORY_MAPPING[x])
    return list

import os
import re

def save_articles_as_html_and_pdf(fileName):
    print("All links scraped, extracting articles")
    all_articles = (
        '<!DOCTYPE html>'
        '<html><head>'
        '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />'
        '<link rel="stylesheet" href="style.min.css" type="text/css" media="all" />'
        '</head><body>'
    )

    for x in range(len(articles)):
        strng = articles[x].decode("utf-8")
        strng = re.sub('\n\s*\n\s*', '', strng)
        all_articles += '<hr id=\"' + str(x + 1) + '\">' + strng

    all_articles += '''</body></html>'''
    html_file_name = 'G4G_' + fileName + '.html'
    if "/" in category_url.title():
        head, tail = os.path.split(re.sub(r"/$", "", category_url.title()))
        html_file_name = 'G4G_' + tail.replace('/', '') + '.html'
    html_file = open(html_file_name, "w")
    html_file.write(all_articles.encode("utf-8"))
    html_file.close()
    pdf_file_name = 'G4G_' + fileName + '.pdf'
    if "/" in category_url.title():
        head, tail = os.path.split(re.sub(r"/$", "", category_url.title()))
        pdf_file_name = 'G4G_' + tail.replace('/', '') + '.pdf'

    print("Generating PDF " + pdf_file_name)
    html_to_pdf_command = 'wkhtmltopdf ' + html_file_name + ' ' + pdf_file_name
    system(html_to_pdf_command)


def scrape_category(category_url):
    try:
        links = []
        print "Using URL now " + category_url
        soup = BeautifulSoup(requests.get(category_url).text, 'lxml')
        previous_url = category_url
        for url in soup.find_all("a", {'class': 'nextpostslink'}):
            category_url = url['href']
        if category_url == previous_url:
            category_url = None
    except ConnectionError:
        print ("Will retry accessing url " + BASE_URL + category_url)

    links = list([a.attrs.get('href') for a in soup.select('ol li a')])
    links.extend(list([a.attrs.get('href') for a in soup.select('article header h2 a')]))
    links = [link for link in links if link is not None or "?" or "#" not in link]
    allLinks.extend(links)

    print("Found: " + str(len(links)) + " links")
    return category_url

def downloadAll(maxCount=1000):
    i = 1
    count = 0

    for link in allLinks:
        try:
            link = link.strip()
            count += 1
            print("Scraping link no: " + str(i) + " Link: " + link)
            i += 1
            download(link)
        except ConnectionError:
            print("Will download again from " + str(link))
            download(link)
        if (count == maxCount):
            gc.collect()
            save_articles_as_html_and_pdf('file' + str(i))
            del articles[:]
            count = 0
            gc.collect()

def download(link):
    result = requests.get(link).text

    link_soup = BeautifulSoup(result, 'lxml')
    [script.extract() for script in link_soup(["script", "ins", "footer"])]
    for code_tag in link_soup.find_all('pre'):
        code_tag['class'] = code_tag.get('class', []) + ['prettyprint']
    article = link_soup.find('article')
    for div in link_soup.find_all("div", {'class': 'AdsParent'}):
        div.decompose()
    for anchor in link_soup.find_all("a", {'href': 'http://practice.geeksforgeeks.org/company-tags'}):
        anchor.decompose()
    for anchor in link_soup.find_all("a", {'href': 'http://quiz.geeksforgeeks.org/gate-corner-2/'}):
        anchor.decompose()
    for div in link_soup.findAll('div', {'id': 'practiceLinkDiv'}):
        div.decompose()

    if (not article is None):
        page = article.encode('UTF-8')
        articles.append(page)

if __name__ == '__main__':
    category_urls = get_category_choice()
    for category_url in category_urls:
        nextUrl = BASE_URL + category_url
        while nextUrl is not None:
            nextUrl = scrape_category(nextUrl)
    gc.collect()
    mset = set()
    lsit = list()
    for item in allLinks:
        if item not in mset:
            lsit.append(item)
            mset.add(item)
    print ('We have all the urls now in hand in total ' + str(len(allLinks)) + ' This does includes duplicates so removing them says ' + str(len(lsit)))
    allLinks = lsit
    mset = None
    downloadAll()
    gc.collect()
    save_articles_as_html_and_pdf('lastFile')