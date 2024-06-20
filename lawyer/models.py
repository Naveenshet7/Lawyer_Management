from django.db import models


# Create your models here.

class PracticeArea(models.Model):
    PAreaName = models.CharField(max_length=200, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PAreaName

class Lawyer(models.Model):
    LawyerName = models.CharField(max_length=200, null=True)
    LawyerEmail = models.CharField(max_length=50, null=True)
    LawyerMobileNo = models.CharField(max_length=15, null=True)
    OfficeAddress = models.CharField(max_length=300, null=True)
    City = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True)
    LanguageKnown = models.CharField(max_length=150, null=True)
    ProfilePic = models.FileField(null=True)
    LawyerExp = models.IntegerField(default=0)
    practiceArea = models.ForeignKey(PracticeArea, on_delete=models.CASCADE)
    Courts = models.CharField(max_length=150, null=True)
    Website = models.CharField(max_length=200, null=True)
    Description = models.CharField(max_length=500, null=True)
    Status = models.CharField(max_length=50, null=True)
    RegDate = models.DateTimeField(null=True)

    def __str__(self):
        return self.LawyerName

class Page(models.Model):
    PageType = models.CharField(max_length=50, null=True)
    PageTitle = models.CharField(max_length=200, null=True)
    PageDescription = models.CharField(max_length=500, null=True)
    Email = models.CharField(max_length=50, null=True)
    MobileNumber = models.CharField(max_length=15, null=True)
    UpdationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.PageType
