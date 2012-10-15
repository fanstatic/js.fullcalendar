# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup
import os

version = '1.5.4'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'fullcalendar', 'test_fullcalendar.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.fullcalendar',
    version=version,
    description="Fanstatic packaging of FullCalendar",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/js.fullcalendar',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'fullcalendar = js.fullcalendar:library',
            ],
        },
    )
