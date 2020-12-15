from django.contrib import admin
from . import models

admin.site.register([
    models.Blog,
    models.Author,
    models.Entry
])