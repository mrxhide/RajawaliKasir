from django.urls import path
from . import views

app_name = 'kasir'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # POS
    path('pos/', views.pos, name='pos'),
    path('pos/items/', views.pos_items, name='pos_items'),
    path('pos/cart/', views.pos_cart, name='pos_cart'),
    path('pos/cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('pos/cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
    path('pos/checkout/', views.pos_checkout, name='pos_checkout'),
    path('pos/struk/<str:invoice>/', views.pos_struk, name='pos_struk'),
    path('pos/cart/increase/<int:item_id>/', views.cart_increase, name='cart_increase'),
    path('pos/cart/decrease/<int:item_id>/', views.cart_decrease, name='cart_decrease'),


    # Hapus session setelah SweetAlert
    path("remove_pos_success/", views.remove_pos_success, name="remove_pos_success"),

    # PRODUK
    path('produk/', views.product_list, name='product_list'),
    path('produk/tambah/', views.product_add, name='product_add'),
    path('produk/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('produk/hapus/<int:pk>/', views.product_delete, name='product_delete'),

    # STOK
    path('stok/masuk/', views.stok_masuk, name='stok_masuk'),
    path('stok/masuk/riwayat/', views.stok_masuk_list, name='stok_masuk_list'),
    path('stok/keluar/', views.stok_keluar, name='stok_keluar'),
    path('stok/keluar/riwayat/', views.stok_keluar_list, name='stok_keluar_list'),

    # LAPORAN
    path('laporan/penjualan/', views.sales_report, name='sales_report'),
    path('laporan/penjualan/export/excel/', views.sales_report_export_excel, name='sales_report_export_excel'),
    path('laporan/penjualan/export/pdf/', views.sales_report_export_pdf, name='sales_report_export_pdf'),

    path("laporan/reset_detail/", views.reset_detail, name="reset_detail"),
    path("laporan/reset_rekap/", views.reset_rekap, name="reset_rekap"),

    path('laporan/detail/export/pdf/', views.export_detail_pdf, name='export_detail_pdf'),
    path('laporan/detail/export/excel/', views.export_detail_excel, name='export_detail_excel'),

    # LOGOUT
    path("logout/", views.logout_view, name="logout_kasir"),
]
