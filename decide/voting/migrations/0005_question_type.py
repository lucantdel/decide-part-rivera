# Generated by Django 4.1 on 2023-12-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_alter_voting_postproc_alter_voting_tally'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('C', 'Pregunta clasica'), ('M', 'Pregunta multirrespuesta')], default='C', max_length=1),
        ),
    ]
