from django.db import models

# Create your models here.



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
    standard_id = models.IntegerField(blank=True, null=True)
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
