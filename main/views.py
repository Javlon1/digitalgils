from unicodedata import name
from .serializer import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets


# logo
class LogoViews(viewsets.ModelViewSet):

    queryset = Logo.objects.all()
    serializer_class = LogoSerializers

    http_method_names = ['get']
    
    def list(self, request):

        slider = Logo.objects.last()
        ser = LogoSerializers(slider)

        return Response(ser.data)


# slider
class SliderViews(viewsets.ModelViewSet):

    queryset = Slider.objects.all()
    serializer_class = SliderSerializers

    http_method_names = ['get']

    
    def list(self, request):

        slider = Slider.objects.last()
        ser = SliderSerializers(slider)

        return Response(ser.data)


# about
class AboutViews(viewsets.ModelViewSet):

    queryset = About.objects.all()
    serializer_class = AboutSerializers

    http_method_names = ['get']

    
    def list(self, request):

        slider = About.objects.all().order_by('-id')
        ser = AboutSerializers(slider, many=True)

        return Response(ser.data)


# direction
class DirectionViews(viewsets.ModelViewSet):

    queryset = Direction.objects.all()
    serializer_class = DirectionSerializers

    http_method_names = ['get']

    
    def list(self, request):
        slider = Direction.objects.all().order_by('-id')[0:5]
        ser = DirectionSerializers(slider, many=True)

        return Response(ser.data)


# task
class TaskViews(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializers

    http_method_names = ['get']

    
    def list(self, request):
        slider = Task.objects.all().order_by('-id')[0:10]
        ser = TaskSerializers(slider, many=True)

        return Response(ser.data)


# resitrations
class RegistrationViews(viewsets.ModelViewSet):

    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers

    http_method_names = ['post']

    def create(self, request):
        try:

            name = request.data['name']
            surname = request.data['surname']
            date_of_birth = request.data['date_of_birth']
            email = request.data['email']
            address = request.data['address']
            number = request.data['number']
            
            answer_id = request.POST.get('answer_id')
            answers = Answers.objects.get(id=answer_id)
            answer = Registration(answer=answers)
            answer.answers.add()


            Registration.objects.create(name=name, surname=surname, date_of_birth=date_of_birth, email=email, address=address, number=number)
            return Response('кошилди')
        except Exception as err:
            data = {
                'error':f'{err}'
            }
            return Response(data)


# result
class ResultViews(viewsets.ModelViewSet):

    queryset = Result.objects.all()
    serializer_class = ResultSerializers

    http_method_names = ['get']

    
    def list(self, request):

        slider = Result.objects.all().order_by('-id')[0:5]
        ser = ResultSerializers(slider, many=True)

        return Response(ser.data)


# contact
class ContactViews(viewsets.ModelViewSet):

    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

    http_method_names = ['get']

    
    def list(self, request):
        slider = Contact.objects.last()
        ser = ContactSerializers(slider)

        return Response(ser.data)
# 
# 
# questions
class QuestionsViews(viewsets.ModelViewSet):

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers

    http_method_names = ['get']
    
    def list(self, request):
        slider = Questions.objects.last()
        ser = QuestionsSerializers(slider)

        return Response(ser.data)


# answer
class AnswersViews(viewsets.ModelViewSet):

    queryset = Answers.objects.all()
    serializer_class = AnswersSerializers
    http_method_names = ['get']


# letter
class LetterViews(viewsets.ModelViewSet):

    queryset = Letter.objects.all()
    serializer_class = LetterSerializers

    http_method_names = ['post']

    
    def create(self, request):
        text = request.data['text']
        Letter.objects.create(text=text)
