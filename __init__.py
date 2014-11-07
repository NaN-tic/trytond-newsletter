# This file is part newsletter module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .newsletter import *

def register():
    Pool.register(
        NewsletterList,
        NewsletterContact,
        NewsletterContactList,
        module='newsletter', type_='model')
