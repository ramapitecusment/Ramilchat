import re
import socket
from urllib import robotparser
from urllib.parse import urljoin, urlparse
from downloader import Downloader
from lxml.html import fromstring

socket.setdefaulttimeout(60)


def get_robots_parser(robots_url):
    " Return the robots parser object using the robots_url "
    try:
        rp = robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp
    except Exception as e:
        return 'Error finding robots_url:', robots_url, e


def get_links(html):
    """ Using lxml and xpath to extract data from country pages. """
    tree = fromstring(html)
    position = tree.xpath('///span[@class = "uccResultAmount"]/text()')
    return position

def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp',
                 proxies=None, delay=3, max_depth=2, num_retries=2, cache={}, scraper_callback=None):
    """ Crawl from the given start URL following links matched by link_regex. In the current
        implementation, we do not actually scrapy any information.

        args:
            start_url (str or list of strs): web site(s) to start crawl
            link_regex (str): regex to match for links
        kwargs:
            robots_url (str): url of the site's robots.txt (default: start_url + /robots.txt)
            user_agent (str): user agent (default: wswp)
            proxies (list of dicts): a list of possible dicts for http / https proxies
                For formatting, see the requests library
            delay (int): seconds to throttle between requests to one domain (default: 3)
            max_depth (int): maximum crawl depth (to avoid traps) (default: 4)
            num_retries (int): # of retries when 5xx error (default: 2)
            cache (dict): cache dict with urls as keys and dicts for responses (default: {})
            scraper_callback: function to be called on url and html content
    """
    if isinstance(start_url, list):
        crawl_queue = start_url
    else:
        crawl_queue = [start_url]
    # keep track which URL's have seen before
    seen, robots = {}, {}
    D = Downloader(delay=delay, user_agent=user_agent, proxies=proxies, cache=cache)
    while crawl_queue:
        url = crawl_queue.pop()
        no_robots = False
        if 'http' not in url:
            continue
        domain = '{}://{}'.format(urlparse(url).scheme, urlparse(url).netloc)
        rp = robots.get(domain)
        if not rp and domain not in robots:
            robots_url = '{}/robots.txt'.format(domain)
            rp = get_robots_parser(robots_url)
            if not rp:
                # issue finding robots.txt, still crawl
                no_robots = True
            robots[domain] = rp
        elif domain in robots:
            no_robots = True
        # check url passes robots.txt restrictions
        if no_robots or rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                return 'Skipping %s due to depth' % url
                continue
            html = D(url, num_retries=num_retries)
            if not html:
                continue
            if scraper_callback:
                links = scraper_callback(url, html) or []
            else:
                links = []
            # filter for links matching our regular expression
            #datas = []
            #for link in get_links(html) + links:
            #    datas.append(link)
            #return datas
            #print(html)
            return get_links(html)

        else:
            return 'Blocked by robots.txt:', url


def amount_of_money(entities, entity, values):
    try:
        if entity == 'amount_of_money':
            return "You entered: " + values[entities.index(entity)]
        elif entity == 'currency_1':
            what = str(values[entities.index('currency_1')]).split(' ')
            to = str(values[entities.index('currency_2')])
            site = 'https://www.xe.com/currencyconverter/convert/?Amount=%s&From=%s&To=%s' % (what[0], what[1], to)
            return str(str(what[0]) + " " + str(what[1]) + " in " + str(to) + " = " + str(link_crawler(site, '')[0]))

    except:
        pass