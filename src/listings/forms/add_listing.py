from django import forms
from crispy_forms.helper import FormHelper
from listings.models import Listing

# NOTE: In the model, all categories must have lowercase names. The value on the right of the tuple is what is shown
# to the user, and the value on the left is what is passed in as the key
# http://www.learningaboutelectronics.com/Articles/How-to-create-a-drop-down-list-in-a-Django-form.php
CATEGORIES = [
        ('anthropology', 'Anthropology'),
        ('biology', 'Biology'),
        ('chemical_physical_sciences', 'Chemical Physical Sciences'),
        ('economics', 'Economics'),
        ('english_drama', 'English & Drama'),
        ('geography', 'Geography'),
        ('history', 'Historical Studies'),
        ('iccit', 'ICCIT'),
        ('language_studies', 'Language Studies'),
        ('management', 'Management'),
        ('mcs', 'MCS'),
        ('philosophy', 'Philosophy'),
        ('political_science', 'Political Science'),
        ('psychology', 'Psychology'),
        ('sociology', 'Sociology'),
        ('visual_studies', 'Visual Studies'),
        ('wgs', 'Women & Gender Studies'),
        ('tutor', 'Tutor Services'),
        ('electronics', 'Electronics'),
        ('misc', 'Miscellaneous')
    ]

class AddListingForm(forms.Form):
    item_name = forms.CharField(max_length=150)
    price = forms.FloatField()
    listing_title = forms.CharField(max_length=150)
    description = forms.CharField(max_length=2000)
    # Choose one of the subject categories and record it (temporarily) as a string. 
    # When creating a listing, query the Category model for the right row and create the correct key constraint
    category = forms.CharField(label='Category', widget=forms.Select(choices=CATEGORIES)) 
    image = forms.ImageField(required=False)


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class EditListingForm(forms.Form):
    image = forms.ImageField(required=False)
    def __init__(self, *args, **kwargs):
        super(EditListingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
    
    class Meta:
        model = Listing
        fields = ("image")
