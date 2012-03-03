# encoding: UTF-8
from django.shortcuts import render
from wad_django.elokuvat_ja_genret.models import Elokuva, Genre
from django.http import HttpResponseRedirect
from django.forms import ModelForm, ValidationError, CheckboxSelectMultiple

class ElokuvaForm(ModelForm):
	class Meta:
		model = Elokuva
		exclude = ('genret',)

class GenreLisaysForm(ModelForm):
	class Meta:
		model = Genre

def listaa(request, elokuva=None, genre=None):
	return render(request, 'elokuvat.html', { 'elokuvat': Elokuva.objects.all(),
		'genret': Genre.objects.all(),
		'elokuva_form': elokuva if elokuva is not None else ElokuvaForm(),
		'genre_form': genre if genre is not None else GenreLisaysForm()
	})

def index(request):
	return listaa(request)

def lisaa_elokuva(request):
	elokuva = ElokuvaForm(request.POST)
	if elokuva.is_valid():
		elokuva.save()
		return HttpResponseRedirect('/elokuvat_ja_genret/')
	else:
		return listaa(request, elokuva=elokuva)

def lisaa_genre(request):
	genre = GenreLisaysForm(request.POST)
	if genre.is_valid():
		genre.save()
		return HttpResponseRedirect('/elokuvat_ja_genret/')
	return listaa(request, genre=genre)

def listaa_genre(request, genre_id):
	genre = Genre.objects.get(pk= int(genre_id))
	return render(request, 'genre.html', { 'genre': genre })

class GenretElokuvaanForm(ModelForm):
	class Meta:
		model = Elokuva
		fields = ('genret',)
		widgets = { 'genret': CheckboxSelectMultiple() }

def genret_elokuvaan(request, elokuva_id):
	elokuva = Elokuva.objects.get(pk= int(elokuva_id))
	if request.POST:
		uudet = GenretElokuvaanForm(request.POST, instance= elokuva)
		uudet.save()
		return HttpResponseRedirect('/elokuvat_ja_genret/')
	else:
		return render(request, 'genret_elokuvaan.html', { 'elokuva': GenretElokuvaanForm(instance= elokuva) })
