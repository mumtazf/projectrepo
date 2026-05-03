from django.shortcuts import render, redirect
import json
import os
from datetime import datetime
import logging
from .models import User
from .services import StockAnalyzer
from .forms import UserInput

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
logger = logging.getLogger(__name__)

def index(request):
    # The project's template is at
    # sellorhold/sellorhold/templates/index.html -> use 'index.html'
    context = {}
    return render(request, 'sellorhold/index.html', context)

def make_openai_call_for_analysis(request):
    """Here is where I process and send info to the user"""
    if request.method != 'POST':
        return redirect('display_form')

    form = UserInput(request.POST)
    if not form.is_valid():
        return render(request, 'sellorhold/home.html', {'form': form})
    
    company_name = request.POST.get("company_name", "").strip()
    vest_date = request.POST.get("vest_date", "").strip()

    stock_analyzer_service = StockAnalyzer()
    openai_response = stock_analyzer_service.analyze_stock(company_name, vest_date)

    return render(request, 'sellorhold/result.html', openai_response)
        

def display_form(request):
    """Get user input on company and stock vest date"""
    form = UserInput()
    return render(request, 'sellorhold/home.html', {'form': form})

    