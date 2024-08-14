# Generated by Django 5.0.8 on 2024-08-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleinfo',
            old_name='article_NAME',
            new_name='title',
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='content',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='image',
            field=models.ImageField(null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='tags_associated',
            field=models.ManyToManyField(to='main.taginfo'),
        ),
    ]
