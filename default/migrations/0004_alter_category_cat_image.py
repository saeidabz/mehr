# Generated by Django 4.0.5 on 2022-07-19 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_category_cat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
