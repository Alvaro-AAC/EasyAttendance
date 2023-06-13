# Generated by Django 4.0.4 on 2022-09-10 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_codigoqr_fecha_exp_alter_codigoqr_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clase',
            name='profesor_id',
        ),
        migrations.AddField(
            model_name='seccion',
            name='profesor_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.profesor'),
            preserve_default=False,
        ),
    ]
