__author__ = 'Dmitriy'

import urllib.request
from src.Solvers.Helpers.UrlParser import UrlParser
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def __init__(self, strict = False):
        super(MyHTMLParser, self).__init__(strict=False)
        self.__html_structure = []

    def handle_starttag(self, tag, attrs):
        self.__html_structure.append(("start_tag", (tag.lower(), [])))
        for attr in attrs:
            self.__html_structure[-1][1][1].append(("attr", (attr[0].lower(), attr[1].lower())))

    def handle_endtag(self, tag):
        self.__html_structure.append(("end_tag", tag.lower()))

    def handle_data(self, data):
        self.__html_structure.append(("data", data.lower()))

    def handle_comment(self, data):
        self.__html_structure.append(("comment", data.lower()))

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        self.__html_structure.append(("named_ent", c.lower()))

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        self.__html_structure.append(("num_ent", c.lower()))

    def handle_decl(self, data):
        self.__html_structure.append(("decl", data.lower()))

    def get_html_structure(self):
        return self.__html_structure

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
        page_code = response.read().decode("utf-8")
        self.__parser.feed(page_code)
        print(self.__parser.get_html_structure())
        return page_code