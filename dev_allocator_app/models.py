from django.db import models

class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)    

    def __str__(self):
        return self.name
    
class Developer(models.Model):
    name = models.CharField(max_length=100)
    technologies = models.ManyToManyField(Technology, related_name='developers')
    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    Technologies = models.ManyToManyField(Technology, related_name='projects')

    def __str__(self):
        return self.name
    
class Allocation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='allocations')
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='allocations')
    hours = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.developer} allocated to {self.project}'