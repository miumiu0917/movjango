# Generated by Django 3.1.2 on 2020-11-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedjango', '0009_auto_20201030_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movies',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]