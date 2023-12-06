from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.db.models import Count
from django.conf import settings
from stripe.error import StripeError

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def home(request):
    context = {
      'datas': ['Promo1', 'Promo2', 'Promo 3'],
      'countDatas': 3
    }
    return render(request, 'Home/home.html',context)
def prueba1(request):
    return render(request, 'Admin/dashboard.html')
  
def prueba2(request):
    return render(request, 'Common/mainAdmin.html')
  
def mainAdmin(request):
    return render(request, 'Common/mainAdmin.html')

def register(request):
 if request.method == 'POST':
  form = UserRegisterForm(request.POST)
  if form.is_valid():
   form.save()
   username = form.cleaned_data['username']
   print(request.POST)
   subject = 'Registro Éxitoso'
   message = ''
   from_email = 'chimalcarlos261198@gmail.com'
   recipient_list = [request.POST['email']]
   context = {
        'user': request.POST['username'],
        'password': request.POST['password1'],
   }
   html_content = render_to_string('Mail/registerMail.html', context)
   send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_content)
   return redirect('login')
 else:
  form = UserRegisterForm()
 context = { 'form' : form }
 return render(request, 'Authentication/register.html', context)

def dashboard_view(request):
  packageLabels=[]
  packageValues=[]
  package = Question.objects.values('package').annotate(total=Count('package'))
  for packageData in package:
    packageLabels.append(packageData['package'])
    packageValues.append(packageData['total'])
  
  packagingLabels=[]
  packagingValues=[]
  packaging = Question.objects.values('packaging').annotate(total=Count('packaging'))
  for packagingData in packaging:
    packagingLabels.append(packagingData['packaging'])
    packagingValues.append(packagingData['total'])
  
  personLabels=[]
  personValues=[]
  person = Question.objects.values('person').annotate(total=Count('person'))
  for personData in person:
    personLabels.append(personData['person'])
    personValues.append(personData['total'])  
  
  sendLabels=[]
  sendValues=[]
  send = Question.objects.values('send').annotate(total=Count('send'))
  for sendData in send:
    sendLabels.append(sendData['send'])
    sendValues.append(sendData['total'])
  
  categoryLabels=[]
  categoryValues=[]
  category = Question.objects.values('category').annotate(total=Count('category'))
  for categoryData in category:
    categoryLabels.append(categoryData['category'])
    categoryValues.append(categoryData['total'])
  
  reasonPurchaseLabels=[]
  reasonPurchaseValues=[]
  reasonPurchase = Question.objects.values('reasonPurchase').annotate(total=Count('reasonPurchase'))
  for reasonPurchaseData in reasonPurchase:
    reasonPurchaseLabels.append(reasonPurchaseData['reasonPurchase'])
    reasonPurchaseValues.append(reasonPurchaseData['total'])
    
  markLabels=[]
  markValues=[]
  mark = Question.objects.values('mark').annotate(total=Count('mark'))
  for markData in mark:
    markLabels.append(markData['mark'])
    markValues.append(markData['total'])
  
  articleLabels=[]
  articleValues=[]
  article = Question.objects.values('article').annotate(total=Count('article'))
  for articleData in article:
    articleLabels.append(articleData['article'])
    articleValues.append(articleData['total'])
  
  context = {
        'package_labels': packageLabels,
        'package_values' : packageValues,
        'packaging_labels': packagingLabels,
        'packaging_values' : packagingValues,
        'person_labels': personLabels,
        'person_values' : personValues,
        'send_labels': sendLabels,
        'send_values' : sendValues,
        'category_labels': categoryLabels,
        'category_values' : categoryValues,
        'reason_purchase_labels': reasonPurchaseLabels,
        'reason_purchase_values' : reasonPurchaseValues,
        'mark_labels': markLabels,
        'mark_values' : markValues,
        'article_labels': articleLabels,
        'article_values' : articleValues,
   }
  return render(request, 'Admin/dashboard.html',context)

def seller(request):
    return render(request, 'Admin/seller.html')

def list_products(request):
    try:
        products = stripe.Product.list()
        productsList = []
        for product in products['data']:
            price = stripe.Price.retrieve(product["default_price"]) # type: ignore
            productsList.append({
                'name': product["name"], # type: ignore
                'description': product["description"], # type: ignore
                'price': price['unit_amount'] / 100.0,
            })

        context = {
            'products': productsList
        }

        return render(request, 'Common/products.html', context)
    except StripeError as e:
        print(f"Error de Stripe: {str(e)}")
        return render(request, 'Common/products.html')
           
def payments(request):
    if request.method == 'POST':
      try:
          create = stripe.PaymentIntent.create(amount=5000,currency="mxn",payment_method="pm_card_visa",)
          print(create)
      except Exception as e:
          return render(request, 'Common/payment_result.html', {'success': False, 'error': str(e)})
      return render(request, 'Common/payment_result.html', {'success': True})
    return render(request, 'Common/payment.html')
