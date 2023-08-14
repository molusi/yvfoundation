from django import forms
from django.forms import ModelForm
from . models import Contact


TOPIC_CHOICES = (
 ('general', 'General enquiry'),
 ('suggestion', 'Suggestion')
)
class ContactForm(ModelForm):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES,widget=forms.Select(attrs={'class': 'p-2 form-control caret'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "message", "rows": 4, "id":"message","cols": 25,"class":"p-2 form-control"}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Your Email (Optional)","id":"sender","class":"p-2 form-control"}),required=False)
    class Meta:
        model = Contact
        fields = "__all__"