# -*- coding: utf-8 -*-

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from js.jquery import jquery


library = Library("js.fullcalendar", "resources")

fullcalendar_css = Resource(
    library,
    "fullcalendar.css",
    minified="fullcalendar.min.css")

fullcalendar_print_css = Resource(
    library,
    "fullcalendar.print.css",
    depends=[fullcalendar_css, ],
    minified="fullcalendar.print.min.css")

fullcalendar_js = Resource(
    library,
    "fullcalendar.js",
    depends=[jquery, ],
    minified="fullcalendar.min.js")

gcal_js = Resource(
    library,
    "gcal.js",
    depends=[fullcalendar_js, ],
    minified="gcal.min.js")

locales = {
    "de": Resource(
        library,
        "fullcalendar_de.js",
        depends=[fullcalendar_js, ],
        minified="fullcalendar_de.min.js"),
    "en": Resource(
        library,
        "fullcalendar_en.js",
        depends=[fullcalendar_js, ],
        minified="fullcalendar_en.min.js"),
}

css = Group([fullcalendar_css, fullcalendar_print_css, ])
js = Group([fullcalendar_js, gcal_js, ])

fullcalendar = Group([css, js, ])
