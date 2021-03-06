# Generated by Django 2.0.13 on 2019-04-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_auto_20190417_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apt',
            name='hospital',
            field=models.CharField(choices=[('jayanagar', 'omega hospitals,jayanagr'), ('vijayanagar', 'omega hospitals,vijayanagar'), ('girinagar', 'omega hospitals,girinagar')], default='girinagar', max_length=30),
        ),
        migrations.AlterField(
            model_name='apt',
            name='speciality',
            field=models.CharField(choices=[('gynecology', 'gynecology'), ('oncology', 'oncology'), ('dermetalogy', 'dermetalogy'), ('ENT', 'ENT'), ('pediatrics', 'pediatrics'), ('cardiology', 'cardiology')], default='pediatrcis', max_length=30),
        ),
    ]
