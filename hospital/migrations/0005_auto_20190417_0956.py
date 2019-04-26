# Generated by Django 2.0.13 on 2019-04-17 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20190417_0953'),
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
            field=models.CharField(choices=[('oncology', 'oncology'), ('ENT', 'ENT'), ('gynecology', 'gynecology'), ('dermetalogy', 'dermetalogy'), ('pediatrics', 'pediatrics'), ('cardiology', 'cardiology')], default='pediatrcis', max_length=30),
        ),
    ]