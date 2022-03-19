from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('logo', LogoViews)
router.register('slider', SliderViews)
router.register('about', AboutViews)
router.register('direction', DirectionViews)
router.register('task', TaskViews)
router.register('resitration', RegistrationViews)
router.register('result', ResultViews)
router.register('contact', ContactViews)
router.register('question', QuestionsViews)
router.register('answer', AnswersViews)
router.register('letter', LetterViews)



