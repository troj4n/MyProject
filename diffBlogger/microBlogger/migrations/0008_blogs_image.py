# Generated by Django 2.2.2 on 2019-07-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microBlogger', '0007_auto_20190701_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]