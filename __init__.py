# This file is part newsletter module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import newsletter

def register():
    Pool.register(
        newsletter.NewsletterList,
        newsletter.NewsletterContact,
        newsletter.NewsletterContactList,
        module='newsletter', type_='model')
