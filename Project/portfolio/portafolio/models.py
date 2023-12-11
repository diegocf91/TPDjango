from django.db import models

# Create your models here.

class Project(models.Model):
    tittle = models.CharField(max_length=200)
    descripcion = models.TextField()
    image = models.ImageField(upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.tittle

class Meta:
    verbose_name = "project"
    verbose_name_plural = "projects"
    ordering = ["-created"]

