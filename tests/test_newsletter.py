# This file is part of the newsletter module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class NewsletterTestCase(ModuleTestCase):
    'Test Newsletter module'
    module = 'newsletter'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        NewsletterTestCase))
    return suite