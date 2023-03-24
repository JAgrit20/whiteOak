from django.shortcuts import render, redirect
from theme_material_kit.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import logout

from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from .models import Payment_details
import datetime
import pytz
from django.shortcuts import  redirect
from django.contrib import messages
# Create your views here.


# Authentication
def registration(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      print('Account created successfully!')
      return redirect('/accounts/login/')
    else:
      print("Registration failed!")
  else:
    form = RegistrationForm()
  
  context = {'form': form}
  return render(request, 'accounts/sign-up.html', context)

class UserLoginView(auth_views.LoginView):
  template_name = 'accounts/sign-in.html'
  form_class = LoginForm
  success_url = '/'

class UserPasswordResetView(auth_views.PasswordResetView):
  template_name = 'accounts/password_reset.html'
  form_class = UserPasswordResetForm

class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
  template_name = 'accounts/password_reset_confirm.html'
  form_class = UserSetPasswordForm

class UserPasswordChangeView(auth_views.PasswordChangeView):
  template_name = 'accounts/password_change.html'
  form_class = UserPasswordChangeForm

def user_logout_view(request):
  logout(request)
  return redirect('/accounts/login/')


# Pages
def index(request):

  return render(request, 'pages/index.html')

def contact_us(request):
  return render(request, 'pages/contact-us.html')

def about_us(request):
  return render(request, 'pages/about-us.html')

def get_time():
    dtobj1 = datetime.datetime.utcnow()  # utcnow class method
    dtobj3 = dtobj1.replace(tzinfo=pytz.UTC)  # replace method
    dtobj_india = dtobj3.astimezone(pytz.timezone("Asia/Calcutta"))  # astimezone method 
    dtobj_india = dtobj_india.strftime("%Y-%m-%d %H:%M:%S")
    dtobj_indiaa = str(dtobj_india)
    return dtobj_indiaa

def save_payment_details(request):
    user_id = ""
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']
        service = request.POST['service']
        transaction_id = request.POST['transaction_id']
        comments = request.POST['comments']
        if request.user.is_authenticated:
          user_id = request.user.id

        rec = Payment_details.objects.create(time=get_time(), transaction_id=transaction_id, user_name=name, user_id=user_id, amount=amount, Services_from_user=service, comments=comments)
        rec.save()

        # Show success message using Django messages framework
        messages.success(request, 'Your form has been submitted successfully!')

        payments = Payment_details.objects.filter(user_id=user_id).values()
        print(payments)

        context ={'payments':payments}

        # Redirect to a thank you page
        return render(request, 'pages/author.html',context)
    else:
        return render(request, 'pages/author.html')


def author(request):
  context = {}
  user_id=""
  if request.user.is_authenticated:
    username = request.user.username
    user_id = request.user.id
    user_name = User.objects.get(username=username)
    email = User.objects.get(username=username).email
    payments = Payment_details.objects.filter(user_id=user_id).values()
    print(payments)

    print(user_name)
    context = {"user_name":user_name,"email":email,'payments':payments}
  return render(request, 'pages/author.html',context)

def Incometax(request):
  return render(request, 'plans/Incometax.html')
def GST(request):
  return render(request, 'plans/GST.html')
def accounting(request):
  return render(request, 'plans/accounting.html')
def Business_Incorporation(request):
  return render(request, 'plans/Business_Incorporation.html')
def PMS(request):
  return render(request, 'plans/PMS.html')
def Compliance(request):
  return render(request, 'plans/Compliance.html')
def Trademark(request):
  return render(request, 'plans/Trademark.html')


# Sections
def presentation(request):
  return render(request, 'sections/presentation.html')
  
def page_header(request):
  return render(request, 'sections/page-sections/hero-sections.html')

def features(request):
  return render(request, 'sections/page-sections/features.html')

def navbars(request):
  return render(request, 'sections/navigation/navbars.html')

def nav_tabs(request):
  return render(request, 'sections/navigation/nav-tabs.html')

def pagination(request):
  return render(request, 'sections/navigation/pagination.html')

def forms(request):
  return render(request, 'sections/input-areas/forms.html')

def inputs(request):
  return render(request, 'sections/input-areas/inputs.html')

def avatars(request):
  return render(request, 'sections/elements/avatars.html')

def badges(request):
  return render(request, 'sections/elements/badges.html')

def breadcrumbs(request):
  return render(request, 'sections/elements/breadcrumbs.html')

def buttons(request):
  return render(request, 'sections/elements/buttons.html')

def dropdowns(request):
  return render(request, 'sections/elements/dropdowns.html')

def progress_bars(request):
  return render(request, 'sections/elements/progress-bars.html')

def toggles(request):
  return render(request, 'sections/elements/toggles.html')

def typography(request):
  return render(request, 'sections/elements/typography.html')

def alerts(request):
  return render(request, 'sections/attention-catchers/alerts.html')

def modals(request):
  return render(request, 'sections/attention-catchers/modals.html')

def tooltips(request):
  return render(request, 'sections/attention-catchers/tooltips-popovers.html')