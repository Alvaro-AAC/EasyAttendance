from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from .models import *
from api.serializers import *
from functools import wraps
import datetime

def guard(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        try:
            username = request.session['username']
            try:
                profesor = Profesor.objects.get(usuario = username)
                return function(request, **kwargs, user=profesor)
            except Profesor.DoesNotExist:
                request.session.flush()
                redirect('/login/')
        except KeyError:
            return redirect('/login/')
  return wrap

def redirecter(request):
    try:
        profe = request.session['profe']
        return redirect('/clases/')
    except KeyError:
        return redirect('/login/')

@guard
def home(request, user):
    ctx = {}
    ctx['prof'] = user
    ctx['secciones'] = Seccion.objects.filter(profesor_id = user).all()
    ramos = []
    for elem in ctx['secciones']:
        ramos.append(elem.ramo_id)
    ctx['ramos'] = ramos
    return render(request, 'core/home.html', ctx)

def login(request):
    try:
        profe = request.session['username']
        return redirect('/clases/')
    except KeyError:
        return render(request, 'core/login.html')

def verifyLogin(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('pwd')
        try:
            profe = Profesor.objects.get(usuario = user)
            if check_password(password, profe.contrasena):
                request.session['username'] = user
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'dataerror'})
        except Profesor.DoesNotExist:
            return JsonResponse({'status': 'dataerror'})
    else:
        return JsonResponse({'status': 'error'})

def logout(request):
    request.session.flush()
    return redirect('/')

def crearclase(request):
    if request.method == 'POST':
        try:
            profe = request.session['username']
        except KeyError:
            return JsonResponse({'status': 'error'})
        ramo = request.POST['ramo']
        seccion = Seccion.objects.get(pk = request.POST['seccion'], ramo_id = ramo)
        clase = Clase(seccion_id = seccion, fecha = datetime.date.today())
        clase.save()
        return JsonResponse({'status': 'success'})
    else:
        print('error')
        return JsonResponse({'status': 'error'})

def verificar(request, token):
    if request.method == 'GET':
        ctx = {'valid': False}
        try:
            vToken = TokenLogin.objects.get(token = token)
            vToken.verificado = True
            vToken.save()
            ctx['valid'] = True
            return render(request, 'core/verificar.html', ctx)
        except TokenLogin.DoesNotExist:
            return render(request, 'core/verificar.html', ctx)
    else:
        return render(request, 'core/verificar.html', ctx)