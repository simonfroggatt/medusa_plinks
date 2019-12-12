from django.db import models
from django.utils import timezone
import datetime as dt

# Create your models here.


class OcOrderQuerySet(models.QuerySet):
    def successful(self):
        valid_status = [2, 3, 4]
        return self.filter(payment_status_id__in=valid_status)

    def today(self):
        #today_data = timezone.datetime.today()
        today_data = '2019-06-17'
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




class OcOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    invoice_no = models.IntegerField()
    invoice_prefix = models.CharField(max_length=26, blank=True, null=True)
    purchase_order_ref = models.CharField(max_length=50, blank=True, null=True)
    store_id = models.IntegerField()
    store_name = models.CharField(max_length=64)
    store_url = models.CharField(max_length=255)
    customer_id = models.IntegerField()
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
    order_status_id = models.IntegerField()
    payment_status_id = models.IntegerField()
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


class OcProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=64)
    sku = models.CharField(max_length=64)
    upc = models.CharField(max_length=12)
    ean = models.CharField(max_length=14)
    jan = models.CharField(max_length=13)
    isbn = models.CharField(max_length=17)
    mpn = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    quantity = models.IntegerField()
    stock_status_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    manufacturer_id = models.IntegerField()
    shipping = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    points = models.IntegerField()
    tax_class_id = models.IntegerField()
    date_available = models.DateField()
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_class_id = models.IntegerField()
    length = models.DecimalField(max_digits=15, decimal_places=8)
    width = models.DecimalField(max_digits=15, decimal_places=8)
    height = models.DecimalField(max_digits=15, decimal_places=8)
    length_class_id = models.IntegerField()
    subtract = models.IntegerField()
    minimum = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    viewed = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    is_bespoke = models.IntegerField(blank=True, null=True)
    bespoke_category = models.IntegerField(blank=True, null=True)
    bespoke_template = models.IntegerField(blank=True, null=True)
    include_google_merchant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_product'

    # def __str__(self):
    #     return self.model

    def full_image_path(self):
        return 'images/' + self.image




class OcProductDescription(models.Model):
    product_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    tag = models.TextField(blank=True, null=True)
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    long_description = models.CharField(max_length=2048)

    class Meta:
        managed = False
        db_table = 'oc_product_description'
        unique_together = (('product_id', 'language_id'),)


class SsanSymbolStandards(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    target_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssan_symbol_standards'


class SsanSymbols(models.Model):
    id = models.IntegerField(primary_key=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    refenceno = models.CharField(max_length=48, blank=True, null=True)
    referent = models.CharField(max_length=255, blank=True, null=True)
    function = models.CharField(max_length=1024, blank=True, null=True)
    content = models.CharField(max_length=1024, blank=True, null=True)
    hazard = models.CharField(max_length=1024, blank=True, null=True)
    humanbehav = models.CharField(max_length=1024, blank=True, null=True)
    svg_path = models.CharField(max_length=255, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    standard_id = models.ForeignKey(SsanSymbolStandards, models.DO_NOTHING, blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_symbols'

    def full_symbol_path(self):
        return 'images/' + self.image_path

    def full_symbol_path_svg(self):
        return 'images/' + self.svg_path


class SsanProductSymbols(models.Model):
    product = models.ForeignKey(OcProduct, models.DO_NOTHING, primary_key=True)
    symbol = models.ForeignKey(SsanSymbols, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ssan_product_symbols'
        unique_together = (('product', 'symbol'),)


class SsanSymbolCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    default_colour_rgb = models.CharField(db_column='default_colour_RGB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    default_colour_hex = models.CharField(db_column='default_colour_HEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    default_text_hex = models.CharField(db_column='default_text_HEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    default_colour = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_symbol_category'


class SsanSymbolsToCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    symbol_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_symbols_to_category'
