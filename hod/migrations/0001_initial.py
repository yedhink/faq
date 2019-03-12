# Generated by Django 2.1.7 on 2019-03-12 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HOD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('branch_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=300)),
                ('query_date', models.DateField(verbose_name='date asked')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hod.HOD')),
            ],
        ),
    ]
