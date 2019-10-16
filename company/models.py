from django.db import models

# Create your models here.
class Company(models.Model):
    company_name =models.CharField(max_length=100, verbose_name="sirket adı")

    def __str__(self):
        return self.company_name

class Departament(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=100,verbose_name="departman adı")

    def __str__(self):
        return self.dep_name


class Staff(models.Model):
    company = models.ForeignKey(Departament, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=100, verbose_name="Adı-Soyadı")
    saatlik_ücreti = models.IntegerField()

    def __str__(self):
        return self.staff_name