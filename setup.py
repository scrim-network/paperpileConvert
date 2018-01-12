from setuptools import setup, find_packages

setup(
    name='paperpileConvert',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Converts PaperPile JSON exports into YAML suitable for Jekyll websites.',
    url='https://github.com/rsm5139/paperpileConvert',
    install_requires=['latexcodec'],
    author='Randy Miller',
    author_email='rsm5139@psu.edu'
)
