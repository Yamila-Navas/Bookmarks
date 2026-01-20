from django.contrib.auth.models import User
import requests
from django.core.files.base import ContentFile
from .models import Profile


class EmailAuthBackend:
    """
    Backend de autenticación custom.
    Sirve para loguearse con email en vez de username.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        



def create_profile(backend, user, *args, **kwargs):
    if backend.name == 'google-oauth2':
        photo_url = response.get('picture')

        profile, created = Profile.objects.get_or_create(user=user)

        if created:
            response = kwargs.get('response')
            if photo_url and not profile.photo:
                image = requests.get(photo_url)
                profile.photo.save(
                    f'{user.username}_google.jpg',
                    ContentFile(image.content),
                    save=True
                )

