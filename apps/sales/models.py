from django.db import models
from django.utils import timezone
import datetime as dt
from apps.products import models as prods


# Create your models here.
class OcOrderQuerySet(models.QuerySet):
    def successful(self):
        valid_status = [2, 3, 4]
        return self.filter(payment_status_id__in=valid_status)

    def today(self):
        today_data = timezone.datetime.today()
       #ß today_data = '2019-06-17'
        return self.filter(date_added__contains=today_data)

    def order_range(self, startdate, enddate):
        return self.filter(date_added__gte=startdate, date_added__lte=enddate)


class OcOrderManager(models.Manager):
    def get_queryset(self):
        return OcOrderQuerySet(self.model, using=self._db)

    def successful(self):
        return self.get_queryset().successful()

    def orders_today(self, blsuccessful = True):
        if (blsuccessful):
            return self.get_queryset().successful().today()
        else:
            return self.get_queryset().today()

    def orders_week(self, blsuccessful = True):
        today = dt.date.today()
        startdate = today - dt.timedelta(days=today.weekday())
        enddate = startdate + dt.timedelta(days=6)
        if (blsuccessful):
            return self.get_queryset().successful().order_range(startdate, enddate)
        else:
            return self.get_queryset().order_range(startdate, enddate)

    def orders_month(self, blsuccessful = True):
        today = dt.date.today()
        startdate = today.replace(day=1)
        if startdate.month == 12:  # December
            enddate = dt.date(startdate.year, startdate.month, 31)
        else:
            enddate = dt.date(startdate.year, startdate.month + 1, 1) - dt.timedelta(days=1)

        if (blsuccessful):
            return self.get_queryset().successful().order_range(startdate, enddate)
        else:
            return self.get_queryset().order_range(startdate, enddate)

    def orders_range(self, startdate, enddate, blsuccessful = True):
        if(blsuccessful):
            return self.get_queryset().successful().order_range(startdate, enddate)
        else:
            return self.get_queryset().order_range(startdate, enddate)


class OcCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_group_id = models.IntegerField()
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    company = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=96, blank=True, null=True)
    telephone = models.CharField(max_length=32, blank=True, null=True)
    alt_telephone = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    cart = models.TextField(blank=True, null=True)
    wishlist = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField()
    address_id = models.IntegerField()
    custom_field = models.TextField()
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    safe = models.IntegerField()
    token = models.TextField()
    code = models.CharField(max_length=40)
    date_added = models.DateTimeField(blank=True, null=True)
    discount_rate = models.FloatField(blank=True, null=True)
    account_terms_type = models.CharField(max_length=5, blank=True, null=True)
    account_terms_days = models.IntegerField(blank=True, null=True)
    old_customer = models.IntegerField()
    xero_id = models.CharField(max_length=512, blank=True, null=True)
    whitelabel = models.CharField(max_length=64)
    subemailtoken = models.CharField(max_length=256, blank=True, null=True)
    consentchangedate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_customer'

class SsanOrderStatus(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ssan_order_status'


class SsanPaymentStatus(models.Model):
    status_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ssan_payment_status'

class SsanOrderProductStatus(models.Model):
    status_title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ssan_order_product_status'

class OcOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26, blank=True, null=True)
    purchase_order_ref = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer = models.ForeignKey(OcCustomer, models.DO_NOTHING)
    customer_group_id = models.IntegerField()
    company = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32, blank=True, null=True)
    custom_field = models.TextField(blank=True, null=True)
    payment_firstname = models.CharField(max_length=32, blank=True, null=True)
    payment_lastname = models.CharField(max_length=32, blank=True, null=True)
    payment_company = models.CharField(max_length=60, blank=True, null=True)
    payment_telephone = models.CharField(max_length=32, blank=True, null=True)
    payment_email = models.CharField(max_length=255, blank=True, null=True)
    payment_address_1 = models.CharField(max_length=128, blank=True, null=True)
    payment_address_2 = models.CharField(max_length=128, blank=True, null=True)
    payment_city = models.CharField(max_length=128, blank=True, null=True)
    payment_postcode = models.CharField(max_length=10, blank=True, null=True)
    payment_country = models.CharField(max_length=128, blank=True, null=True)
    payment_country_id = models.IntegerField(blank=True, null=True)
    payment_zone = models.CharField(max_length=128, blank=True, null=True)
    payment_zone_id = models.IntegerField(blank=True, null=True)
    payment_address_format = models.TextField(blank=True, null=True)
    payment_custom_field = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=128, blank=True, null=True)
    payment_code = models.CharField(max_length=128, blank=True, null=True)
    shipping_company = models.CharField(max_length=255, blank=True, null=True)
    shipping_firstname = models.CharField(max_length=32, blank=True, null=True)
    shipping_lastname = models.CharField(max_length=32, blank=True, null=True)
    shipping_telephone = models.CharField(max_length=32, blank=True, null=True)
    shipping_email = models.CharField(max_length=255, blank=True, null=True)
    shipping_address_1 = models.CharField(max_length=128, blank=True, null=True)
    shipping_address_2 = models.CharField(max_length=128, blank=True, null=True)
    shipping_city = models.CharField(max_length=128, blank=True, null=True)
    shipping_postcode = models.CharField(max_length=10, blank=True, null=True)
    shipping_country = models.CharField(max_length=128, blank=True, null=True)
    shipping_country_id = models.IntegerField(blank=True, null=True)
    shipping_zone = models.CharField(max_length=128, blank=True, null=True)
    shipping_zone_id = models.IntegerField(blank=True, null=True)
    shipping_address_format = models.TextField(blank=True, null=True)
    shipping_custom_field = models.TextField(blank=True, null=True)
    shipping_method = models.CharField(max_length=128, blank=True, null=True)
    shipping_code = models.CharField(max_length=128, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    order_status = models.ForeignKey(SsanOrderStatus, models.DO_NOTHING)
    payment_status = models.ForeignKey(SsanPaymentStatus, models.DO_NOTHING)
    affiliate_id = models.IntegerField()
    commission = models.DecimalField(max_digits=15, decimal_places=4)
    marketing_id = models.IntegerField()
    tracking = models.CharField(max_length=64, blank=True, null=True)
    shipped_by_company = models.CharField(max_length=255, blank=True, null=True)
    language_id = models.IntegerField()
    currency_id = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    currency_value = models.DecimalField(max_digits=15, decimal_places=8)
    ip = models.CharField(max_length=40)
    forwarded_ip = models.CharField(max_length=40)
    user_agent = models.CharField(max_length=255)
    accept_language = models.CharField(max_length=255)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    date_printed = models.DateTimeField(blank=True, null=True)
    date_shipped = models.DateTimeField(blank=True, null=True)
    date_paid = models.DateTimeField(blank=True, null=True)
    payment_due_date = models.DateTimeField(blank=True, null=True)
    printed_status = models.IntegerField(blank=True, null=True)
    printed_user = models.IntegerField(blank=True, null=True)
    payment_transaction_ref = models.CharField(max_length=100, blank=True, null=True)
    flag_id = models.IntegerField(blank=True, null=True)
    xero_invoiceid = models.CharField(max_length=512, blank=True, null=True)
    direct_website_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_order'

    objects = OcOrderManager()

class OcOrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OcOrder, models.DO_NOTHING, related_name='order_products')
    product = models.ForeignKey(prods.OcProduct, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    reward = models.IntegerField()
    size_id = models.IntegerField()
    size_name = models.CharField(max_length=255)
    material_id = models.IntegerField()
    material_name = models.CharField(max_length=255)
    product_variant = models.ForeignKey(prods.SsanProductVariants, models.DO_NOTHING)
    is_bespoke = models.IntegerField()
    status = models.ForeignKey(SsanOrderProductStatus, models.DO_NOTHING)
    bespoke_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_order_product'

class OcOrderTotal(models.Model):
    order_total_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OcOrder, models.DO_NOTHING)
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=15, decimal_places=4)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_order_total'


class SsanTempShipping(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    thumb = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    tracking_url = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_temp_shipping'

