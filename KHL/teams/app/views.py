from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework import generics
from django.http import HttpResponseRedirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
import socket
from datetime import datetime

def logging(url, success):
    ip = socket.gethostbyname(socket.getfqdn())
    time = datetime.now(tz=None)
    l = Log(ip = ip,
            url = url,
            time = time,
            success = success,
            )
    l.save()
            
class LogView(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'log.html'

    def get(self, request):
        logs = Log.objects.all()
        return Response({'logs': logs})

class AddTeamView(generics.ListCreateAPIView):
    serializer_class = TeamSerializer
    renderer_classes = (TemplateHTMLRenderer, )
    template_name='addteam.html'

    def get(self, request):
        return Response({'serializer': TeamSerializer})

    def post(self, request):
        text = ''
        if request.data['name'] != '' and request.data['city'] != '':
            t = Team(name=request.data['name'], 
                     city=request.data['city'])
            t.save()
            logging(request.path, True)
        else:
            text = 'The form is not valid!'
            logging(request.path, False)
        return Response({'serializer': TeamSerializer, 'text': text})

class AddPlayerView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer
    renderer_classes = (TemplateHTMLRenderer, )
    template_name='addplayer.html'

    def get(self, request, pk):
        team = Team.objects.get(id=pk)
        return Response({'serializer': PlayerSerializer, 'team': team})

    def post(self, request, pk):
        text = ''
        success = False
        try:
            if request.data['first_name'] != '' and request.data['last_name'] != '':
                team = Team.objects.get(id=pk)
                p = Player(first_name=request.data['first_name'], 
                         last_name=request.data['last_name'],
                         birthday=request.data['birthday'],
                         team=team)
                p.save()
                success = True
            else:
                text = 'The form is not valid!'
        except:
            text = 'The form is not valid!'
        team = Team.objects.get(id=pk)
        logging(request.path, success)
        return Response({'serializer': PlayerSerializer, 'text': text, 'team': team})

class TeamDetailsView(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'teamdetails.html'

    def get(self, request, pk):
        players = Player.objects.filter(team_id=pk)
        team = Team.objects.get(id=pk)
        return Response({'team': team, 'players': players})

    def post(self, request, pk):
        t = Team.objects.get(id=pk)
        t.delete()
        logging(request.path, True)
        return HttpResponseRedirect('/team/')

class TeamsView(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'teams.html'

    def get(self, request):
        teams = Team.objects.all()
        return Response({'teams': teams})
