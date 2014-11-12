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

fullcalendar = Group([css, fullcalendar_js])

# Optional.
gcal_js = Resource(
    library,
    "gcal.js",
    depends=[fullcalendar_js, ])

locales = {
    "de": Resource(
        library,
        "lang/de.js",
        depends=[fullcalendar_js, ]),
    "fr": Resource(
        library,
        "lang/fr.js",
        depends=[fullcalendar_js, ]),
    "nl": Resource(
        library,
        "lang/nl.js",
        depends=[fullcalendar_js, ]),
    "es": Resource(
        library,
        "lang/es.js",
        depends=[fullcalendar_js, ]),
}
