from django.db import models

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