# Generated by Django 4.0.4 on 2022-09-03 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_alumno_seccion_options_alter_codigoqr_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horario_seccion',
            options={'verbose_name': 'horario sección', 'verbose_name_plural': 'Horario Secciones'},
        ),
        migrations.AlterField(
            model_name='codigoqr',
            name='fecha_exp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='codigoqr',
            name='url',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.CreateModel(
            name='TokenAlumno',
            fields=[
                ('token_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=1000)),
                ('fecha_exp', models.DateTimeField(null=True)),
                ('alumno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
            ],
        ),
    ]
