from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from accounts.models import Account
from profiles.models import Profile


class ProfileTestMixin(TestCase):
    def setUp(self):
        self.account = Account.objects.create_user(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='john.m.doe@gmail.com',
            password='top_secret'
        )

        self.profile = Profile.objects.create(
            account=self.account,
            title='The John Doe Home Page',
            bio='this is a little somthing about me'
        )

    def authenticate_account(self):
        token = Token.objects.create(user=self.account)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)


class AccessProfileTest(APITestCase, ProfileTestMixin):
    def test_cannot_access_profile_information_when_not_authenticated(self):
        response = self.client.get('/api/v1/profiles/')

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_access_profile_when_authenticated(self):
        self.authenticate_account()

        response = self.client.get('/api/v1/profiles/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_can_view_profile_data(self):
        self.authenticate_account()

        response = self.client.get('/api/v1/profiles/')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.profile.title)
        self.assertContains(response, self.profile.bio)


class UpdateProfileTitleTest(APITestCase, ProfileTestMixin):
    def test_cannot_update_title_when_not_authenticated(self):
        post_data = {
            'title': 'New Title'
        }

        response = self.client.patch('/api/v1/profiles/', post_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cannot_update_title_when_blank(self):
        self.authenticate_account()

        post_data = {
            'title': ''
        }

        response = self.client.patch('/api/v1/profiles/%s/' % self.profile.id , post_data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['title'][0], 'This field may not be blank.')

    def test_can_update_title(self):
        self.authenticate_account()

        updated_title = 'New Title'
        post_data = {
            'title': updated_title
        }

        response = self.client.patch('/api/v1/profiles/%s/' % self.profile.id , post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(updated_title, updated_profile.title)


class UpdateProfileBioTest(APITestCase, ProfileTestMixin):
    def test_cannot_update_bio_when_not_authenticated(self):
        post_data = {
            'bio': 'New Bio'
        }

        response = self.client.patch('/api/v1/profiles/', post_data)

        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_update_bio(self):
        self.authenticate_account()

        updated_bio = 'New Bio'
        post_data = {
            'bio': updated_bio
        }

        response = self.client.patch('/api/v1/profiles/%s/' % self.profile.id , post_data)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        updated_profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(updated_bio, updated_profile.bio)
