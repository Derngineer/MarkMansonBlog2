from django.contrib import admin
from .models import User, Article,Comment


# Register your models here.
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)



class CommentAdmin(admin.ModelAdmin):
	list_display = ('name','body','Article',)
	list_filter =('active','date_posted',)
	search_fields = ('name', 'body')
	actions = ['approve_comments']

	def approve_comments(self,request,queryset):
		queryset.update(active = True)


