from django.db import models

# Create your models here.
class Military(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    ]
    IS_MARRIED_CHOICES= [
        ('M', 'MARIED'),
        ('S', 'SINGLE'),
        ('D', 'DIVORCED'),
    ]
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    rank = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    departement = models.CharField(max_length=50)
    registration_number = models.IntegerField()
    profile_picture = models.ImageField(upload_to='pofile_pictures/', blank=True, null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    is_maried = models.CharField(max_length=1, choices=IS_MARRIED_CHOICES)
    graduation_school = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rank} {self.name} - {self.departement}"
    

class Diploma(models.Model):
    CATEGORY_DIPLOMA = [
        ('M', 'Military'),
        ('C', 'Civilian'),
    ]

    owner = models.ForeignKey(Military, on_delete=models.CASCADE)

    diploma_title = models.CharField(max_length=100)
    type_of_diploma = models.CharField(max_length=1, choices=CATEGORY_DIPLOMA)
    date_of_production = models.DateField()
    school_of_graduation = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.diploma_title}'
    
class Children(models.Model):

    parent = models.ForeignKey(Military, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'{self.name} of {self.parent}'