from __future__ import unicode_literals

from django.db import models

# Create your models here.

ESTADO = (
  ( '1' , 'Activo'), 
  ( '2' , 'Inactivo'), 
)



class Departamento(models.Model):
	Id_departamento = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=50)
	Estado = models.CharField(max_length=10, choices=ESTADO)
	



	#ACTIVO = 'S'
	#NO_ACTIVO = 'N'
	#ESTADO = (
	#	(ACTIVO, 'activo'),
	#	(NO_ACTIVO, 'no_activo'),
	#	)
	#estado = models.CharField(
	#	max_length=1,
	#	choices=ESTADO,
	#	)

    #def is_upperclass(self):
        #return self.estado in (self.JUNIOR, self.SENIOR)