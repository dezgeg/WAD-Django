# encoding: UTF-8
from django.shortcuts import render
from wad_django.henkilot_huoneisiin.models import Henkilo, Huone
from django.http import HttpResponseRedirect
from django.forms import ModelForm, ValidationError

class HuoneForm(ModelForm):
	class Meta:
		model = Huone

class HenkiloForm(ModelForm):
	class Meta:
		model = Henkilo

	def clean_huone(self):
		huone = self.cleaned_data['huone']
		if huone.henkilot.count() >= huone.kapasiteetti:
			raise ValidationError('Et voi lisätä henkilöä täyteen huoneeseen')
		return huone

def listaa(request, huone=None, henkilo=None):
	return render(request, 'listaa.html', { 'huoneet': Huone.objects.all(),
		'henkilot': Henkilo.objects.all(),
		'lisattava_huone': huone if huone is not None else HuoneForm(),
		'lisattava_henkilo': henkilo if henkilo is not None else HenkiloForm()
	})

def index(request):
	return listaa(request)

def lisaa_huone(request):
	huone = HuoneForm(request.POST)
	if huone.is_valid():
		huone.save()
		return HttpResponseRedirect('/henkilot_huoneisiin/')
	else:
		return listaa(request, huone=huone)

def lisaa_henkilo(request):
	henkilo = HenkiloForm(request.POST)
	if henkilo.is_valid():
		henkilo.save()
		return HttpResponseRedirect('/henkilot_huoneisiin/')
	return listaa(request, henkilo=henkilo)

def poista_henkilo(request, id):
	Henkilo.objects.get(pk=id).delete()
	return HttpResponseRedirect('/henkilot_huoneisiin/')

def poista_huone(request, id):
	Huone.objects.get(pk=id).delete()
	return HttpResponseRedirect('/henkilot_huoneisiin/')
