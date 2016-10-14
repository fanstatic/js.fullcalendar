from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from fanstatic.core import render_print_css
from js.jquery import jquery
from js.momentjs import moment


library = Library('js.fullcalendar', 'resources')

fullcalendar_css = Resource(
    library,
    'fullcalendar.css',
    minified='fullcalendar.min.css')

fullcalendar_print_css = Resource(
    library,
    'fullcalendar.print.css',
    depends=[fullcalendar_css, ],
    renderer=render_print_css)

css = Group([fullcalendar_css, fullcalendar_print_css, ])

fullcalendar_js = Resource(
    library,
    'fullcalendar.js',
    depends=[jquery, moment],
    minified='fullcalendar.min.js')

lang_all_js = Resource(
    library,
    'lang-all.js',
    depends=[fullcalendar_js])

fullcalendar = Group([css, fullcalendar_js])

# Optional.
gcal_js = Resource(
    library,
    'gcal.js',
    depends=[fullcalendar_js, ])

locales = {}

for lang in ('ar-ma.js', 'ar-sa.js', 'ar-tn.js', 'ar.js', 'bg.js',
             'ca.js', 'cs.js', 'da.js', 'de-at.js', 'de.js', 'el.js',
             'en-au.js', 'en-ca.js', 'en-gb.js', 'en-ie.js', 'en-nz.js',
             'es.js', 'eu.js', 'fa.js', 'fi.js', 'fr-ca.js', 'fr-ch.js',
             'fr.js', 'gl.js', 'he.js', 'hi.js', 'hr.js', 'hu.js',
             'id.js', 'is.js', 'it.js', 'ja.js', 'ko.js', 'lb.js',
             'lt.js', 'lv.js', 'nb.js', 'nl.js', 'nn.js', 'pl.js',
             'pt-br.js', 'pt.js', 'ro.js', 'ru.js', 'sk.js', 'sl.js',
             'sr-cyrl.js', 'sr.js', 'sv.js', 'th.js', 'tr.js', 'uk.js',
             'vi.js', 'zh-cn.js', 'zh-tw.js', ):
    locales[lang] = Resource(
        library,
        'lang/{0}'.format(lang),
        depends=[fullcalendar_js, ])
