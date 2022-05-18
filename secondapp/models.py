from tkinter import Widget
from django.db import models
from django import forms
from .models import Course

from member import forms

class Course(models.Model):
    name = models.CharField(max_length=30)
    cnt = models.IntegerField()

class ArmyShop(models.Model):
    name = models.TextField()
    type = models.TextField()
    month = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        db_table = 'army_shop'
        # 이미 생성되어있는 테이블이므로
        managed = False

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'cnt']
        Widget = {
            'name': forms.TextInput(
                attrs={'required':False, 'size': 10}),
            'cnt': forms.TextInput(
                attrs={'required':False, 'size': 10}),
        }
        labels = {
            'name':'과목', 'cnt':'수강인원'
        }