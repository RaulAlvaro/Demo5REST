from alumnos.models import Alumno
from alumnos.serializers import AlumnoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AlumnoList(APIView):
	def get(self, request, format=None):
		alumnos = Alumno.objects.all()
		serializer = AlumnoSerializer(alumnos, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = AlumnoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlumnosDetail(APIView):
	def get_objet(self, pk):
		try:
			return Alumno.objects.get(pk=pk)
		except Alumno.DosNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		alumno = self.get_objet(pk)
		serializer = AlumnoSerializer(alumno)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		alumno = self.get_objet(pk)
		serializer = AlumnoSerializer(alumno, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		alumno = self.get_objet(pk)
		alumno.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
