import os
from setuptools import setup, find_packages

def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''
    

setup(
    name='norilog',
    version='1.0.0',
    description='The NoriLog web application.',
    long_description=read_file('README.rst'),
    author='',
    author_email='',
    url='https://github.com//norilog/',
    classifiers=[
        'Development Status :: 4 - Bata',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD Lisense',
        'Programing Langeage :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    keywords=['web', 'norilog'],
    license='BSD License',
    install_requires=[
        'Flask',
    ],
    entry_points="""
    [console_scripts]
    norilog = norilog:main
    """,
)