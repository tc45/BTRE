from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            # Filter objects from the contact database that match the listing_id and user_id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/' + listing_id)

        new_contact = Contact(listing=listing, listing_id=listing_id,
                              name=name, email=email, phone=phone,
                              message=message, user_id=user_id)

        new_contact.save()
        print('Sending email to realtor: ' + realtor_email)
        # Send mail if saved.
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + ' . Sign into the admin panel for more info',
            'btrealestate123@gmail.com',
            [realtor_email, email, 'btrealestate123@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "Your request has been submitted.  A realtor will get back to you soon.")

        return redirect('/listings/' + listing_id)
