"""
referencesController.py

"""

from referenceFormatter import referenceFormatter
from referenceWriter import referenceWriter
import sets
import json
import operator
import os

class referencesController:
    def __init__(self, json, path):
        self.json = json
        self.data = []
        self.pub_dir = ""
        self.tags = False
        self.order = [1]
        self.path = path[:-7]
        self.writer = referenceWriter()
        return None


    def formatReferences(self):
        for item in self.json:
            ref = referenceFormatter(item)
            self.data.append(ref.get())
        return None


    def setTags(self, tags):
        self.tags = tags
        return None


    def writeReferences(self):
        self.sortReferences()
        self.writer.write(self.data, self.tags, self.path)
        return None


    def sortReferences(self):
        try:
            self.data = sorted(self.data, key = lambda k: (-int(k['published_date']), k['authors']))
        except:
            self.data = sorted(self.data, key = lambda k: (k['authors']))
        return None
