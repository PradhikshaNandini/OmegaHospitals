# Generated by Django 2.0.13 on 2019-04-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_auto_20190421_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apt',
            name='hospital',
            field=models.CharField(choices=[('jayanagar', 'omega hospitals,jayanagr'), ('girinagar', 'omega hospitals,girinagar'), ('vijayanagar', 'omega hospitals,vijayanagar')], default='girinagar', max_length=30),
        ),
        migrations.AlterField(
            model_name='apt',
            name='speciality',
            field=models.CharField(choices=[('ENT', 'ENT'), ('cardiology', 'cardiology'), ('oncology', 'oncology'), ('dermetalogy', 'dermetalogy'), ('gynecology', 'gynecology'), ('pediatrics', 'pediatrics')], default='pediatrcis', max_length=30),
        ),
    ]
