from django import forms

class AddListingForm(forms.Form):
    item_name = forms.CharField(max_length=150)
    price = forms.FloatField()
    listing_title = forms.CharField(max_length=150)
    description = forms.CharField(max_length=2000)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
