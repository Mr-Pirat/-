# Generated by Django 2.0.13 on 2019-08-26 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('country_of_birth', models.CharField(max_length=50)),
                ('year_of_birth', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Year of issue')),
                ('edition', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Author')),
            ],
        ),
    ]
