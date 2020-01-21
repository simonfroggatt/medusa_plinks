from django.db import models
from django.utils import timezone
import datetime as dt

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


class SsanProductMaterial(models.Model):
    material_name = models.CharField(max_length=255)
    material_desc = models.CharField(max_length=255, blank=True, null=True)
    material_desc_full = models.CharField(max_length=255, blank=True, null=True)
    mounting_desc = models.CharField(max_length=255, blank=True, null=True)
    mounting_desc_full = models.CharField(max_length=255, blank=True, null=True)
    thickness_desc = models.CharField(max_length=255, blank=True, null=True)
    thickness_desc_full = models.CharField(max_length=255, blank=True, null=True)
    fixing_desc = models.CharField(max_length=255, blank=True, null=True)
    fixing_desc_full = models.CharField(max_length=255, blank=True, null=True)
    colour_desc = models.CharField(max_length=255, blank=True, null=True)
    colour_desc_full = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_product_material'


class SsanProductSizes(models.Model):
    size_name = models.CharField(max_length=50)
    size_width = models.IntegerField(blank=True, null=True)
    size_height = models.IntegerField(blank=True, null=True)
    size_units = models.CharField(max_length=50, blank=True, null=True)
    size_orientation = models.CharField(max_length=20, blank=True, null=True)
    size_extra = models.CharField(max_length=100, blank=True, null=True)
    size_template = models.IntegerField(blank=True, null=True)
    size_code = models.CharField(max_length=5)
    symbol_default_location = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_product_sizes'


class SsanSizeMaterialComb(models.Model):
    product_size = models.ForeignKey(SsanProductSizes, models.DO_NOTHING)
    product_material = models.ForeignKey(SsanProductMaterial, models.DO_NOTHING)
    size_material_comb_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ssan_size_material_comb'
        unique_together = (('id', 'product_size', 'product_material'),)

class SsanProductVariants(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    size_material = models.ForeignKey(SsanSizeMaterialComb, models.DO_NOTHING)
    variant_code = models.CharField(max_length=255, blank=True, null=True)
    variant_overide_price = models.DecimalField(max_digits=5, decimal_places=2)
    alternative_image = models.CharField(max_length=255, blank=True, null=True)
    exclude_fpnp = models.IntegerField()
    supplier_id = models.IntegerField(blank=True, null=True)
    supplier_code = models.CharField(max_length=255, blank=True, null=True)
    supplier_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock_amount = models.IntegerField(blank=True, null=True)
    stock_days = models.IntegerField(blank=True, null=True)
    gtin = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_product_variants'
