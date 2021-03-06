# Generated by Django 2.0.13 on 2019-04-17 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20190417_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apt',
            name='hospital',
            field=models.CharField(choices=[('girinagar', 'omega hospitals,girinagar'), ('jayanagar', 'omega hospitals,jayanagr'), ('vijayanagar', 'omega hospitals,vijayanagar')], default='girinagar', max_length=30),
        ),
        migrations.AlterField(
            model_name='apt',
            name='speciality',
            field=models.CharField(choices=[('ENT', 'ENT'), ('cardiology', 'cardiology'), ('oncology', 'oncology'), ('pediatrics', 'pediatrics'), ('dermetalogy', 'dermetalogy'), ('gynecology', 'gynecology')], default='pediatrcis', max_length=30),
        ),
    ]
