"""from django.contrib import admin
from .models import Imageai

# Register your models here.
admin.site.register(Imageai)"""

from django.contrib import admin
#from .models import ImageElement
from .models import TextElement


#admin.site.register(ImageElement)
admin.site.register(TextElement)