# Generated by Django 4.1.4 on 2023-01-06 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_highlightevents'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HighlightEvents',
        ),
        migrations.AddField(
            model_name='events',
            name='highlight',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
