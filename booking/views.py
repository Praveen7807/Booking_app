from django.shortcuts import render

def booking_view(request):
    if request.method == 'POST':
        date = request.POST.get('booking_date')
        persons = request.POST.get('no_of_persons')
        rooms = request.POST.get('no_of_rooms')
        # Logic for processing booking can be added here
        return render(request, 'booking/confirmation.html', {
            'date': date,
            'persons': persons,
            'rooms': rooms,
        })
    return render(request, 'booking/booking.html')
