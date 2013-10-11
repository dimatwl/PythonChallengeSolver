__author__ = 'Dmitriy'

import urllib.request
from src.Solvers.Helpers.UrlParser import UrlParser
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag:", tag)
        for attr in attrs:
            print("     attr:", attr)
    def handle_endtag(self, tag):
        print("End tag  :", tag)
    def handle_data(self, data):
        print("Data     :", data)
    def handle_comment(self, data):
        print("Comment  :", data)
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)
    def handle_decl(self, data):
        print("Decl     :", data)

class UrlFetcher:
    def __init__(self, url_parser):
        if isinstance(url_parser, UrlParser):
            self.__url_parser = url_parser
            self.__parser = MyHTMLParser(strict=False)
        else:
            raise ValueError("url_parser isn't instance of UrlParser.")

    def fetch_url(self):
        request = urllib.request.Request(self.__url_parser.get_url())
        response = urllib.request.urlopen(request)
        page_code = response.read()
        self.__parser.feed(str(page_code))
        return page_code