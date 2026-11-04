from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class AccountFlowTests(TestCase):
    def test_signup_shows_success_message(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newmember",
                "email": "newmember@example.com",
                "password1": "StrongPass!8472",
                "password2": "StrongPass!8472",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("login"))
        self.assertContains(response, "Your account was created successfully")
        self.assertTrue(get_user_model().objects.filter(username="newmember").exists())

    def test_profile_update_changes_only_signed_in_user(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username="member",
            password="StrongPass!8472",
            first_name="Before",
        )
        other_user = user_model.objects.create_user(
            username="other",
            password="StrongPass!8472",
            first_name="Other",
        )
        self.client.force_login(user)

        response = self.client.post(
            reverse("profile"),
            {
                "username": "member",
                "email": "member@example.com",
                "first_name": "Updated",
                "last_name": "Member",
                "course": "Computing",
                "role": user_model.Role.ADMIN,
            },
        )

        self.assertRedirects(response, reverse("dashboard"))
        user.refresh_from_db()
        other_user.refresh_from_db()
        self.assertEqual(user.first_name, "Updated")
        self.assertEqual(user.course, "Computing")
        self.assertEqual(user.role, user_model.Role.STUDENT)
        self.assertEqual(other_user.first_name, "Other")

    def test_profile_requires_login(self):
        response = self.client.get(reverse("profile"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('profile')}",
        )
