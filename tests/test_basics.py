import unittest
import os
import shutil
from paperpileConvert import *

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        convert(['scrim_publications', 'clima_publications'], 'tests/paperpile.json', path=os.getcwd()+'/tests')

    def tearDown(self):
        os.remove(os.getcwd()+'/tests/scrim_publications.md')
        os.remove(os.getcwd()+'/tests/clima_publications.md')
        shutil.rmtree(os.getcwd()+'/tests/scrim_publications')
        shutil.rmtree(os.getcwd()+'/tests/clima_publications')

    def test_files_exist(self):
        files = ['scrim_publications.md', 'clima_publications.md', 'scrim_publications/Hargreaves2013-py.md', 'clima_publications/Hargreaves2013-py.md', 'clima_publications/Christianson2013-ej.md', 'clima_publications/Kozar2013-du.md', 'clima_publications/Kozar2013-sd.md']
        for f in files:
            self.assertTrue(os.path.isfile(os.getcwd()+'/tests/'+f))

    def test_files_not_exist(self):
        files = ['scrim_publications/Christianson2013-ej.md', 'other_non-supported_references.md', 'other_non-supported_references/Thrasher2013-tx.md']
        for f in files:
            self.assertFalse(os.path.isfile(os.getcwd()+'/tests/'+f))

    def test_CO2s(self):
        f = open(os.getcwd()+'/tests/scrim_publications.md')
        text = f.read()
        f.close()
        self.assertTrue('test1CO<sub>2</sub>' in text)
        self.assertTrue('test2CO<sub>2</sub>' in text)
        self.assertFalse('CO2' in text)
        self.assertFalse('CO$_2$' in text)
        self.assertFalse('CO$^2$' in text)

    def test_correct_tag_usage(self):
        f = open(os.getcwd()+'/tests/scrim_publications.md')
        text = f.read()
        f.close()
        self.assertTrue('Hargreaves2013-py' in text)
        self.assertFalse('Christianson2013-ej' in text)
