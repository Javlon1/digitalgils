from django.db import models


# logo
class Logo(models.Model):
    img = models.ImageField(upload_to='logo/')


# slider
class Slider(models.Model):
    img = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=255)
    text = models.TextField()


# about
class About(models.Model):
    img = models.ImageField(upload_to='about/')
    text = models.TextField()


# direction
class Direction(models.Model):
    img = models.ImageField(upload_to='direction/')
    title = models.CharField(max_length=255)


# task
class Task(models.Model):
    title = models.CharField(max_length=255)


# result
class Result(models.Model):
    img = models.ImageField(upload_to='result/')
    title = models.CharField(max_length=255)


# contact
class Contact(models.Model):
    website = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)    


# questions
class Questions(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.question


# answer
class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answers = models.CharField(max_length=255)

    def __str__(self):
        return self.answer


# resitrations
class Registration(models.Model):
    answer = models.ManyToManyField(Answers, blank=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# letter
class Letter(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE) 
    text = models.TextField()