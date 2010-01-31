# Create your views here.
from jogo.models import *
from django.contrib.auth.models import User

from django.shortcuts import render_to_response
from django.template.context import RequestContext

from django.contrib.auth.decorators import login_required

# Render helper function

def render(request,template,context={}):
	return render_to_response(template,context,context_instance=RequestContext(request))

# Views

@login_required
def user_view(request, username):
  user = User.objects.get(username=username)
  return render (request, 'detalhe_user.html', {'user':user})
  