from django.test import TestCase
from django.contrib.auth import get_user_model #models yerine burada import ettik


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is succesful"""
        email = 'test@testingemail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email, email)

        # check password fonksiyonu get_user_modelda var ve bool değer döndürüyor.
        self.assertTrue(user.check_password(password)) 

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        # controlling case sensitive 
        self.assertEqual(user.email, email.lower()) 

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        # value error varsa bu kod bloğunun içine giriyor
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Tesst creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@asdasd.com',
            'test123'
        )

        self.assertTrue(user.is_superuser) # Permission mixinle geliyor bu
        self.assertTrue(user.is_staff)
