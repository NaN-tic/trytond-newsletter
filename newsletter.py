#This file is part newsletter module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields

__all__ = ['NewsletterList', 'NewsletterContact', 'NewsletterContactList']


class NewsletterList(ModelSQL, ModelView):
    'Newsletter List'
    __name__ = 'newsletter.list'
    name = fields.Char('Name', required=True)
    contacts = fields.Many2Many('newsletter.contact-newsletter.list',
        'newsletter_list', 'newsletter_contact', 'Contacts')
    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True


class NewsletterContact(ModelSQL, ModelView):
    'Newsletter Contact'
    __name__ = 'newsletter.contact'
    _rec_name = 'email'
    email = fields.Char('Email', required=True)
    name = fields.Char('Name')
    party = fields.Many2One('party.party', 'Party')
    lists = fields.Many2Many('newsletter.contact-newsletter.list',
        'newsletter_contact', 'newsletter_list', 'Lists')
    active = fields.Boolean('Active', select=True)

    @classmethod
    def __setup__(cls):
        super(NewsletterContact, cls).__setup__()
        cls._sql_constraints += [
            ('contact_uniq', 'UNIQUE(email)',
                'An email must be unique.'),
            ]
        cls._error_messages.update({
            'copy_dissable': 'Copy method is dissabled',
        })

    @staticmethod
    def default_active():
        return True

    @classmethod
    def copy(cls, contacts, default=None):
        cls.raise_user_error('copy_dissable')


class NewsletterContactList(ModelSQL):
    'Newsletter Contact - Newsletter List'
    __name__ = 'newsletter.contact-newsletter.list'
    _table = 'newsletter_contact_list_rel'
    newsletter_contact = fields.Many2One('newsletter.contact', 'Contact', ondelete='CASCADE',
            required=True, select=True)
    newsletter_list = fields.Many2One('newsletter.list', 'List',
        ondelete='CASCADE', required=True, select=True)
