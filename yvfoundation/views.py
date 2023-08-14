from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import FormView,TemplateView

from .models import Contact
from .forms import ContactForm

def yvfoundationhome(request):
    form = ContactForm()
    context = {"form": form}
    return render(request,"yvfoundation/index.html",context)

class AboutView(TemplateView):
    template_name = "yvfoundation/about.html"


# class ContactView(FormView):
#     template_name = 'yvfoundation/contact.html'
#
#     def get(self, request, *args, **kwargs):
#         form = ContactForm()
#         context = {"form": form}
#         return render(self.request, "yvfoundation/contact.html", context)
#
#     def post(self, request, *args, **kwargs):
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             topic = form.cleaned_data['topic']
#             message = form.cleaned_data['message']
#             sender = form.cleaned_data.get('sender', 'noreply@example.com')
#             form.save()
#             # send_mail(
#             #     'Feedback from your site, topic: %s' % topic,
#             #     message, sender,
#             #     ['molusi.abigail@gmail.com']
#             # )
#             form = ContactForm()
#             return redirect('yvfoundation:home')
#         else:
#             form.errors
# views.py



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender')
            if not sender:
                sender="anonymous"
            send_mail(
                subject=f"topic:{topic}",
                message=f'New message: "{message}" sent by: {sender}',
                from_email='molusi.abigail@gmail.com',  # Change to your desired email sender
                recipient_list=['yvfoundation1@gmail.com'],  # Change to the recipient email
                fail_silently=False,
            )
            print("Got in==================================")
            return redirect('yvfoundation:home')
        else:
            form.errors
    else:
        form = ContactForm()
    context={"form":form}
    return render(request,"yvfoundation/contact.html", context)


