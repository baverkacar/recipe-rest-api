from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse 


class AdminSiteTests(TestCase):

    """Setup is gonna consist my test client. I am going to add a new user 
        that we can use to test ı am going to make sure the user is logged into client
        and finally ı am going to create a regular user that is not authenticated or 
        that we can use to list in my admin page"""
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='baverkacar@gmail.com',
            password='asdasd123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='testuser@gmail.com',
            password='asdasd123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        """ assertContains checks HTTP 200 and that it looks into 
        the actual content of this res. """
        self.assertContains(response, self.user.name) 
        self.assertContains(response, self.user.email)

    def test_user_change_page(self):
        """Test that user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # Sample url: /admin/core/user/{id}  
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        

