from django.db import models

# Create your models here.

class DiseaseType(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease_type'

class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField()

    class Meta:
        verbose_name_plural = 'Countries'
        managed = False
        db_table = 'country'

class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    id = models.ForeignKey('DiseaseType', models.DO_NOTHING, db_column='id')

    class Meta:
        managed = False
        db_table = 'disease'

class Discover(models.Model):
    cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='cname', primary_key=True)
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('cname', 'disease_code'),)

class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(primary_key=True, max_length=60)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

class PublicServant(models.Model):
    email = models.OneToOneField('User', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_servant'

class Doctor(models.Model):
    email = models.OneToOneField('User', models.DO_NOTHING, db_column='email', primary_key=True)
    degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'

class Specialize(models.Model):
    id = models.OneToOneField(DiseaseType, models.DO_NOTHING, db_column='id')
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'specialize'
        unique_together = (('id', 'email'),)

class Record(models.Model):
    email = models.OneToOneField(PublicServant, models.DO_NOTHING, db_column='email', primary_key=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)