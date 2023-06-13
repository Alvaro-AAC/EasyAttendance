# Generated by Django 4.0.4 on 2022-09-02 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alumno_seccion',
            options={'verbose_name': 'alumno de sección', 'verbose_name_plural': 'Alumnos de sección'},
        ),
        migrations.AlterModelOptions(
            name='codigoqr',
            options={'verbose_name_plural': 'Codigos QR'},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'verbose_name_plural': 'Profesores'},
        ),
        migrations.AlterModelOptions(
            name='seccion',
            options={'verbose_name_plural': 'Secciones'},
        ),
        migrations.AlterField(
            model_name='seccion',
            name='tipo',
            field=models.CharField(choices=[('D', 'Diurno'), ('V', 'Vespertino')], max_length=1),
        ),
    ]
