# Generated by Django 2.0.4 on 2018-05-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palanaeum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersentrycollection',
            name='starred',
        ),
        migrations.AddField(
            model_name='usersentrycollection',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='usersentrycollection',
            name='entries',
            field=models.ManyToManyField(related_name='collections', to='palanaeum.Entry'),
        ),
    ]