from setuptools import setup, find_packages

setup(
    name='paperpileConvert',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Converts PaperPile JSON exports into YAML suitable for Jekyll websites.',
    url='https://github.com/scrim-network/paperpileConvert',
    install_requires=['latexcodec'],
    author='Randy Miller',
    author_email='rsm5139@psu.edu'
)
