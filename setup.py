# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup
import os

version = u'2.3.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read(u'README.txt')
    + u'\n' +
    read(u'js', u'fullcalendar', u'test_fullcalendar.txt')
    + u'\n' +
    read(u'CHANGES.txt'))

setup(
    name=u'js.fullcalendar',
    version=version,
    description="Fanstatic packaging of FullCalendar",
    long_description=long_description,
    classifiers=[],
    keywords=u'',
    author=u'Andreas Kaiser',
    author_email=u'disko@binary-punks.com',
    url=u'https://github.com/Kotti/js.fullcalendar',
    license=u'BSD',
    packages=find_packages(),
    namespace_packages=[u'js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        u'fanstatic',
        u'js.jquery',
        u'js.momentjs',
        u'setuptools',
        ],
    entry_points={
        u'fanstatic.libraries': [
            u'fullcalendar = js.fullcalendar:library',
            ],
        },
    )
