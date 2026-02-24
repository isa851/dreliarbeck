from django.shortcuts import redirect
from django.contrib import messages
from .forms import BookingForm

def booking_submit(request):
    if request.method != "POST":
        return redirect("contacts")

    form = BookingForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Заявка отправлена! Мы перезвоним вам в течение 15 минут.")
    else:
        messages.error(request, "Ошибка. Проверьте поля формы.")

    return redirect("contacts")