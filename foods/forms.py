from django import forms

from foods.models import Booking


class BookingForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    phone_number = forms.CharField(label="Your phone number", max_length=20)
    email = forms.EmailField(label="Your email")
    how_many_persons = forms.IntegerField(label="How many persons?", min_value=1, max_value=7)
    datetime = forms.DateTimeField(label="Date and Time")

    def save(self):
        data = self.cleaned_data

        booking = Booking.objects.create(
            user_name=data["name"],
            phone_number=data["phone_number"],
            email=data["email"],
            num_of_people=data["how_many_persons"],
            datetime=data["datetime"],
        )

        return booking