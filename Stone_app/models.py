from django.db import models
import uuid


class BusinessUser(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=12 ,primary_key=True)
    password=models.CharField(max_length=18)
    mobile=models.CharField(max_length=20)
    email=models.CharField(max_length=50 ,blank=True)
    business_address=models.CharField(max_length=200)
    office_number=models.CharField(max_length=50 ,blank=True ,null=True)
    user_image = models.ImageField(blank=True ,null=True, upload_to = 'Stone_app/Media/Image/Stone_app/User_Image', default = 'Stone_app/Image/Stone_app/User_Image/no-img.jpg')
    pub_date=models.DateField(auto_now=True)
    KIND_OF_WORK =(
    ('SC','سنگبری'),
    ('SG','سنگ قیچی'),
    ('CNC','CNC'),
    )
    kind_of_work=models.CharField(max_length=3 ,choices=KIND_OF_WORK ,blank=True ,default='SC')

    def __str__(self):
        return '%s ,%s ,%s ,%s ,%s' % (self.first_name ,self.last_name ,self.email ,self.kind_of_work ,self.pub_date)




class PostUser(models.Model):
    post_id=models.AutoField(primary_key=True)
    business_user=models.ForeignKey('BusinessUser' ,on_delete=models.SET_NULL ,null=True)
    post_text=models.TextField(max_length=500)
    post_picture=models.ImageField(blank=True , null=True ,upload_to='Stone_app/Media/Image/Stone_app/Posts_Images' ,default='Stone_app/Media/Image/Stone_app/Posts_Images/no-img.jpg')
    post_video=models.FileField(blank=True , null=True ,upload_to='Stone_app/Media/Video/Stone_app/Post_Video' , default='Stone_app/Media/Video/Stone_app/Post_Video')
    post_sharp=models.CharField(max_length=30 , blank=True ,null=True)
    date_of_add=models.DateTimeField(auto_now=False ,auto_now_add=True)

    def __str__(self):
        return '%s ,%s ,%s ,%s' % (self.post_text ,self.post_sharp ,self.date_of_add ,self.post_id)

class meta:
    ordering=["-date_of_add"]


class UserComment(models.Model):
    user=models.ForeignKey('BusinessUser' ,on_delete=models.SET_NULL ,null=True)
    comment_id=models.AutoField(primary_key=True)
    comment=models.TextField(max_length=200)
    username=models.CharField(max_length=12)
    date_of_add=models.DateTimeField(auto_now=True)
    DISPLAY_COMMENT=(
    ('show','نمایش نظر'),
    ('hide','حذف نظر')
    )
    display=models.CharField(max_length=4 ,choices=DISPLAY_COMMENT ,default='show' ,blank=True)

    def __str__(self):
        return '%s ,%s ,%s ,%s' % (self.comment ,self.display ,self.username ,self.date_of_add)

    def getdgree(self):
        return user.objects.filter(degree=self)


class meta:
    ordering=['-date_of_add']


class UserPageProperties(models.Model):
    user=models.ForeignKey('BusinessUser',on_delete=models.SET_NULL ,null=True)
    views=models.IntegerField(default=0)
    bio=models.TextField(max_length=300 ,blank=True ,null=True)
    Profile_Image = models.ImageField(blank=True ,null=True ,upload_to= 'Stone_app/Media/Image/Stone_app/Profile_Image',name='', default = 'Stone_app/Media/Image/Stone_app/Profile_Image/no-img.jpg')
    notifics=models.TextField(max_length=200 ,blank=True ,null=True)
    CITY=(
    ('other','سایر'),
    ('Esfahan','اصفهان'),
    ('NajafAbad','نجف آباد'),
    ('Tiran','تیران'),
    ('RezvanCity','رضوانشهر'),
    )
    city=models.CharField(max_length=30,choices=CITY ,default='other' ,blank=True)

    def getdgree(self):
        return user.objects.filter(degree=self)

    def __str__(self):
        return '%s ,%s ,%s ' % (self.views ,self.bio ,self.city)



class Follower(models.Model):
    follower_user=models.CharField(max_length=12)
    followed_user=models.CharField(max_length=12)
    date_of_add=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s ,%s ,%s' % (self.follower_user ,self.followed_user ,self.date_of_add)



class UserLike(models.Model):
    liker_user=models.ForeignKey( 'BusinessUser' ,on_delete=models.SET_NULL , null=True)
    like_page=models.IntegerField(default=0)
    like_post=models.IntegerField(default=0)
    post_id=models.IntegerField(blank=True ,null=True)
    like_comment=models.IntegerField(default=0)
    comment_id=models.IntegerField(blank=True ,null=True)
    username=models.CharField(max_length=12)

    def __str__(self):
        return '%s,%s,%s,%s' % (self.like_page ,self.like_post ,self.like_comment ,self.username)

    def getdgree(self):
        return liker_user.objects.filter(degree=self)
