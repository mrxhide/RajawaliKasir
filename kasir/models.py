from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    barcode = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)

    name = models.CharField("Nama Barang", max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    purchase_price = models.DecimalField("Harga Beli", max_digits=12, decimal_places=2)
    sell_price = models.DecimalField("Harga Jual", max_digits=12, decimal_places=2)

    unit = models.CharField("Satuan", max_length=50, default="pcs")

    stock = models.IntegerField("Stok", default=0)
    min_stock = models.IntegerField("Stok Minimum", default=0)

    # ✔ Tambahkan Foto Produk
    image = models.ImageField(upload_to="produk/", blank=True, null=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produk"
        verbose_name_plural = "Produk"

    def __str__(self):
        return f"{self.name} ({self.unit})"


class Sale(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('transfer', 'Transfer'),
        ('qris', 'QRIS'),
    )

    invoice_no = models.CharField(max_length=50, unique=True)
    date_time = models.DateTimeField(auto_now_add=True)
    cashier = models.ForeignKey(User, on_delete=models.PROTECT)

    customer_name = models.CharField(max_length=100, blank=True, null=True)

    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2)
    change_amount = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Penjualan"
        verbose_name_plural = "Penjualan"

    def __str__(self):
        return f"{self.invoice_no} - {self.date_time.strftime('%d/%m/%Y %H:%M')}"


class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    qty = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Detail Penjualan"

    def __str__(self):
        return f"{self.sale.invoice_no} - {self.product.name}"


class StockMovement(models.Model):
    MOVEMENT_TYPE_CHOICES = (
        ('SALE', 'Penjualan'),
        ('PURCHASE', 'Pembelian'),
        ('ADJUSTMENT', 'Penyesuaian'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_TYPE_CHOICES)
    quantity = models.IntegerField()

    note = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Pergerakan Stok"
        verbose_name_plural = "Pergerakan Stok"

    def __str__(self):
        return f"{self.product.name} - {self.movement_type} - {self.quantity}"
