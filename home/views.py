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
def DSC(request):  
  return render(request, 'plans/DSC.html')
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


# ///////////////// CC Avenue///////////////////////////


#!/usr/bin/env python

#!/usr/bin/env python

# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.primitives import padding
# from cryptography.hazmat.primitives import hashes, hmac
# from cryptography.hazmat.backends import default_backend
# import binascii

# def pad(data):
#     padder = padding.PKCS7(128).padder()
#     padded_data = padder.update(data.encode())
#     padded_data += padder.finalize()
#     return padded_data

# def unpad(padded_data):
#     unpadder = padding.PKCS7(128).unpadder()
#     data = unpadder.update(padded_data)
#     data += unpadder.finalize()
#     return data.decode()

# def encrypt(plainText, workingKey):
#     iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
#     plainText = pad(plainText)
#     key = hashes.Hash(hashes.MD5(), backend=default_backend())
#     key.update(workingKey.encode())
#     cipher = Cipher(algorithms.AES(key.finalize()), modes.CBC(iv), backend=default_backend())
#     encryptor = cipher.encryptor()
#     ct = encryptor.update(plainText) + encryptor.finalize()
#     return binascii.hexlify(ct).decode()

# def decrypt(cipherText, workingKey):
#     iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
#     key = hashes.Hash(hashes.MD5(), backend=default_backend())
#     key.update(workingKey.encode())
#     cipher = Cipher(algorithms.AES(key.finalize()), modes.CBC(iv), backend=default_backend())
#     decryptor = cipher.decryptor()
#     ct = binascii.unhexlify(cipherText)
#     pt = decryptor.update(ct) + decryptor.finalize()
#     return unpad(pt)

# from ccavutil import encrypt,decrypt
# from string import Template

# def res(encResp):

# 	workingKey = '588E07A459E6C1C7B2ABA1AA639B1EE8'
# 	decResp = decrypt(encResp,workingKey)
# 	data = '<table border=1 cellspacing=2 cellpadding=2><tr><td>'	
# 	data = data + decResp.replace('=','</td><td>')
# 	data = data.replace('&','</td></tr><tr><td>')
# 	data = data + '</td></tr></table>'
	
# 	html = '''\
# 	<html>
# 		<head>
# 			<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
# 			<title>Response Handler</title>
# 		</head>
# 		<body>
# 			<center>
# 				<font size="4" color="blue"><b>Response Page</b></font>
# 				<br>
# 				$response
# 			</center>
# 			<br>
# 		</body>
# 	</html>
# 	'''
# 	fin = Template(html).safe_substitute(response=data)
# 	return fin



from django.shortcuts import render
from django.http import HttpResponse
# from ccavutil import encrypt, decrypt
# from ccavResponseHandler import res
from django.template import Template, Context
from django.views.decorators.csrf import csrf_exempt

accessCode = 'AVTV50KD64BC69VTCB' 	
workingKey = '588E07A459E6C1C7B2ABA1AA639B1EE8'

def webprint(request):
    return render(request, 'dataFrom.htm')

# def checkout(request):
#     return render(request, 'about-us.html')

@csrf_exempt
def ccavResponseHandler(request):
    return render(request, 'dataFrom.htm')

@csrf_exempt
def login(request):
    
    ccavenue = CCAvenue("588E07A459E6C1C7B2ABA1AA639B1EE8", "AVTV50KD64BC69VTCB", "2308221", "http://www.whiteoakconsultant.com/", "http://www.whiteoakconsultant.com/")

    p_merchant_id = request.POST['merchant_id']
    p_order_id = request.POST['order_id']
    p_currency = request.POST['currency']
    p_amount = request.POST['amount']
    p_redirect_url = request.POST['redirect_url']
    p_cancel_url = request.POST['cancel_url']
    p_language = request.POST['language']
    p_billing_name = request.POST['billing_name']
    p_billing_address = request.POST['billing_address']
    p_billing_city = request.POST['billing_city']
    p_billing_state = request.POST['billing_state']
    p_billing_zip = request.POST['billing_zip']
    p_billing_country = request.POST['billing_country']
    p_billing_tel = request.POST['billing_tel']
    p_billing_email = request.POST['billing_email']
    p_delivery_name = request.POST['delivery_name']
    p_delivery_address = request.POST['delivery_address']
    p_delivery_city = request.POST['delivery_city']
    p_delivery_state = request.POST['delivery_state']
    p_delivery_zip = request.POST['delivery_zip']
    p_delivery_country = request.POST['delivery_country']
    p_delivery_tel = request.POST['delivery_tel']
    p_merchant_param1 = request.POST['merchant_param1']
    p_merchant_param2 = request.POST['merchant_param2']
    p_merchant_param3 = request.POST['merchant_param3']
    p_merchant_param4 = request.POST['merchant_param4']
    p_merchant_param5 = request.POST['merchant_param5']
    p_promo_code = request.POST['promo_code']
    p_customer_identifier = request.POST['customer_identifier']

    merchant_data='merchant_id='+p_merchant_id+'&'+'order_id='+p_order_id + '&' + "currency=" + p_currency + '&' + 'amount=' + p_amount+'&'+'redirect_url='+p_redirect_url+'&'+'cancel_url='+p_cancel_url+'&'+'language='+p_language+'&'+'billing_name='+p_billing_name+'&'+'billing_address='+p_billing_address+'&'+'billing_city='+p_billing_city+'&'+'billing_state='+p_billing_state+'&'+'billing_zip='+p_billing_zip+'&'+'billing_country='+p_billing_country+'&'+'billing_tel='+p_billing_tel+'&'+'billing_email='+p_billing_email+'&'+'delivery_name='+p_delivery_name+'&'+'delivery_address='+p_delivery_address+'&'+'delivery_city='+p_delivery_city+'&'+'delivery_state='+p_delivery_state+'&'+'delivery_zip='+p_delivery_zip+'&'+'delivery_country='+p_delivery_country+'&'+'delivery_tel='+p_delivery_tel+'&'+'merchant_param1='+p_merchant_param1+'&'+'merchant_param2='+p_merchant_param2+'&'+'merchant_param3='+p_merchant_param3+'&'+'merchant_param4='+p_merchant_param4+'&'+'merchant_param5='+p_merchant_param5+'&'+'promo_code='+p_promo_code+'&'+'customer_identifier='+p_customer_identifier+'&'

    merchant_data = {
    'merchant_id': p_merchant_id,
    'order_id': p_order_id,
    'currency': p_currency,
    'amount': p_amount,
    'redirect_url': p_redirect_url,
    'cancel_url': p_cancel_url,
    'language': p_language,
    'billing_name': p_billing_name,
    'billing_address': p_billing_address,
    'billing_city': p_billing_city,
    'billing_state': p_billing_state,
    'billing_zip': p_billing_zip,
    'billing_country': p_billing_country,
    'billing_tel': p_billing_tel,
    'billing_email': p_billing_email,
    'delivery_name': p_delivery_name,
    'delivery_address': p_delivery_address,
    'delivery_city': p_delivery_city,
    'delivery_state': p_delivery_state,
    'delivery_zip': p_delivery_zip,
    'delivery_country': p_delivery_country,
    'delivery_tel': p_delivery_tel,
    'merchant_param1': p_merchant_param1,
    'merchant_param2': p_merchant_param2,
    'merchant_param3': p_merchant_param3,
    'merchant_param4': p_merchant_param4,
    'merchant_param5': p_merchant_param5,
    'promo_code': p_promo_code,
    'customer_identifier': p_customer_identifier
    }

    # encryption = encrypt(merchant_data, workingKey)
    encrypted_data = ccavenue.encrypt(merchant_data)


    html = '''\
    <html>
    <head>
        <title>Sub-merchant checkout page</title>
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    </head>
    <body>
    <form id="nonseamless" method="post" name="redirect" action="https://secure.ccavenue.com/transaction/transaction.do?command=initiateTransaction" > 
            <input type="hidden" id="encRequest" name="encRequest" value=$encReq>
            <input type="hidden" name="access_code" id="access_code" value=$xscode>
            <script language='javascript'>document.redirect.submit();</script>
    </form>    
    </body>
    </html>
    '''

    context = Context({"encReq": encrypted_data, "xscode": accessCode})
    template = Template(html)
    return HttpResponse(template.render(context))



from django.shortcuts import render
from pay_ccavenue import CCAvenue

def payment(request):
    ccavenue = CCAvenue("588E07A459E6C1C7B2ABA1AA639B1EE8", "AVTV50KD64BC69VTCB", "2308221", "http://www.whiteoakconsultant.com/", "http://www.whiteoakconsultant.com/")


    
    # ccavenue = CCAvenue(settings.CCAVENUE_WORKING_KEY, settings.CCAVENUE_ACCESS_CODE, settings.CCAVENUE_MERCHANT_CODE, settings.CCAVENUE_REDIRECT_URL, settings.CCAVENUE_CANCEL_URL)
    form_data = {
        "amount": "10",
        "currency": "INR",
        "order_id": "123456",
        # add other required fields as per CCAvenue documentation
    }
    encrypted_data = ccavenue.encrypt(form_data)
    return render(request, 'pages/author.html', {"encrypted_data": encrypted_data})

def payment_response(request):
    ccavenue = CCAvenue("588E07A459E6C1C7B2ABA1AA639B1EE8", "AVTV50KD64BC69VTCB", "2308221", "http://www.whiteoakconsultant.com/", "http://www.whiteoakconsultant.com/")
    # ccavenue = CCAvenue(settings.CCAVENUE_WORKING_KEY, settings.CCAVENUE_ACCESS_CODE, settings.CCAVENUE_MERCHANT_CODE, settings.CCAVENUE_REDIRECT_URL, settings.CCAVENUE_CANCEL_URL)
    response_data = request.POST
    decrypted_data = ccavenue.decrypt(response_data)
    # Handle the decrypted_data as required
    return render(request, 'payment_response.html', {"response": decrypted_data})


from django.shortcuts import HttpResponse, render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from home.utils import *

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def checkout(request):
    
    amt = request.POST.get('amt')
    service = request.POST.get('service')
    
    p_merchant_id = settings.CC_MERCHANT_ID

    # current site domain
    current_site = settings.CURRENT_SITE_DOMAIN

    p_order_id = '0001'
    p_currency = settings.CC_CURRENCY
    p_amount = amt

    p_redirect_url = str(current_site) + '/payment_success/'
    p_cancel_url = str(current_site) + '/payment_cancel/'

    p_language = settings.CC_LANG

    p_billing_name = 'White Oak User'
    p_billing_address = '12/ Dubai'
    p_billing_city = 'Jalgoan'
    p_billing_state = 'Maharshtra'
    p_billing_zip = '786125'
    p_billing_country = settings.CC_BILL_CONTRY
    p_billing_tel = '8875091601'
    p_billing_email = 'testemail@gmail.com'

    p_delivery_name = ''
    p_delivery_address = ''
    p_delivery_city = ''
    p_delivery_state = ''
    p_delivery_zip = ''
    p_delivery_country = 'India'
    p_delivery_tel = ''

    p_merchant_param1 = ''
    p_merchant_param2 = ''
    p_merchant_param3 = ''
    p_merchant_param4 = ''
    p_merchant_param5 = ''
    p_promo_code = ''

    p_customer_identifier = ''
    merchant_data = 'merchant_id=' + p_merchant_id + '&' + 'order_id=' + p_order_id + '&' + "currency=" + p_currency + \
                    '&' + 'amount=' + p_amount + '&' + 'redirect_url=' + p_redirect_url + '&' + 'cancel_url=' + p_cancel_url + \
                    '&' + 'language=' + p_language + '&' + 'billing_name=' + p_billing_name + '&' + 'billing_address=' + p_billing_address + \
                    '&' + 'billing_city=' + p_billing_city + '&' + 'billing_state=' + p_billing_state + '&' + 'billing_zip=' + p_billing_zip + \
                    '&' + 'billing_country=' + p_billing_country + '&' + 'billing_tel=' + p_billing_tel + '&' + 'billing_email=' + p_billing_email + \
                    '&' + 'delivery_name=' + p_delivery_name + '&' + 'delivery_address=' + p_delivery_address + '&' + 'delivery_city=' + p_delivery_city + \
                    '&' + 'delivery_state=' + p_delivery_state +  '&' + 'delivery_zip=' + p_delivery_zip + '&' + 'delivery_country=' + p_delivery_country + \
                    '&' + 'delivery_tel=' + p_delivery_tel + '&' + 'merchant_param1=' + p_merchant_param1 + '&' + 'merchant_param2=' + p_merchant_param2 + \
                    '&' + 'merchant_param3=' + p_merchant_param3 + '&' + 'merchant_param4=' + p_merchant_param4 + '&' + 'merchant_param5=' + p_merchant_param5 + \
                    '&' + 'promo_code=' + p_promo_code + '&' + 'customer_identifier=' + p_customer_identifier + '&'

    encryption = encrypt(merchant_data, settings.CC_WORKING_KEY)
    
    params = {
        'p_redirect_url': p_redirect_url,
        'encryption': encryption, 'access_code': settings.CC_ACCESS_CODE,
        'cc_url': settings.CC_URL, 'p_amount': float(amt),'current_site':current_site,'service':service
    }

    return render(request, 'pages/payment.html', params)


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings

@csrf_exempt
def payment_success(request):
    import urllib.parse
    """
    Method to handle cc-ave payment success.
    :param request:
    :return:
    """
    response_data = request.POST
    response_chiper = response_data.get('encResp')
    response_string = decrypt(response_chiper, settings.CC_WORKING_KEY)
    response_data = urllib.parse.parse_qs(response_string)
    print(response_data)
    print(type(response_data))
    # print(payment_list)

# import urllib.parse

# # Your response string
# response_string = 'order_id=0001&tracking_id=112903827686&bank_ref_no=663698&order_status=Success&failure_message=&payment_mode=Credit Card&card_name=Visa&status_code=null&status_message=SUCCESS¤cy=INR&amount=1.00&billing_name=Foo Bar&billing_address=12/Foo Bar&billing_city=Tinsukia&billing_state=Assam&billing_zip=786125&billing_country=India&billing_tel=9957767675&billing_email=vishal.pandey@chat360.io&delivery_name=Foo Bar&delivery_address=12/Foo Bar&delivery_city=Tinsukia&delivery_state=Assam&delivery_zip=786125&delivery_country=India&delivery_tel=9957767675&merchant_param1=&merchant_param2=&merchant_param3=&merchant_param4=&merchant_param5=&vault=N&offer_type=null&offer_code=null&discount_value=0.0&mer_amount=1.00&eci_value=null&retry=N&response_code=0&billing_notes=&trans_date=07/06/2023 22:28:01&bin_country=INDIA'

# # Parse the response string
# response_data = urllib.parse.parse_qs(response_string)

# Check the order_status
    beautiful_message = "Invalid Response"
    if response_data['order_status'][0] == "Success":
        beautiful_message = f"""
        Dear {response_data['billing_name'][0]},

        We are pleased to confirm that your recent transaction with Order ID: {response_data['order_id'][0]} on date {response_data['trans_date'][0]} was successful. 

        Order Status: {response_data['order_status'][0]}
        Payment Mode: {response_data['payment_mode'][0]}
        Card Name: {response_data['card_name'][0]}
        Status Message: {response_data['status_message'][0]}
        Transaction Amount: {response_data['amount'][0]} {response_data['currency'][0]}
        Merchant Amount: {response_data['mer_amount'][0]}

        Thank you for your trust,
        Support Team
        """
    elif response_data['order_status'][0] == "Failure":
        beautiful_message = f"""
        Dear {response_data['billing_name'][0]},

        We regret to inform you that your recent transaction with Order ID: {response_data['order_id'][0]} on date {response_data['trans_date'][0]} was unsuccessful. 

        Order Status: {response_data['order_status'][0]}
        Payment Mode: {response_data['payment_mode'][0]}
        Card Name: {response_data['card_name'][0]}
        Status Message: {response_data['status_message'][0]}
        Transaction Amount: {response_data['amount'][0]} {response_data['currency'][0]}
        Merchant Amount: {response_data['mer_amount'][0]}

        Please contact our support team if you need any further assistance.

        Thank you,
        Support Team
        """

    print(beautiful_message)
    params = {
    'message' : beautiful_message,
    }

    return render(request, 'pages/author.html', params)









    # return HttpResponse((beautiful_message))

@csrf_exempt
def payment_cancel(request):
    """
    Method to handle cc-ave.
    :param request: data
    :return: status
    """
    response_data = request.POST
    response_chiper = response_data.get('encResp')
    payment_list = decrypt(response_chiper, settings.CC_WORKING_KEY)
    print(payment_list)
    # payment cancel code

    return HttpResponse('Cancel')
