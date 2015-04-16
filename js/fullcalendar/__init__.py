# -*- coding: utf-8 -*-

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from fanstatic.core import render_print_css
from js.jquery import jquery
from js.momentjs import moment


library = Library(u'js.fullcalendar', u'resources')

fullcalendar_css = Resource(
    library,
    u'fullcalendar.css',
    minified=u'fullcalendar.min.css')

fullcalendar_print_css = Resource(
    library,
    u'fullcalendar.print.css',
    depends=[fullcalendar_css, ],
    renderer=render_print_css)

css = Group([fullcalendar_css, fullcalendar_print_css, ])

fullcalendar_js = Resource(
    library,
    u'fullcalendar.js',
    depends=[jquery, moment],
    minified=u'fullcalendar.min.js')

lang_all_js = Resource(
    library,
    u'lang-all.js',
    depends=[fullcalendar_js])

fullcalendar = Group([css, fullcalendar_js])

# Optional.
gcal_js = Resource(
    library,
    u'gcal.js',
    depends=[fullcalendar_js, ])

locales = {}

for lang in (u'ar-ma', u'ar-sa', u'ar', u'bg', u'ca', u'cs', u'da', u'de-at',
             u'de', u'el', u'en-au', u'en-ca', u'en-gb', u'es', u'fa', u'fi',
             u'fr-ca', u'fr', u'hi', u'hr', u'hu', u'id', u'is', u'it', u'ja',
             u'ko', u'lt', u'lv', u'nl', u'pl', u'pt-br', u'pt', u'ro', u'ru',
             u'sk', u'sl', u'sr-cyrl', u'sr', u'sv', u'th', u'tr', u'uk',
             u'vi', u'zh-cn', u'zh-tw'):
    locales[lang] = Resource(
        library,
        u'lang/{0}.js'.format(lang),
        depends=[fullcalendar_js, ])
