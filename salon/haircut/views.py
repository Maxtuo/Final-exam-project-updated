from django.shortcuts import render
from . models import Appointment


def home_page(request):
    if request.method == 'POST':
        barber = request.POST.get('barber')
        user = request.POST.get('user')
        time = request.POST.get('time')
        appointment_obj = Appointment.objects.create(
            barber=barber,
            user=user,
            time=time
        )

        all_appointment = Appointment.objects.all()
        context = {'appointments': all_appointment}

        return render(request, 'haircut/home_page.html', context)
    if request.method == "GET":
        all_appointment = Appointment.objects.all()
        context = {'appointments': all_appointment}
        return render(request, 'haircut/home_page.html', context)
