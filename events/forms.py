from django import forms

from .data import CATEGORIES


class EventForm(forms.Form):
    title = forms.CharField(
        min_length=5,
        max_length=100,
        label="Title",
        error_messages={
            "required": "Title is required.",
            "min_length": "Title must contain at least 5 characters.",
        },
    )
    description = forms.CharField(
        min_length=20,
        widget=forms.Textarea,
        label="Description",
        error_messages={
            "required": "Description is required.",
            "min_length": "Description must contain at least 20 characters.",
        },
    )
    category = forms.ChoiceField(choices=[(c, c) for c in CATEGORIES])
    location = forms.CharField(
        max_length=100,
        label="Location",
        error_messages={"required": "Location is required."},
    )

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if title.isdigit():
            raise forms.ValidationError("Title cannot contain only numbers.")

        return title

    def clean_location(self):
        location = self.cleaned_data["location"].strip()

        if len(location) < 2:
            raise forms.ValidationError("Location must contain at least 2 characters.")

        return location
