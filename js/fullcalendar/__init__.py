from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from fanstatic.core import render_print_css
from js.jquery import jquery
from js.momentjs import moment


library = Library("js.fullcalendar", "resources")

fullcalendar_css = Resource(
    library,
    "fullcalendar.css",
    minified="fullcalendar.min.css")

fullcalendar_print_css = Resource(
    library,
    "fullcalendar.print.css",
    depends=[fullcalendar_css, ],
    renderer=render_print_css)

css = Group([fullcalendar_css, fullcalendar_print_css, ])

fullcalendar_js = Resource(
    library,
    "fullcalendar.js",
    depends=[jquery, moment],
    minified="fullcalendar.min.js")

lang_all_js = Resource(
    library,
    "lang-all.js",
    depends=[fullcalendar_js])

fullcalendar = Group([css, fullcalendar_js])

# Optional.
gcal_js = Resource(
    library,
    "gcal.js",
    depends=[fullcalendar_js, ])

locales = {}

for lang in ('ar-ma', 'ar-sa', 'ar', 'bg', 'ca', 'cs', 'da', 'de-at', 'de',
             'el', 'en-au', 'en-ca', 'en-gb', 'es', 'fa', 'fi', 'fr-ca', 'fr',
             'hi', 'hr', 'hu', 'id', 'is', 'it', 'ja', 'ko', 'lt', 'lv', 'nl',
             'pl', 'pt-br', 'pt', 'ro', 'ru', 'sk', 'sl', 'sr-cyrl', 'sr',
             'sv', 'th', 'tr', 'uk', 'vi', 'zh-cn', 'zh-tw'):
    locales[lang] = Resource(
        library,
        "lang/{}.js".format(lang),
        depends=[fullcalendar_js, ])
