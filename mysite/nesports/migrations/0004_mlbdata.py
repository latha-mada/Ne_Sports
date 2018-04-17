# Generated by Django 2.0.2 on 2018-04-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nesports', '0003_nfldata'),
    ]

    operations = [
        migrations.CreateModel(
            name='MlbData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('team', models.CharField(max_length=10)),
                ('player', models.CharField(max_length=50)),
                ('games', models.IntegerField()),
                ('homeruns', models.IntegerField()),
                ('walks', models.IntegerField()),
                ('homeplate', models.IntegerField()),
            ],
        ),
    ]