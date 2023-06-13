# Generated by Django 4.0.4 on 2022-09-03 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_codigoqr_url_alter_tokenalumno_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tokenalumno',
            old_name='token_id',
            new_name='tokenAlumno_id',
        ),
        migrations.CreateModel(
            name='TokenLogin',
            fields=[
                ('tokenLogin_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(blank=True, max_length=1000, null=True, unique=True)),
                ('fecha_exp', models.DateTimeField(blank=True, null=True)),
                ('alumno_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
            ],
        ),
    ]
