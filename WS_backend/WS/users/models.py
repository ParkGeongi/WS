from django.db import models

# Create your models here.
class User(models.Model):
    use_in_migration = True
    id = models.AutoField(primary_key=True)
    password = models.TextField()
    birthday = models.TextField()
    height = models.TextField()
    weight = models.TextField()
    phone_num = models.TextField()




    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'{self.pk} {self.password} {self.birthday} {self.height} {self.weight} {self.phone_num}'
