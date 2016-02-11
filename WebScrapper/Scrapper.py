#!/bin/python3

import getopt
import sys
from datetime import datetime

import requests

from WebScrapper.Element import Element
from WebScrapper.Website import Website


def request_content(url, headers):
    try:
        response = requests.get(url, headers, verify=False)
    except requests.RequestException as e:
        return e
    if response.status_code == requests.codes.ok:
        print(datetime.now().strftime("%d/%m/%y %H:%M:%S") + " Request: " + url)
        return response.text
    else:
        print(datetime.now().strftime("%d/%m/%y %H:%M:%S") + " Fail: " + str(response.history) + " " + url)
        return None


def main(argv):
    url = None
    tag = None
    cls = None
    text = False
    href = False
    get_child = False
    try:
        opts, args = getopt.getopt(argv, "hu:t:c:g:text:href:", ["url=", "tag=", "class=", "get="])
    except getopt.GetoptError as e:
        print(e)
        print("Scrapper.py -u <url> -t <tag> -c <class> -g <text or href>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("Scrapper.py -u <url> -t <tag> -c <class> -g <text or href>")
            sys.exit()
        elif opt in ("-u", "--url"):
            url = arg
        elif opt in ("-t", "--tag"):
            tag = arg
        elif opt in ("-c", "--class"):
            cls = arg
        elif opt in ("-g", "--get"):
            get_child = True
            text = True if arg == "text" else False
            href = True if arg == "href" else False
    # Evaluates script params
    if url is not None:
        s = Scrapper(url)
        if get_child and tag is not None and cls is None:
            for child in s.content.get_child(tag):
                if text:
                    print(child.text)
                elif href and tag == "a":
                    child.tag = tag
                    print(child.href)
        elif get_child and tag is not None and cls is not None:
            for child in s.content.get_child(tag, cls):
                if text:
                    print(child.text)
                elif href and tag == "a":
                    child.tag = tag
                    child.classes = cls
                    print(child.href)
        elif tag is not None:
            s.content.tag = tag
            print(s.content.text)
        elif tag is not None and cls is not None:
            s.content.tag = tag
            s.content.classes = cls
            print(s.content.text)


class Scrapper(Website):
    def __init__(self, url):
        super().__init__(url)
        self.__site = Website(url)
        self.__request_header = {'user-agent': 'Mozilla/5.0 (X11; ; Linux i686; rv:1.9.2.20) Gecko/20110805'}

    @property
    def site(self):
        """
        Get url target
        :return: string
        """
        return self.__site.url

    @property
    def request_header(self):
        """
        Get request headers
        :return: dict
        """
        return self.__request_header

    @request_header.setter
    def request_header(self, value):
        """
        Set request headers
        :param value: dict
        :return:
        """
        self.__request_header = value

    @property
    def content(self):
        """
        Get response text
        :return: string
        """
        if self.site is not None:
            return Element(request_content(self.site, self.request_header))
        else:
            return None


if __name__ == '__main__':
    main(sys.argv[1:])
