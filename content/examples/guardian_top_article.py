# -*- coding: utf-8 -*-
"""
Fecth the text of the main headline article from the Guardian website.
Print it out and print out the URLs of any links in the text.
"""

import bs4
import requests


# %% Helper functions

def get_and_soupify(url):
    """Gets a webpage and turns it into a BeautifulSoup.

    Argument url: string URL

    Returns: bs4.BeautifulSoup

    Raises RuntimeError: if status of request is not '200 (OK)'
    """

    response = requests.get(url)
    msg = '{} ({}): {}'.format(response.status_code, response.reason, url)

    if response.status_code != 200:
        raise RuntimeError(msg)

    print(msg)

    return bs4.BeautifulSoup(response.text, 'lxml')


def print_output(content, title):
    """Print some output with a neat header line.

    Arguments:
        content: string content to print
        title: string title to display in header
    """

    header = '#### ' + title + ' ####'
    footer = '#' * len(header)

    print('', header, content, footer, sep='\n')


# %% Main page

main_url = 'https://www.theguardian.com/international'

page = get_and_soupify(main_url)

# Target:
# Within the <section> with id 'headlines' ...
# the first <a> tag ...
# with class 'fc-item__link' ...
# and data-link-name 'article'.

headlines = page.find('section', attrs={'id':'headlines'})
top_headline = headlines.find('a', attrs={'class':'fc-item__link', 'data-link-name':'article'})
article_url = top_headline['href']


# %% Top article page

article_page = get_and_soupify(article_url)

# Target:
# Within the first <div> tag with class 'content__article-body' ...
# all the <p> tags.

main_section = article_page.find('div', attrs={'class':'content__article-body'})
paragraphs = main_section.find_all('p')


# %% Article text

paragraph_texts = [p.get_text() for p in paragraphs]

print_output('\n'.join(paragraph_texts), 'Body text')


# %% Linked URLs

links = []

for p in paragraphs:
    a_tags = p.find_all('a')
    for a in a_tags:
        links.append(a['href'])

print_output('\n'.join(links), 'Linked URLs')
