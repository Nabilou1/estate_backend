# Generated by Django 5.0.1 on 2024-02-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_picture2_listing_picture3_listing_picture4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='picture5',
            field=models.ImageField(blank=True, null=True, upload_to='pictures_/%Y/%m/%d/'),
        ),
    ]
