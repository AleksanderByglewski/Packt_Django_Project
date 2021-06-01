from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

import os
from .models import Listing

listings=Listing.objects.all()
print(listings)


def index(request):
    listings=Listing.objects.all()

    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    
    context={'listings':listings}
    return render(request, 'listings/listings.html',context)


def listing(request,listing_id):
    return render(request, 'listings/listing.html')
def search(request):
    return render(request, 'listings/search.html')