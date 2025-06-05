from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .api_endpoints.LoginSession.views import SessionLoginAPIView
from accounts.models import User



