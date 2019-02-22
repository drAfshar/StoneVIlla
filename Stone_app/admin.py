from django.contrib import admin
from . import models

@admin.register(models.BusinessUser)
class BusinessUserAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','username','email','kind_of_work' ,'pub_date' ,)
    list_filter=('kind_of_work','pub_date')

@admin.register(models.PostUser)
class PostUserAdmin(admin.ModelAdmin):
    list_display=('post_sharp','post_id',)
    list_filter=('post_sharp',)

@admin.register(models.UserComment)
class AdminUserComment(admin.ModelAdmin):
    list_display=('user','username' ,'display' ,'date_of_add')
    list_filter=('date_of_add',)

@admin.register(models.UserPageProperties)
class AdminUserPageProperties(admin.ModelAdmin):
    list_display=('user' ,'views' ,'city',)

@admin.register(models.Follower)
class AdminFollower(admin.ModelAdmin):
    list_display=('followed_user','follower_user','date_of_add')
    list_filter=('date_of_add',)

@admin.register(models.UserLike)
class AdminUserLike(admin.ModelAdmin):
    list_display=('liker_user','like_page' ,'like_comment' ,'like_post',)
