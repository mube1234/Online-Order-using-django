# Generated by Django 3.0.3 on 2020-07-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abmublog', '0002_auto_20200707_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], default='Pending', max_length=200, null=True),
        ),
    ]
