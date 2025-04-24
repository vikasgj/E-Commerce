from django import forms

# Newsletter subscription form
class NewsletterForm(forms.Form):
    email = forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(attrs={'placeholder': 'Your email address'})
    )
