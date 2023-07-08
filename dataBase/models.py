from django.db import models

# Create your models here.

class Shows(models.Model):
    show_id= models.AutoField(primary_key=True)
    show_name=models.CharField(max_length=50,default='')
    epesodes=models.IntegerField(default=0)
    poster=models.ImageField(default='')

    def __str__(self):
        return self.show_name

class MostPoplular(models.Model):
    show=models.ForeignKey(Shows,on_delete=models.CASCADE)

class Starplus(models.Model):
    show=models.ForeignKey(Shows,on_delete=models.CASCADE)

class StarBharat(models.Model):
    show=models.ForeignKey(Shows,on_delete=models.CASCADE)

class Episodes(models.Model):
    show=models.ForeignKey(Shows,on_delete=models.CASCADE)
    episode_no=models.IntegerField(default=-1)
    decribtion=models.CharField(max_length=100,default='')
    video = models.FileField(upload_to='videos/')  # FileField to store the video file
    image=models.ImageField(default='')

    def __str__(self):
        return f"Episode {self.episode_no} of {self.show}"
    
class User(models.Model):
    first_name=models.CharField(max_length=30,default='')
    last_name=models.CharField(max_length=30,default='')
    mail=models.EmailField(default='')
    password=models.CharField(max_length=107,null=False)

class Slide(models.Model):
    show=models.ForeignKey(Shows,on_delete=models.CASCADE)
    width_image=models.ImageField(default='')




    



    

    

