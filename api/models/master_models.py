from django.db import models

class Role(models.Model):
    class Meta:
        db_table = 'role'
    id         = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=50, null=True, blank=True)
    is_active  = models.BooleanField(('active'), default=True )

    def __str__(self):
        return self.name