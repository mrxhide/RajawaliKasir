from django.shortcuts import redirect
from django.urls import reverse

class KasirAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # jika belum login → biarkan login view yg menangani
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Izinkan logout
        if request.path.startswith("/logout/"):
            return self.get_response(request)

        # ❗ Izinkan semua HTMX request (MUAT /pos/items/ dan /pos/cart/)
        if request.headers.get("HX-Request") == "true":
            return self.get_response(request)

        # ROLE admin → bebas
        if request.user.groups.filter(name="Admin").exists():
            return self.get_response(request)

        # ROLE kasir – hanya boleh akses POS
        if request.user.groups.filter(name="Kasir").exists():
            allowed_paths = [
                "/pos/",
                "/pos/items/",
                "/pos/cart/",
                "/pos/add/",
                "/pos/checkout/",
                "/pos/remove/",
            ]

            # Izinkan prefix POS (lebih aman)
            if request.path.startswith("/pos/"):
                return self.get_response(request)

            # selain POS → tendang ke /pos/
            return redirect("/pos/")

        # default → lanjutkan
        return self.get_response(request)
