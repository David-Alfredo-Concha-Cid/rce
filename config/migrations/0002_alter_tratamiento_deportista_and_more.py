# Generated by Django 4.2.3 on 2023-08-31 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tratamiento',
            name='deportista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='config.deportista'),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='diagnostico',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='ejercicios',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='kinesiologo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='config.kinesiologo'),
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='observaciones',
            field=models.TextField(null=True),
        ),
    ]
