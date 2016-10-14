from setuptools import find_packages
from setuptools import setup
import os

version = '2.9.1'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.txt') + '\n' +
    read('js', 'fullcalendar', 'test_fullcalendar.txt') + '\n' +
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
    url='https://github.com/Kotti/js.fullcalendar',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery>=1.7.1',
        'js.momentjs>=2.5.0',
        'setuptools',
    ],
    entry_points={
        'fanstatic.libraries': [
            'fullcalendar = js.fullcalendar:library',
        ],
    },
)
