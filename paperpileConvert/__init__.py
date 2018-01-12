import json
import os
from sys import *
if 3 == version_info.major:
    from .python_3_x import referencesController
    from .python_3_x import referenceFormatter
    from .python_3_x import referenceWriter
else:
    from python_2_x import referencesController
    from python_2_x import referenceFormatter
    from python_2_x import referenceWriter

__all__ = ["convert"]

def convert(tags,fname,path=os.getcwd()):
    with open(fname) as f:
        data = json.load(f)
    f.close()
    print(os.getcwd())
    converted = referencesController(data,path)
    converted.formatReferences()
    converted.setTags(tags)
    converted.writeReferences()
    return None
