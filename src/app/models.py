from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, Group, AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField

class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='img/agent/%Y/%m/%d')
    job = models.CharField(max_length=50)
    description = models.TextField()

    last_login = None
    first_name = None
    last_name = None

    #is_superuser = models.BooleanField(default=False)
    #groups = models.ManyToManyField(Group)
    #USERNAME_FIELD = 'name'

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

    def __str__(self):
        return '%s' % (self.name)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(UserExtra, on_delete=models.CASCADE, help_text='Select your name from the list')
    url = models.CharField(max_length=100, default='some')
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='img/blog/%Y/%m/%d')
    tag = models.TextField(help_text='Separate tags with two dashes from each other')
    description = RichTextUploadingField()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return '%s' % (self.title)

class City(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return '%s' % (self.name)

class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Property Type'
        verbose_name_plural = 'Property Types'

    def __str__(self):
        return '%s' % (self.name)


class Property(models.Model):
    status_choise = (
        ('sell', 'For Sell'),
        ('rent', 'For Rent'),
    )
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    status = models.CharField(max_length=5, choices=status_choise)
    agent = models.ForeignKey(UserExtra, on_delete=models.CASCADE, help_text='Please select your name from list')
    address = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='img/properties/1/%Y/%m/%d')
    image2 = models.ImageField(upload_to='img/properties/2/%Y/%m/%d', null=True, blank=True, help_text='You can leave this field empty')
    image3 = models.ImageField(upload_to='img/properties/3/%Y/%m/%d', null=True, blank=True, help_text='You can leave this field empty')
    image4 = models.ImageField(upload_to='img/properties/4/%Y/%m/%d', null=True, blank=True, help_text='You can leave this field empty')
    image5 = models.ImageField(upload_to='img/properties/5/%Y/%m/%d', null=True, blank=True, help_text='You can leave this field empty')
    price = models.FloatField(max_length=11)
    bed_room = models.DecimalField(max_digits=2, decimal_places=0)
    baths = models.DecimalField(max_digits=2, decimal_places=0)
    garage = models.DecimalField(max_digits=2, decimal_places=0)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    year_build = models.CharField(max_length=10)
    home_area = models.DecimalField(max_digits=4, decimal_places=0)
    garage_area = models.DecimalField(max_digits=4, decimal_places=0)
    description = RichTextUploadingField()

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return '%s' % (self.title)

class AgentContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(UserExtra, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = 'Agent Contact'
        verbose_name_plural = 'Agent Contacts'

    def __str__(self):
        return '%s' % (self.name)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField()

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return '%s' % (self.name)