from django.db import models

class Genre(models.Model):
	nimi = models.CharField(max_length=32)

	def __unicode__(self):
		return "%d: %s" % (self.id, self.nimi)

class Elokuva(models.Model):
	nimi = models.CharField(max_length=32)
	pituus = models.IntegerField()
	vuosi = models.IntegerField()
	genret = models.ManyToManyField(Genre, related_name='elokuvat')

	genret.help_text = ''

	def __unicode__(self):
		return "Elokuva %d: %s, pituus %d, vuosi %d" % (self.id, self.nimi,
				self.pituus, self.vuosi)
