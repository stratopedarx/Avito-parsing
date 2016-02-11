# coding: utf-8
import requests
from lxml import html
import urlparse
import smtplib


class Avito:

    MAX_SUM = 2500000
    MIN_SUM = 1400000

    RESULT = []

    url = "https://www.avito.ru/dzerzhinsk/kvartiry/prodam/2-komnatnye/vtorichka?bt=0&f=59_13988b"
    r = requests.get(url)
    res = html.fromstring(r.content)