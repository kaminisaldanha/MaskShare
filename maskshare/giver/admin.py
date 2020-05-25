from django.contrib import admin

from .models import Giver
from .models import Mask

admin.site.register(Giver)
admin.site.register(Mask)
