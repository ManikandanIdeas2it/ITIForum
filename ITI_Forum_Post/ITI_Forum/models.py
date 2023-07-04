from django.db import models

# user -> id(AutoField), emp_id(CharField), name(CharField), createdat(IntegerField), CreatedDate(DateTimeField)
# Create your models here.
class User(models.Model):
    emp_id = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    createdat = models.IntegerField()
    createddate = models.DateTimeField()

    def __str__(self):
        return self.name

# Postdata -> postid(AutoField), emp_id(CharField), text(CharField), Image(CharField),Categories(CharField),Like(IntegerField), Comment(CharField),Caption(CharField), createdat(IntegerField), CreatedDate(DateTimeField)
class Postdata(models.Model):
    emp_id = models.CharField(max_length=20)
    text = models.CharField(max_length=500)
    image = models.CharField(max_length=500)
    categories = models.CharField(max_length=50)
    like = models.IntegerField()
    comment = models.CharField(max_length=500)
    caption = models.CharField(max_length=500)
    createdat = models.IntegerField()
    createddate = models.DateTimeField()

    def __str__(self):
        return self.text