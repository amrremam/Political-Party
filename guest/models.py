from django.db import models



class Author(models.Model):
    fName = models.CharField(max_length=222)

    def __str__(self):
        return self.fName


class Post(models.Model):
    title = models.CharField(max_length=222)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
