from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length = 35, blank = False)
    last_name = models.CharField(max_length = 35, blank = False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.last_name} {self.name} {self.second_name}'


class Student(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length = 35, blank = False)
    last_name = models.CharField(max_length = 35, blank = False)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.last_name} {self.name} {self.second_name}'


class Specialte(models.Model):
    title = models.CharField(max_length=20, blank=False)
    description = models.CharField(max_length = 200, blank = False)


    def __str__(self):
        return f'{self.title} {self.description}'

class Time(models.Model):
    date = models.DateField(blank=False)
    time = models.TimeField(blank = False)
    tutor = models.CharField(max_length = 35, blank = False)
    special = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.date} {self.special} {self.tutor} {self.time}'

class Record(models.Model):
    last_name = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length = 35, blank = False)
    second_name = models.CharField(max_length = 35, blank = False)
    phone = models.CharField(max_length=12)
    mail = models.EmailField()

    def __str__(self):
        return f'{self.last_name} {self.name} {self.second_name}'

class Feedback(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length = 35, blank = False)
    last_name = models.CharField(max_length = 35, blank = False)
    feedback = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return f'{self.last_name} {self.name} {self.second_name}'