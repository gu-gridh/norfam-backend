# Generated by Django 3.0.2 on 2020-01-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_id', models.IntegerField()),
                ('term_term', models.CharField(max_length=100)),
                ('term_stem', models.CharField(max_length=100)),
                ('term_df', models.IntegerField()),
            ],
        ),
    ]