# Generated by Django 5.0.3 on 2024-04-25 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auctionslisting_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionslisting',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]