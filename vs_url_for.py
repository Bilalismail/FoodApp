from flask import url_for

URL_PREFIX = '/usr/323'

def vs_url_for(view):
    url = url_for(view)
    url = URL_PREFIX + url
    return url
