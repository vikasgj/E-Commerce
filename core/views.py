from django.shortcuts import render, redirect
from .forms import NewsletterForm  # Ensure this import is correct
from .models import InstagramFeed

# Homepage view
def home(request):
    # Fetch Instagram posts
    instagram_posts = InstagramFeed.objects.all()[:6]  # Get the latest 6 Instagram posts
    return render(request, 'core/home.html', {
        'instagram_posts': instagram_posts,
    })

# Newsletter subscription handler
def subscribe_newsletter(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Save the email to the database
            Newsletter.objects.create(email=email)
            return redirect('home')  # Redirect to the homepage after subscription
    else:
        form = NewsletterForm()

    return render(request, 'core/home.html', {'form': form})
