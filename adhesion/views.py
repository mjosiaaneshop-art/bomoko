from django.shortcuts import render, redirect

from .forms import AdherentForm


def accueil(request):

    if request.method == 'POST':

        form = AdherentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('merci')

    else:

        form = AdherentForm()

    return render(
        request,
        'adhesion/index.html',
        {'form': form}
    )


def merci(request):

    return render(
        request,
        'adhesion/merci.html'
    )