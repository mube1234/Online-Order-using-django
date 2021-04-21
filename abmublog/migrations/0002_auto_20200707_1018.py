# Generated by Django 3.0.3 on 2020-07-07 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abmublog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abmublog.Product'),
        ),
    ]
