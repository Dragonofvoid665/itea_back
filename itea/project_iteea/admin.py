from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(Vacansy)
class VacansyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_ru', 'title_en', 'title_tm','description_ru','description_en','description_tm', 'picture','company_name','phone_number','email']
    def picture(self, obj:Vacansy):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" >')
        except:
            return None
@admin.register(Course_Category)
class Course_CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price','picture']
    filter_horizontal = ('course',)
    def picture(self, obj:Course_Category):
        try:
            return format_html(f'<img src="{obj.image.url}" widt="150px" height="150px" >')
        except:
            return None
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_en', 'name_ru', 'name_tm', 'description_en', 'description_ru', 'description_tm', 'price', 'duration']
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_en', 'name_ru', 'name_tm', 'picture','role','colour']
    def picture(self, obj:Team):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None

@admin.register(News_email)
class News_emailAdmin(admin.ModelAdmin):
    list_display = ['id','email']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_en', 'title_ru', 'title_tm', 'content_en', 'content_ru', 'content_tm','date_published','picture','places','ordered_places']
    filter_horizontal = ('new_email',)
    def picture(self, obj:Team):
        try:
            return format_html(f'<img src="{obj.image.url}" width="150px" height="150px" />')
        except:
            return None