# Generated by Django 3.0.3 on 2020-02-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_resume_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodingSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('level', models.IntegerField(help_text='%')),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('level', models.IntegerField(help_text='%')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Knowlegde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('level', models.IntegerField(help_text='%')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('desciption', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='resume',
            name='future_goals',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='coding_skill',
            field=models.ManyToManyField(null=True, to='Home.CodingSkill'),
        ),
        migrations.AddField(
            model_name='resume',
            name='design',
            field=models.ManyToManyField(null=True, to='Home.Design'),
        ),
        migrations.AddField(
            model_name='resume',
            name='education',
            field=models.ManyToManyField(null=True, to='Home.Education'),
        ),
        migrations.AddField(
            model_name='resume',
            name='experience',
            field=models.ManyToManyField(null=True, to='Home.Experience'),
        ),
        migrations.AddField(
            model_name='resume',
            name='interest',
            field=models.ManyToManyField(null=True, to='Home.Interest'),
        ),
        migrations.AddField(
            model_name='resume',
            name='knowlegde',
            field=models.ManyToManyField(null=True, to='Home.Knowlegde'),
        ),
        migrations.AddField(
            model_name='resume',
            name='language',
            field=models.ManyToManyField(null=True, to='Home.Language'),
        ),
        migrations.AddField(
            model_name='resume',
            name='team',
            field=models.ManyToManyField(null=True, to='Home.Team'),
        ),
    ]