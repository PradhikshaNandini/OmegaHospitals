# Generated by Django 2.0.13 on 2019-04-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_auto_20190417_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apt',
            name='hospital',
            field=models.CharField(choices=[('vijayanagar', 'omega hospitals,vijayanagar'), ('jayanagar', 'omega hospitals,jayanagr'), ('girinagar', 'omega hospitals,girinagar')], default='girinagar', max_length=30),
        ),
        migrations.AlterField(
            model_name='apt',
            name='speciality',
            field=models.CharField(choices=[('cardiology', 'cardiology'), ('gynecology', 'gynecology'), ('pediatrics', 'pediatrics'), ('dermetalogy', 'dermetalogy'), ('oncology', 'oncology'), ('ENT', 'ENT')], default='pediatrcis', max_length=30),
        ),
    ]