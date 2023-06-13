from django.contrib import admin
import core.models

# Register your models here.

admin.register(core.models.Ramo,core.models.Modulo,
               core.models.Seccion,core.models.Horario_Seccion,
               core.models.Alumno,core.models.Alumno_Seccion,
               core.models.Profesor,core.models.Clase,
               core.models.Asistencia,core.models.CodigoQR,
               core.models.TokenAlumno,core.models.TokenLogin,
               core.models.Credencial)(admin.ModelAdmin)