"""
referenceWriter.py
Randy Miller
rsm5139@psu.edu

"""

import os

class referenceWriter:
    """
    Writes references given to it by referencesController
    Input: None

    """

    def __init__(self):
        return None


    def write(self, data, tags, source_dir):
        for tag in tags:
            if not os.path.isdir(source_dir+"/"+tag):
                try:
                    os.makedirs(source_dir+"/"+tag)
                except:
                    continue
            #write individual files
            for dat in data:
                if 'labelsNamed'in dat and tag in dat['labelsNamed']:
                    file_handle = open(source_dir+"/"+tag+"/"+dat['citekey']+".md", 'w+')
                    file_handle.write("---\n")
                    file_handle.write("layout: single-bib-item\n")
                    file_handle.write("hidden: true\n")
                    for k, v in list(dat.items()):
                        self.writeField(file_handle, prefix=k+":", v=v, level=0)
                    file_handle.write("---")
                    file_handle.close()
            #write combined files
            file_handle = open(source_dir+"/"+tag+".md", 'w+')
            matched_list = []
            matched_list = [item for item in data if 'labelsNamed' in item and tag in item['labelsNamed']]
            file_handle.write("---\n")
            file_handle.write("title: "+tag+"\n")
            file_handle.write("hidden: true\n")
            self.writeField(file_handle, prefix="items:", v=matched_list, level=0)
            file_handle.write("---")
            file_handle.close()
        return None


    def writeField(self, file_handle, prefix="", v="", level=0):
        idt = " " * level
        if isinstance(v, str) or isinstance(v, int) or isinstance(v, float):
            file_handle.write(idt+prefix+' "'+v+str("\"\n"))
        else:
            file_handle.write(idt+prefix+"\n")
        if isinstance(v, list):
            level += 2
            for item in v:
                self.writeField(file_handle, prefix="-", v=item, level=level)
        elif isinstance(v, dict):
            level += 2
            idt = " " * level
            for key, value in list(v.items()):
                self.writeField(file_handle, prefix=key+":", v=value, level=level)
        else:
            pass
        return None
