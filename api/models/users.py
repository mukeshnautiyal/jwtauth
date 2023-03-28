from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext as _
from __future__ import unicode_literals

from models.master_models import Role

class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
       db_table  = "users"
    id         =     models.AutoField(primary_key=True)
    username        = models.CharField(_('username'), max_length=75, unique=True, help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators = [ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid') ])
    first_name      = models.CharField(('first_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50, null=True,blank=True)
    last_name       = models.CharField(('last_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50,null=True,blank=True)
    email           = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    is_staff        = models.BooleanField(default=0)
    is_active       = models.BooleanField(('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    image       = models.ImageField(upload_to='static/img/avatars',null=True, blank=True,default=None) 
    phone               = models.CharField(validators=[RegexValidator( '^[0-9]{10}$')],max_length=12, null=True,blank=True,unique=True)
    phone_verified= models.BooleanField( default=1)
    email_verified=  models.BooleanField(default=1)
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING,default= 2, related_name='role_id')
    otp   = models.IntegerField(validators=[RegexValidator( '^[0-9]{4}$')],null=True,blank=False)
    onetime_token = models.CharField(blank=True, null=True, unique=True, max_length=254, default=None)
    device_token= models.CharField(max_length=255,default=None,blank=True, null=True)
    created_on      = models.DateTimeField(auto_now_add=True,blank=True, null=True,)
    updated_on      = models.DateTimeField(auto_now=True,blank=True, null=True,)

    objects         = UserManager()
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def get_short_name(self):
        return self.first_name
    def __unicode__(self):
        return self.email