from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import redirect

from .forms import OrderForm
from .models import MailModel


def redirect(request):
    response = redirect('main')
    return response


def about(request):
    return render(request, 'about.html')


def main(request):
    return render(request, 'main.html')


def blueprints(request):
    return render(request, 'blueprints.html')

def brochure_printing(request):
    return render(request, 'brochure_printing.html')

def document_printing(request):
    return render(request, 'document_printing.html')

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            message = f"Пришел заказ от {request.POST['name']}\n"
            message += f"Телефон: {request.POST['phone']}\n"
            message += f"Почта: {request.POST['mail']}\n"
            message += f"Коментарий: {request.POST['comments']}\n"
            email = EmailMessage(
                'Новый заказ',
                message,
                'Dont Reply <do_not_reply@domain.com>',
                [mail.mail for mail in MailModel.objects.all()],
                headers={'Reply-To': 'test@gmail.com'}
            )
            if request.FILES:
                try:
                    uploaded_file = request.FILES['photo_file']
                    email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                except Exception:
                    pass
                try:
                    uploaded_file = request.FILES['document_file']
                    email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
                except Exception:
                    pass
            email.send()
            form.save()
            return render(request, 'order.html', {'info': 'Заказ отправлен.'})
        else:
            return render(request, 'order.html', {'form': form})
        return render(request, 'order.html')
    else:
        return render(request, 'order.html')

def photo_printing(request):
    return render(request, 'photo_printing.html')

def photo_processing(request):
    return render(request, 'photo_processing.html')

def services(request):
    return render(request, 'services.html')

def shirt_printing(request):
    return render(request, 'shirt_printing.html')