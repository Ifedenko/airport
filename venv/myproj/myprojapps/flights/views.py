from django.shortcuts import render, redirect
from django.views.generic.base import View
from myprojapps.flights.models import Flight
from myprojapps.flights.forms import HFlightForm
class FlightsView(View):
    """Список рейсов"""
    def get(self, request):
        flightss = Flight.objects.all()
        return render(request, "Hflights/flights_list.html", {"flight_list": flightss})
def flightT(request):
    if request.method == "POST":
        form = HFlightForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = HFlightForm()
    return render(request,'Hflights/index.html',{'form':form})
def show(request):
    Tflights = Flight.objects.all()
    return render(request,"Hflights/show.html",{'Tflights':Tflights})
def edit(request, id):
    Tflight = Flight.objects.get(id=id)
    return render(request,'Hflights/edit.html', {'Tflight':Tflight})
def update(request, id):
    Tflight = Flight.objects.get(id=id)
    form = HFlightForm(request.POST, instance=Tflight)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'Hflights/edit.html', {'Tflight':Tflight})
def destroy(request, id):
    Tflight = Flight.objects.get(id=id)
    Tflight.delete()
    return redirect("/show")
