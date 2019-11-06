# Generated by Django 2.2 on 2019-11-01 13:41

from django.db import migrations


def create_profiles(app, schema_editor):
    User = app.get_model('auth', 'User')
    Profile = app.get_model('accounts', 'Profile')
    for user in User.objects.all():
        Profile.objects.get_or_create(user=user)

def delete_profiles(app, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_profiles, delete_profiles)
    ]