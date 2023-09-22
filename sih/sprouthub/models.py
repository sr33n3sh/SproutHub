from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Institute(models.Model):
    Institute_id = models.IntegerField(primary_key=True)   
    Institute_username = models.CharField(max_length=50)             
    Institute_password = models.CharField(max_length=20)
    Institute_address = models.CharField(max_length=200)
    Institute_email = models.EmailField()
    Institute_contact = models.BigIntegerField()
    Institute_type = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Institute_id) + " " + self.Institute_username

class AnyStudent(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_username = models.CharField(max_length=50)
    student_password = models.CharField(max_length=60)
    student_contact = models.BigIntegerField(max_length=100)
    student_email = models.EmailField()

    def __str__(self):
        return str(self.student_id) + " " + self.student_username

class ProjectInstituteStudent(models.Model):
    YEAR_IN_INSTITUTE_CHOICES = [
        ("FR", "Freshman"),
        ("SO", "Sophomore"),
        ("JR", "Junior"),
        ("SR", "Senior"),
        ("GR", "Graduate"),
    ]

    Istudent_id = models.IntegerField(primary_key=True)
    Istudent_instituteId = models.ForeignKey('Institute', on_delete=models.CASCADE)
    Istudent_username = models.CharField(max_length=20)
    Istudent_contact = models.BigIntegerField()
    Istudent_email = models.EmailField()
    Istudent_year_in_institute = models.CharField(max_length=2,choices=YEAR_IN_INSTITUTE_CHOICES)
    Istudent_major = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Istudent_id) + " " + str(self.Istudent_instituteId)

class Projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_title = models.CharField(max_length=100)
    project_description = models.TextField()
    project_studentId = models.ManyToManyField('ProjectInstituteStudent')
    project_files = models.FileField()

    def __str__(self):
        return str(self.project_id) + " ___ " + self.project_title 





# class CreateProject(models.Model):
#     project_id = models.AutoField(primary_key=True)  
#     project_name = models.CharField(max_length=200)
#     project_description = models.TextField()
#     student_name = models.CharField(max_length=100)
#     student_email=models.EmailField()
#     student_roll = models.CharField(max_length=10)
#     project_file = models.FileField(upload_to='uploads/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.project_name

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)  
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    student_name = models.CharField(max_length=100)
    student_email=models.EmailField(default='example@email.com')
    student_roll = models.CharField(max_length=10)
    project_file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
