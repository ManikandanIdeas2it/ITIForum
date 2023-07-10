from django.db import models

# user -> id(AutoField), emp_id(CharField), name(CharField), createdat(IntegerField), CreatedDate(DateTimeField)
# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=30)
    user_mail_id = models.EmailField(max_length=254)

    def __str__(self):
        return self.user_name
    

# PostsCollection -> postid(AutoField), emp_id(CharField), text(CharField), Image(CharField),Categories(CharField),Like(IntegerField), Comment(CharField),Caption(CharField), createdat(IntegerField), CreatedDate(DateTimeField)
class PostsCollection(models.Model):
    emp_id = models.ForeignKey("Users", on_delete=models.DO_NOTHING)
    post_id = models.UUIDField(primary_key= True, editable= False) 
    post_category = models.CharField(max_length=50) 
    post_text = models.CharField(max_length=500)
    post_img = models.ImageField(upload_to='pics')
    post_caption = models.CharField(max_length=500)
    like_fk = models.IntegerField()
    comment_fk = models.CharField(max_length=500)
    date_posted = models.DateTimeField()
    date_last_modified = models.DateTimeField()

    def __str__(self):
        return self.post_text
