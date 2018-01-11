from sys import *
if 3 == version_info.major:
    from python_3_x import referencesController
    from python_3_x import referenceFormatter
    from python_3_x import referenceWriter
else:
    from python_2_x import referencesController
    from python_2_x import referenceFormatter
    from python_2_x import referenceWriter

def convert(tags,file):
    print('hello')
