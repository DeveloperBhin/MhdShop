# Generated by Django 5.1.1 on 2025-03-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sellerpages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=10)),
                ('Contact_name', models.CharField(max_length=20)),
                ('Region', models.CharField(max_length=20)),
                ('District', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=20)),
                ('Image', models.ImageField(default=None, upload_to='Uploads/')),
                ('Product_name', models.CharField(max_length=10)),
                ('Price', models.CharField(max_length=20)),
                ('Status', models.CharField(max_length=20)),
                ('Brand', models.CharField(max_length=20)),
                ('Delivery', models.CharField(max_length=20)),
                ('Description', models.CharField(max_length=20)),
            ],
        ),
    ]
