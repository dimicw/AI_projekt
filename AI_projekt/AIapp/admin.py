"""from django.contrib import admin
from .models import Imageai

# Register your models here.
admin.site.register(Imageai)"""

from django.contrib import admin
#from .models import ImageElement
from .models import TextElement
from .models import GeminiTextElement


#admin.site.register(ImageElement)
admin.site.register(TextElement)
admin.site.register(GeminiTextElement)