# Generated by Django 2.2.6 on 2019-10-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.ForeignKey(on_delete=True, to='company.Company')),
            ],
        ),
    ]
