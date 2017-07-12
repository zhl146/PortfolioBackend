from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    imgPath = models.CharField(max_length=128)
    gitHubLink = models.CharField(max_length=128)
    demoLink = models.CharField(max_length=128)
    blogRoute = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_json(self):
        json = {
            'name': self.name,
            'description': self.description,
            'imgPath': self.imgPath,
            'gitHubLink': self.gitHubLink,
            'demoLink': self.demoLink,
            'blogRoute': self.blogRoute,
        }
        return json
