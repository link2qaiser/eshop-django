# Generated by Django 2.2.5 on 2019-09-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('parent_field', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
    ]
