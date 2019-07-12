from __future__ import unicode_literals

from django.contrib.auth import get_user_model
# Create your tests here.
from django.test import RequestFactory
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from tunga_profiles.models import UserProfile
from tunga_utils.constants import USER_TYPE_DEVELOPER


class TestUserProfile(APITestCase):

    def setUp(self):
        self.developer = get_user_model().objects.create_user(
            'developer', 'developer@example.com', 'secret',
            **dict(type=USER_TYPE_DEVELOPER)
        )

        self.factory = RequestFactory()

    def test_get_profile(self):
        url = reverse('profile-info')
        self.__create_profile(self.developer)
        # login user
        self.client.force_authenticate(user=self.developer)
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # User has a default badge of having an account
        self.assertEqual(data.get('tunga_badge'), 'Developer')

    def __create_profile(self, user):
        return UserProfile.objects.create(user=user)
