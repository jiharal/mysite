from django.contrib import admin
from . import models

admin.site.register([
    models.Person,
    models.Mucisian,
    models.Membership,
    models.Group,
    models.Album
])