"""
referenceFormatter.py
Randy Miller
rsm5139@psu.edu

"""
from json import *
import re
import codecs
import latexcodec


class referenceFormatter:
    """
    Formats references given to it by referencesController
    Input:
      - item:
          type: dict

    """

    def __init__(self, item):
        self.item = item
        self.formatted = {}
        self.setFields()
        return None


    def cleanString(self, string):
        string = codecs.decode(str(string), 'ulatex')
        string = re.sub(r'\$_(.*?)\$', r'<sub>\1</sub>', string)
        string = re.sub(r'\$\^(.*?)\$', r'<sup>\1</sup>', string)
        string = string.replace('CO2', 'CO<sub>2</sub>')
        string = string.replace('{', '')
        string = string.replace('}', '')
        string = string.replace('"', "\\\"")
        return string


    def get(self):
        return self.formatted


    def setFields(self):
        for key, value in list(self.item.items()):
            self.formatted[str(key)] = self.format(value)
        #special cases
        if 'author' in self.item:
            self.formatted['authors'] = self.name('author', self.item['author'])
        elif 'editor' in self.item:
            self.formatted['authors'] = self.name('editor', self.item['editor'])
        else:
            self.formatted['authors'] = self.item['title'][:4]
        if 'published' in self.item:
            self.formatted['published_date'] = self.date('published', self.item['published'])
        else:
            self.formatted['published_date'] = "0"
        return None


    def format(self, value):
        fmat = value
        if isinstance(fmat, list):
            fmat = []
            for item in value:
                fmat.append(self.format(item))
        elif isinstance(fmat, dict):
            fmat = {}
            for key, val in list(value.items()):
                fmat[str(key)] = self.format(val)
        else:
            fmat = self.cleanString(fmat)
        return fmat


    def name(self, key, value):
        authors = ""
        n = len(value)
        for ind, name in enumerate(value, start=0):
            if str(ind) == "0":
                try:
                    authors += name['collective']
                except:
                    try:
                        authors += name['last']+", "+name['initials']
                    except:
                        authors += name['initials']
            elif str(ind+1) == str(n):
                try:
                    authors += " and "+name['initials']+" "+name['last']
                except:
                     authors += " and "+name['initials']
            else:
                try:
                    authors += ", "+name['initials']+" "+name['last']
                except:
                    authors += ", "+name['initials']
        return authors


    def date(self, key, value):
        return value['year']
