# coding: utf-8
import requests
from lxml import html
import urlparse
import smtplib


class Avito:

    MAX_SUM = 2500000
    MIN_SUM = 1400000

    RESULT = []

    
