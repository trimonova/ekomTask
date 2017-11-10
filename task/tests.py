from django.test import TestCase
from . import utils

# Create your tests here.

class UtilsTestCase(TestCase):

    def test_is_email_returns_true_if_email(self):
        email = 'trimonovds@gmail.com'
        self.assertTrue(utils.FieldTypeHelper.is_email(email))

    def test_is_email_returns_false_if_doesnt_contain_sobaka_symbol(self):
        email = 'trimonovdsgmail.com'
        self.assertFalse(utils.FieldTypeHelper.is_email(email))

    def test_is_email_correctly_works(self):
        valid_emails = ['email@domain.com', 'firstname.lastname@domain.com', 'email@subdomain.domain.com', 'firstname+lastname@domain.com']
        invalid_emails = ['plainaddress', 'email@domain@domain.com']
        for valid in valid_emails:
            self.assertTrue(utils.FieldTypeHelper.is_email(valid))
        for invalid in invalid_emails:
            self.assertFalse(utils.FieldTypeHelper.is_email(invalid))

