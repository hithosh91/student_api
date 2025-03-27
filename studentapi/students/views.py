

from rest_framework import generics
from .models import Student
from .serializers import studentSeriliazer

#create view for student

class studentCreatview(generics.CreateAPIView):
       queryset=Student.objects.all()
       serializer_class=studentSeriliazer
       
#getallstudents

class studentgetall(generics.ListAPIView):
   queryset=Student.objects.all()
   serializer_class=studentSeriliazer
   
#getby id

class studentgetbyid(generics.RetrieveAPIView):
   queryset=Student.objects.all()
   serializer_class=studentSeriliazer


#update
class studentupdate(generics.UpdateAPIView):
   queryset=Student.objects.all()
   serializer_class=studentSeriliazer
   
#delete

class studentdelete(generics.DestroyAPIView):
   queryset=Student.objects.all()
   serializer_class=studentSeriliazer
