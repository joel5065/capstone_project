from django.db import models

# Create your models here.
class Military(models.Model):
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    IS_MARRIED_CHOICES= [
        ('M', 'MARIED'),
        ('S', 'SINGLE'),
        ('D', 'DIVORCED'),
    ]
    RANK_CHOICES = [
        ('PVT', 'Private'),
        ('CPL', 'Corporal'),
        ('SGT', 'Sergeant'),
        ('ADT', 'Adjudant'),
        ('LT', 'Lieutenant'),
        ('CPT','Captain'),
        ('MAJ', 'Major'),
        ('COL', 'Colonel'),
        ('GEN', 'General'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    rank = models.CharField(max_length=3, choices=RANK_CHOICES)
    date_of_birth = models.DateField()
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)
    current_unit = models.CharField(max_length=100)
    service_number = models.CharField(max_length=100, unique=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    is_maried = models.CharField(max_length=1, choices=IS_MARRIED_CHOICES)
    graduation_school = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.rank} {self.first_name} - {self.current_unit}"
    

class Diploma(models.Model):
    CATEGORY_DIPLOMA = [
        ('M', 'Military'),
        ('C', 'Civilian'),
    ]

    military = models.ForeignKey(Military, on_delete=models.CASCADE, related_name='diplomas')

    fiel_of_study = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    diploma_number = models.CharField(max_length=50, unique=True)
    type_of_diploma = models.CharField(max_length=1, choices=CATEGORY_DIPLOMA)
    graduation_date = models.DateField()
    institution = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.degree} in {self.fiel_of_study} - {self.institution}"
    
class Children(models.Model):

    military = models.ForeignKey(Military, on_delete=models.CASCADE, related_name='children')

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], blank=True)
    grade = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'