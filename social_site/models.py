# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Beziehung(models.Model):
    id1 = models.ForeignKey('Nutzer', models.DO_NOTHING, related_name='second', db_column='id1', primary_key=True)
    id2 = models.ForeignKey('Nutzer', models.DO_NOTHING, related_name='first', db_column='id2')
    art = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beziehung'
        unique_together = (('id1', 'id2'),)


class Brillentraeger(models.Model):
    id = models.ForeignKey('Nutzer', models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'brillentraeger'


class Hobby(models.Model):
    h_name = models.CharField(primary_key=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'hobby'


class Istfan(models.Model):
    id1 = models.ForeignKey('Nutzer',  models.DO_NOTHING, db_column='id1', primary_key=True)
    id2 = models.ForeignKey('Nutzer', models.DO_NOTHING,related_name='idol', db_column='id2')

    class Meta:
        managed = False
        db_table = 'istfan'
        unique_together = (('id1', 'id2'),)


class Nutzer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    n_name = models.TextField()
    alter = models.IntegerField()
    wohnort = models.TextField(blank=True, null=True)
    anzeigename = models.CharField(max_length=80, blank=True, null=True)
    einkommen = models.BigIntegerField()
    class Meta:
        managed = False
        db_table = 'nutzer'


class Uebtaus(models.Model):
    nutzerid = models.ForeignKey(Nutzer, models.DO_NOTHING, db_column='nutzerid', primary_key=True)
    hobbyname = models.ForeignKey(Hobby, models.DO_NOTHING, db_column='hobbyname')

    class Meta:
        managed = False
        db_table = 'uebtaus'
        unique_together = (('nutzerid', 'hobbyname'),)

