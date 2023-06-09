# Generated by Django 4.0.4 on 2022-09-02 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('alumno_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100, unique=True)),
                ('contrasena', models.CharField(max_length=2000)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno_Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presente', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('clase_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CodigoQR',
            fields=[
                ('codigoqr_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=1000)),
                ('fecha_exp', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horario_Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('LUN', 'Lunes'), ('MAR', 'Martes'), ('MIE', 'Miercoles'), ('JUE', 'Jueves'), ('VIE', 'Viernes'), ('SAB', 'Sabado'), ('DOM', 'Domingo')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('modulo_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('hora_ini', models.TimeField()),
                ('hora_fin', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('profesor_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100, unique=True)),
                ('contrasena', models.CharField(max_length=2000)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ramo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_letra', models.CharField(max_length=3)),
                ('codigo_numero', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_seccion', models.IntegerField()),
                ('tipo', models.CharField(max_length=1)),
                ('ramo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ramo')),
            ],
        ),
        migrations.AddConstraint(
            model_name='ramo',
            constraint=models.UniqueConstraint(fields=('codigo_letra', 'codigo_numero'), name='constraint_ramo_codigo'),
        ),
        migrations.AddField(
            model_name='horario_seccion',
            name='modulo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modulo'),
        ),
        migrations.AddField(
            model_name='horario_seccion',
            name='seccion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.seccion'),
        ),
        migrations.AddField(
            model_name='codigoqr',
            name='clase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clase'),
        ),
        migrations.AddField(
            model_name='clase',
            name='profesor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profesor'),
        ),
        migrations.AddField(
            model_name='clase',
            name='seccion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.seccion'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='alumno_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='clase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.clase'),
        ),
        migrations.AddField(
            model_name='alumno_seccion',
            name='alumno_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno'),
        ),
        migrations.AddField(
            model_name='alumno_seccion',
            name='seccion_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.seccion'),
        ),
        migrations.AddConstraint(
            model_name='seccion',
            constraint=models.CheckConstraint(check=models.Q(('tipo__in', ('D', 'V'))), name='constraint_seccion_check_tipo'),
        ),
        migrations.AddConstraint(
            model_name='seccion',
            constraint=models.UniqueConstraint(fields=('codigo_seccion', 'ramo_id', 'tipo'), name='constraint_seccion_codigo'),
        ),
        migrations.AddConstraint(
            model_name='horario_seccion',
            constraint=models.UniqueConstraint(fields=('modulo_id', 'seccion_id', 'dia'), name='horario_seccion_constraint_uk'),
        ),
        migrations.AddConstraint(
            model_name='asistencia',
            constraint=models.UniqueConstraint(fields=('clase_id', 'alumno_id'), name='constraint_asistencia_pk'),
        ),
    ]
