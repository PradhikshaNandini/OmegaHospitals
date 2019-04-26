# Generated by Django 2.0.13 on 2019-04-17 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_auto_20190417_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('qualifications', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=15)),
                ('speciality', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='apt',
            name='hospital',
            field=models.CharField(choices=[('girinagar', 'omega hospitals,girinagar'), ('jayanagar', 'omega hospitals,jayanagr'), ('vijayanagar', 'omega hospitals,vijayanagar')], default='girinagar', max_length=30),
        ),
        migrations.AlterField(
            model_name='apt',
            name='speciality',
            field=models.CharField(choices=[('gynecology', 'gynecology'), ('ENT', 'ENT'), ('cardiology', 'cardiology'), ('oncology', 'oncology'), ('pediatrics', 'pediatrics'), ('dermetalogy', 'dermetalogy')], default='pediatrcis', max_length=30),
        ),
    ]
