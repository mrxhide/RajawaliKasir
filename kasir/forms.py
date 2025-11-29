from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "barcode",
            "sku",
            "category",
            "purchase_price",
            "sell_price",
            "unit",
            "stock",
            "min_stock",
            "image",       # ✔ Tambahkan field foto!
            "is_active",
        ]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "barcode": forms.TextInput(attrs={"class": "form-control"}),
            "sku": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "purchase_price": forms.NumberInput(attrs={"class": "form-control"}),
            "sell_price": forms.NumberInput(attrs={"class": "form-control"}),
            "unit": forms.TextInput(attrs={"class": "form-control"}),
            "stock": forms.NumberInput(attrs={"class": "form-control"}),
            "min_stock": forms.NumberInput(attrs={"class": "form-control"}),

            # ✔ Widget upload file
            "image": forms.FileInput(attrs={"class": "form-control"}),

            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class StokMasukForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(is_active=True),
        widget=forms.Select(attrs={"class": "form-control"})
    )
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    note = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )


class StokKeluarForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(is_active=True),
        widget=forms.Select(attrs={"class": "form-control"})
    )
    quantity = forms.IntegerField(
        min_value=1,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    note = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
