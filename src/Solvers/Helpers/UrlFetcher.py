__author__ = 'Dmitriy'

import urllib.request
from src.Solvers.Helpers.UrlParser import UrlParser
from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def __init__(self, strict = False):
        self.__start_tag = "start_tag"
        self.__attribute = "attribute"
        self.__end_tag = "end_tag"
        self.__data = "data"
        self.__comment = "comment"
        self.__entity_reference = "entity_reference"
        self.__character_reference = "character_reference"
        self.__declaration = "declaration"

        super(MyHTMLParser, self).__init__(strict=False)
        self.__html_structure = []

    def handle_starttag(self, tag, attrs):
        self.__html_structure.append((self.__start_tag, (tag.lower(), [])))
        for attr in attrs:
            self.__html_structure[-1][1][1].append((self.__attribute, (attr[0].lower(), attr[1].lower())))

    def handle_endtag(self, tag):
        self.__html_structure.append((self.__end_tag, tag.lower()))

    def handle_data(self, data):
        self.__html_structure.append((self.__data, data.lower()))

    def handle_comment(self, data):
        self.__html_structure.append((self.__comment, data.lower()))

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        self.__html_structure.append((self.__entity_reference, c.lower()))

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        self.__html_structure.append((self.__character_reference, c.lower()))

    def handle_decl(self, data):
        self.__html_structure.append((self.__declaration, data.lower()))

    def get_html_structure(self):
        return self.__html_structure

    def get_data_for_tag(self, tag):
        result = []
        if isinstance(tag, str):
            for i in range(len(self.__html_structure)):
                aone = self.__html_structure[i][0]
                atwo = self.__html_structure[i][1][0]
                if self.__html_structure[i][0] == self.__start_tag and self.__html_structure[i][1][0] == tag:
                    j = i
                    aone = self.__html_structure[j][0]
                    atwo = self.__html_structure[j][1][0]
                    while self.__html_structure[j][0] != self.__end_tag or self.__html_structure[j][1][0] != tag and self.__html_structure[j][0] != self.__start_tag:
                        if self.__html_structure[j][0] == self.__data:
                            result.append(self.__html_structure[j][1])
                            break
                        j += 1
        else:
            raise ValueError("tag is not a string.")
        return result

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
        return page_code