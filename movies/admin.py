from django.contrib import admin
from .models import Movie,Actor,Review

class MovieAdmin(admin.ModelAdmin):
    list_filter = ('likes',)
    search_fields = ('name', 'likes','actors__firstname','actors__lastname')
    list_display = ('name', 'creationDate', 'watchCount', 'costummDisplay')

    def costummDisplay(self,obj):
        return str(obj.likes) + ' '+str(obj.creationDate)




# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Review)