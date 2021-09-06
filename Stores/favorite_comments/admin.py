from django.contrib import admin
from favorite_comments.models import Comments,Favorite
# Register your models here.
admin.site.register(Comments)
admin.site.register(Favorite)