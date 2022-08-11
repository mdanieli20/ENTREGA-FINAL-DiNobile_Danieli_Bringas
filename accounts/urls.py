from importlib.resources import path
from .views import login

urlpatterns = [
    path('login/', login, name='login')
]