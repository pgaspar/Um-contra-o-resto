# -*- coding: utf-8 -*-
from django.db import models

class Pergunta(models.Model):
   
   pergunta = models.TextField()
   
#   def __unicode__(self):
#    return u'%s' % self.nome

#  def get_absolute_url(self):
#    return u'/categorias/%d/' % self.id

class Resposta(models.Model):
   resposta = models.CharField(max_length = 150)
   # ATENCAO :
   #resposta_imagem = models.ImageField(upload_to='imagens')
   #falta instalar Pyhton Imageing Library
   
   def __unicode__(self):
    return u'%s' % self.nome

#  def get_absolute_url(self):
#    return u'/categorias/%d/' % self.id

