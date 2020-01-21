# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OcAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    company = models.CharField(max_length=40, blank=True, null=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    custom_field = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_address'


class OcAffiliate(models.Model):
    affiliate_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    company = models.CharField(max_length=40)
    website = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    postcode = models.CharField(max_length=10)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    code = models.CharField(max_length=64)
    commission = models.DecimalField(max_digits=4, decimal_places=2)
    tax = models.CharField(max_length=64)
    payment = models.CharField(max_length=6)
    cheque = models.CharField(max_length=100)
    paypal = models.CharField(max_length=64)
    bank_name = models.CharField(max_length=64)
    bank_branch_number = models.CharField(max_length=64)
    bank_swift_code = models.CharField(max_length=64)
    bank_account_name = models.CharField(max_length=64)
    bank_account_number = models.CharField(max_length=64)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    approved = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate'


class OcAffiliateActivity(models.Model):
    affiliate_activity_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_activity'


class OcAffiliateLogin(models.Model):
    affiliate_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_login'


class OcAffiliateTransaction(models.Model):
    affiliate_transaction_id = models.AutoField(primary_key=True)
    affiliate_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_affiliate_transaction'


class OcApi(models.Model):
    api_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    key = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api'


class OcApiIp(models.Model):
    api_ip_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'oc_api_ip'


class OcApiSession(models.Model):
    api_session_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    token = models.CharField(max_length=32)
    session_id = models.CharField(max_length=32)
    session_name = models.CharField(max_length=32)
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_api_session'


class OcAttribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    attribute_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute'


class OcAttributeDescription(models.Model):
    attribute_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_description'
        unique_together = (('attribute_id', 'language_id'),)


class OcAttributeGroup(models.Model):
    attribute_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_attribute_group'


class OcAttributeGroupDescription(models.Model):
    attribute_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_attribute_group_description'
        unique_together = (('attribute_group_id', 'language_id'),)


class OcBanner(models.Model):
    banner_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner'


class OcBannerImage(models.Model):
    banner_image_id = models.AutoField(primary_key=True)
    banner_id = models.IntegerField()
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    link = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_banner_image'


class OcCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    api_id = models.IntegerField()
    customer_id = models.IntegerField()
    session_id = models.CharField(max_length=32)
    product_id = models.IntegerField()
    recurring_id = models.IntegerField()
    product_variant_id = models.IntegerField()
    option = models.TextField()
    ssan_options = models.TextField()
    quantity = models.IntegerField()
    date_added = models.DateTimeField()
    is_bespoke = models.IntegerField()
    svg_raw = models.TextField(blank=True, null=True)
    svg_json = models.TextField(blank=True, null=True)
    svg_export = models.TextField(blank=True, null=True)
    svg_bespoke_images = models.CharField(max_length=255, blank=True, null=True)
    svg_bespoke_texts = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_cart'


class OcCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    top = models.IntegerField()
    column = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()
    homepage_status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_category'


class OcCategoryDescription(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)
    clean_url_overide = models.CharField(max_length=255, blank=True, null=True)
    adwords_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oc_category_description'
        unique_together = (('category_id', 'language_id'),)


class OcCategoryDescriptionCopy(models.Model):
    category_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_category_description_copy'
        unique_together = (('category_id', 'language_id'),)


class OcCategoryFilter(models.Model):
    category_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_filter'
        unique_together = (('category_id', 'filter_id'),)


class OcCategoryPath(models.Model):
    category_id = models.IntegerField(primary_key=True)
    path_id = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_path'
        unique_together = (('category_id', 'path_id'),)


class OcCategoryToLayout(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_layout'
        unique_together = (('category_id', 'store_id'),)


class OcCategoryToStore(models.Model):
    category_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_category_to_store'
        unique_together = (('category_id', 'store_id'),)


class OcCountry(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)
    address_format = models.TextField()
    postcode_required = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_country'


class OcCouponCategory(models.Model):
    coupon_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_category'
        unique_together = (('coupon_id', 'category_id'),)


class OcCouponHistory(models.Model):
    coupon_history_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_history'


class OcCouponProduct(models.Model):
    coupon_product_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_coupon_product'


class OcCurrency(models.Model):
    currency_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=3)
    symbol_left = models.CharField(max_length=12)
    symbol_right = models.CharField(max_length=12)
    decimal_place = models.CharField(max_length=1)
    value = models.FloatField()
    status = models.IntegerField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_currency'


class OcCustomField(models.Model):
    custom_field_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    value = models.TextField()
    validation = models.CharField(max_length=255)
    location = models.CharField(max_length=7)
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field'


class OcCustomFieldCustomerGroup(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_customer_group'
        unique_together = (('custom_field_id', 'customer_group_id'),)


class OcCustomFieldDescription(models.Model):
    custom_field_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_description'
        unique_together = (('custom_field_id', 'language_id'),)


class OcCustomFieldValue(models.Model):
    custom_field_value_id = models.AutoField(primary_key=True)
    custom_field_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value'


class OcCustomFieldValueDescription(models.Model):
    custom_field_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_custom_field_value_description'
        unique_together = (('custom_field_value_id', 'language_id'),)


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


class OcCustomerActivity(models.Model):
    customer_activity_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    key = models.CharField(max_length=64)
    data = models.TextField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_activity'


class OcCustomerGroup(models.Model):
    customer_group_id = models.AutoField(primary_key=True)
    approval = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group'


class OcCustomerGroupDescription(models.Model):
    customer_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_customer_group_description'
        unique_together = (('customer_group_id', 'language_id'),)


class OcCustomerHistory(models.Model):
    customer_history_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_history'


class OcCustomerIp(models.Model):
    customer_ip_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_ip'


class OcCustomerLogin(models.Model):
    customer_login_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=96)
    ip = models.CharField(max_length=40)
    total = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_login'


class OcCustomerOnline(models.Model):
    ip = models.CharField(primary_key=True, max_length=40)
    customer_id = models.IntegerField()
    url = models.TextField()
    referer = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_online'


class OcCustomerReward(models.Model):
    customer_reward_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    points = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_reward'


class OcCustomerSearch(models.Model):
    customer_search_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    customer_id = models.IntegerField()
    keyword = models.CharField(max_length=255)
    category_id = models.IntegerField(blank=True, null=True)
    sub_category = models.IntegerField()
    description = models.IntegerField()
    products = models.IntegerField()
    ip = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_search'


class OcCustomerTransaction(models.Model):
    customer_transaction_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_transaction'


class OcCustomerWishlist(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_customer_wishlist'
        unique_together = (('customer_id', 'product_id'),)


class OcDownload(models.Model):
    download_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=160)
    mask = models.CharField(max_length=128)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_download'


class OcDownloadDescription(models.Model):
    download_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_download_description'
        unique_together = (('download_id', 'language_id'),)


class OcEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    trigger = models.TextField()
    action = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_event'


class OcExtension(models.Model):
    extension_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_extension'


class OcFilter(models.Model):
    filter_id = models.AutoField(primary_key=True)
    filter_group_id = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter'


class OcFilterDescription(models.Model):
    filter_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    filter_group_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_description'
        unique_together = (('filter_id', 'language_id'),)


class OcFilterGroup(models.Model):
    filter_group_id = models.AutoField(primary_key=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_filter_group'


class OcFilterGroupDescription(models.Model):
    filter_group_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_filter_group_description'
        unique_together = (('filter_group_id', 'language_id'),)


class OcGeoZone(models.Model):
    geo_zone_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_modified = models.DateTimeField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_geo_zone'


class OcGoogleBaseCategory(models.Model):
    google_base_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_google_base_category'


class OcGoogleBaseCategoryToCategory(models.Model):
    google_base_category_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_google_base_category_to_category'
        unique_together = (('google_base_category_id', 'category_id'),)


class OcInformation(models.Model):
    information_id = models.AutoField(primary_key=True)
    bottom = models.IntegerField()
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information'


class OcInformationDescription(models.Model):
    information_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=64)
    description = models.TextField()
    meta_title = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    meta_keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_information_description'
        unique_together = (('information_id', 'language_id'),)


class OcInformationToLayout(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_layout'
        unique_together = (('information_id', 'store_id'),)


class OcInformationToStore(models.Model):
    information_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_information_to_store'
        unique_together = (('information_id', 'store_id'),)


class OcLanguage(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=5)
    locale = models.CharField(max_length=255)
    image = models.CharField(max_length=64)
    directory = models.CharField(max_length=32)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_language'


class OcLayout(models.Model):
    layout_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout'


class OcLayoutModule(models.Model):
    layout_module_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    code = models.CharField(max_length=64)
    position = models.CharField(max_length=14)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_layout_module'


class OcLayoutRoute(models.Model):
    layout_route_id = models.AutoField(primary_key=True)
    layout_id = models.IntegerField()
    store_id = models.IntegerField()
    route = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_layout_route'


class OcLengthClass(models.Model):
    length_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'oc_length_class'


class OcLengthClassDescription(models.Model):
    length_class_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_length_class_description'
        unique_together = (('length_class_id', 'language_id'),)


class OcLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    address = models.TextField()
    telephone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    geocode = models.CharField(max_length=32)
    image = models.CharField(max_length=255, blank=True, null=True)
    open = models.TextField()
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_location'


class OcManufacturer(models.Model):
    manufacturer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer'


class OcManufacturerToStore(models.Model):
    manufacturer_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_manufacturer_to_store'
        unique_together = (('manufacturer_id', 'store_id'),)


class OcMarketing(models.Model):
    marketing_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=64)
    clicks = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_marketing'


class OcMenu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    type = models.CharField(max_length=6)
    link = models.CharField(max_length=255)
    sort_order = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_menu'


class OcMenuDescription(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_menu_description'
        unique_together = (('menu_id', 'language_id'),)


class OcMenuModule(models.Model):
    menu_module_id = models.IntegerField(primary_key=True)
    menu_id = models.IntegerField()
    code = models.CharField(max_length=64)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_menu_module'


class OcModification(models.Model):
    modification_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    version = models.CharField(max_length=32)
    link = models.CharField(max_length=255)
    xml = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_modification'


class OcModule(models.Model):
    module_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=32)
    setting = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_module'


class OcOpenbayFaq(models.Model):
    route = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_openbay_faq'


class OcOption(models.Model):
    option_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=32)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option'


class OcOptionDescription(models.Model):
    option_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_description'
        unique_together = (('option_id', 'language_id'),)


class OcOptionValue(models.Model):
    option_value_id = models.AutoField(primary_key=True)
    option_id = models.IntegerField()
    image = models.CharField(max_length=255)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_option_value'


class OcOptionValueDescription(models.Model):
    option_value_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    option_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_option_value_description'
        unique_together = (('option_value_id', 'language_id'),)


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
    order_status = models.ForeignKey('SsanOrderStatus', models.DO_NOTHING)
    payment_status = models.ForeignKey('SsanPaymentStatus', models.DO_NOTHING)
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


class OcOrderCustomField(models.Model):
    order_custom_field_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    custom_field_id = models.IntegerField()
    custom_field_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)
    location = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'oc_order_custom_field'


class OcOrderHistory(models.Model):
    order_history_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_history'


class OcOrderOption(models.Model):
    order_option_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_product_id = models.IntegerField()
    product_option_id = models.IntegerField()
    product_option_value_id = models.IntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()
    type = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_option'


class OcOrderProduct(models.Model):
    order_product_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OcOrder, models.DO_NOTHING)
    product = models.ForeignKey('OcProduct', models.DO_NOTHING)
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
    product_variant = models.ForeignKey('SsanProductVariants', models.DO_NOTHING)
    is_bespoke = models.IntegerField()
    status = models.ForeignKey('SsanOrderProductStatus', models.DO_NOTHING)
    bespoke_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_order_product'


class OcOrderRecurring(models.Model):
    order_recurring_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    product_quantity = models.IntegerField()
    recurring_id = models.IntegerField()
    recurring_name = models.CharField(max_length=255)
    recurring_description = models.CharField(max_length=255)
    recurring_frequency = models.CharField(max_length=25)
    recurring_cycle = models.SmallIntegerField()
    recurring_duration = models.SmallIntegerField()
    recurring_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial = models.IntegerField()
    trial_frequency = models.CharField(max_length=25)
    trial_cycle = models.SmallIntegerField()
    trial_duration = models.SmallIntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring'


class OcOrderRecurringTransaction(models.Model):
    order_recurring_transaction_id = models.AutoField(primary_key=True)
    order_recurring_id = models.IntegerField()
    reference = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_order_recurring_transaction'


class OcOrderStatus(models.Model):
    order_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_order_status'
        unique_together = (('order_status_id', 'language_id'),)


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


class OcOrderVoucher(models.Model):
    order_voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    voucher_id = models.IntegerField()
    description = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'oc_order_voucher'


class OcPaypalIframeOrder(models.Model):
    paypal_iframe_order_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    capture_status = models.CharField(max_length=11, blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    authorization_id = models.CharField(max_length=30)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_paypal_iframe_order'


class OcPaypalIframeOrderTransaction(models.Model):
    paypal_iframe_order_transaction_id = models.AutoField(primary_key=True)
    paypal_iframe_order_id = models.IntegerField()
    transaction_id = models.CharField(max_length=20)
    parent_id = models.CharField(max_length=20)
    date_added = models.DateTimeField()
    note = models.CharField(max_length=255)
    msgsubid = models.CharField(max_length=38)
    receipt_id = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=7, blank=True, null=True)
    payment_status = models.CharField(max_length=20)
    pending_reason = models.CharField(max_length=50)
    transaction_entity = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debug_data = models.TextField()
    call_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_paypal_iframe_order_transaction'


class OcPaypalOrder(models.Model):
    paypal_order_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    capture_status = models.CharField(max_length=11, blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    authorization_id = models.CharField(max_length=30)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_paypal_order'


class OcPaypalOrderTransaction(models.Model):
    paypal_order_transaction_id = models.AutoField(primary_key=True)
    paypal_order_id = models.IntegerField()
    transaction_id = models.CharField(max_length=20)
    parent_id = models.CharField(max_length=20)
    date_added = models.DateTimeField()
    note = models.CharField(max_length=255)
    msgsubid = models.CharField(max_length=38)
    receipt_id = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=7, blank=True, null=True)
    payment_status = models.CharField(max_length=20)
    pending_reason = models.CharField(max_length=50)
    transaction_entity = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debug_data = models.TextField()
    call_data = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_paypal_order_transaction'


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


class OcProductAttribute(models.Model):
    product_id = models.IntegerField(primary_key=True)
    attribute_id = models.IntegerField()
    language_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_product_attribute'
        unique_together = (('product_id', 'attribute_id', 'language_id'),)


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


class OcProductFilter(models.Model):
    product_id = models.IntegerField(primary_key=True)
    filter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_filter'
        unique_together = (('product_id', 'filter_id'),)


class OcProductImage(models.Model):
    product_image_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_image'


class OcProductOption(models.Model):
    product_option_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    value = models.TextField()
    required = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_option'


class OcProductOptionValue(models.Model):
    product_option_value_id = models.AutoField(primary_key=True)
    product_option_id = models.IntegerField()
    product_id = models.IntegerField()
    option_id = models.IntegerField()
    option_value_id = models.IntegerField()
    quantity = models.IntegerField()
    subtract = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=4)
    price_prefix = models.CharField(max_length=1)
    points = models.IntegerField()
    points_prefix = models.CharField(max_length=1)
    weight = models.DecimalField(max_digits=15, decimal_places=8)
    weight_prefix = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'oc_product_option_value'


class OcProductRecurring(models.Model):
    product_id = models.IntegerField(primary_key=True)
    recurring_id = models.IntegerField()
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_recurring'
        unique_together = (('product_id', 'recurring_id', 'customer_group_id'),)


class OcProductRelated(models.Model):
    product_id = models.IntegerField(primary_key=True)
    related_id = models.IntegerField()
    show_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_related'
        unique_together = (('product_id', 'related_id'),)


class OcProductReward(models.Model):
    product_reward_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_group_id = models.IntegerField()
    points = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_reward'


class OcProductToCategory(models.Model):
    product_id = models.IntegerField(primary_key=True)
    category_id = models.IntegerField()
    cat_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_category'
        unique_together = (('product_id', 'category_id'),)


class OcProductToDownload(models.Model):
    product_id = models.IntegerField(primary_key=True)
    download_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_download'
        unique_together = (('product_id', 'download_id'),)


class OcProductToLayout(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()
    layout_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_layout'
        unique_together = (('product_id', 'store_id'),)


class OcProductToStore(models.Model):
    product_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_product_to_store'
        unique_together = (('product_id', 'store_id'),)


class OcRecurring(models.Model):
    recurring_id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    frequency = models.CharField(max_length=10)
    duration = models.PositiveIntegerField()
    cycle = models.PositiveIntegerField()
    trial_status = models.IntegerField()
    trial_price = models.DecimalField(max_digits=10, decimal_places=4)
    trial_frequency = models.CharField(max_length=10)
    trial_duration = models.PositiveIntegerField()
    trial_cycle = models.PositiveIntegerField()
    status = models.IntegerField()
    sort_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_recurring'


class OcRecurringDescription(models.Model):
    recurring_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_recurring_description'
        unique_together = (('recurring_id', 'language_id'),)


class OcReturnAction(models.Model):
    return_action_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'oc_return_action'
        unique_together = (('return_action_id', 'language_id'),)


class OcReturnHistory(models.Model):
    return_history_id = models.AutoField(primary_key=True)
    return_id = models.IntegerField()
    return_status_id = models.IntegerField()
    notify = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_return_history'


class OcReturnReason(models.Model):
    return_reason_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'oc_return_reason'
        unique_together = (('return_reason_id', 'language_id'),)


class OcReturnStatus(models.Model):
    return_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_return_status'
        unique_together = (('return_status_id', 'language_id'),)


class OcReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    author = models.CharField(max_length=64)
    text = models.TextField()
    rating = models.IntegerField()
    status = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_review'


class OcSagepayServerCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    token = models.CharField(max_length=50)
    digits = models.CharField(max_length=4)
    expiry = models.CharField(max_length=5)
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'oc_sagepay_server_card'


class OcSagepayServerOrder(models.Model):
    sagepay_server_order_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    vpstxid = models.CharField(db_column='VPSTxId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendortxcode = models.CharField(db_column='VendorTxCode', max_length=50)  # Field name made lowercase.
    securitykey = models.CharField(db_column='SecurityKey', max_length=50)  # Field name made lowercase.
    txauthno = models.IntegerField(db_column='TxAuthNo', blank=True, null=True)  # Field name made lowercase.
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    release_status = models.IntegerField(blank=True, null=True)
    void_status = models.IntegerField(blank=True, null=True)
    settle_type = models.IntegerField(blank=True, null=True)
    rebate_status = models.IntegerField(blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_sagepay_server_order'


class OcSagepayServerOrderRecurring(models.Model):
    sagepay_server_order_recurring_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_recurring_id = models.IntegerField()
    vpstxid = models.CharField(db_column='VPSTxId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendortxcode = models.CharField(db_column='VendorTxCode', max_length=50)  # Field name made lowercase.
    securitykey = models.CharField(db_column='SecurityKey', max_length=50)  # Field name made lowercase.
    txauthno = models.IntegerField(db_column='TxAuthNo', blank=True, null=True)  # Field name made lowercase.
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    next_payment = models.DateTimeField()
    trial_end = models.DateTimeField(blank=True, null=True)
    subscription_end = models.DateTimeField(blank=True, null=True)
    currency_code = models.CharField(max_length=3)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_sagepay_server_order_recurring'


class OcSagepayServerOrderTransaction(models.Model):
    sagepay_server_order_transaction_id = models.AutoField(primary_key=True)
    sagepay_server_order_id = models.IntegerField()
    date_added = models.DateTimeField()
    type = models.CharField(max_length=7, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'oc_sagepay_server_order_transaction'


class OcSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    code = models.CharField(max_length=32)
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_setting'


class OcSettingCopy1(models.Model):
    setting_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    code = models.CharField(max_length=32)
    key = models.CharField(max_length=64)
    value = models.TextField()
    serialized = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_setting_copy1'


class OcStockStatus(models.Model):
    stock_status_id = models.AutoField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_stock_status'
        unique_together = (('stock_status_id', 'language_id'),)


class OcStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    ssl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_store'


class OcTaxClass(models.Model):
    tax_class_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_class'


class OcTaxRate(models.Model):
    tax_rate_id = models.AutoField(primary_key=True)
    geo_zone_id = models.IntegerField()
    name = models.CharField(max_length=32)
    rate = models.DecimalField(max_digits=15, decimal_places=4)
    type = models.CharField(max_length=1)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate'


class OcTaxRateToCustomerGroup(models.Model):
    tax_rate_id = models.IntegerField(primary_key=True)
    customer_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rate_to_customer_group'
        unique_together = (('tax_rate_id', 'customer_group_id'),)


class OcTaxRule(models.Model):
    tax_rule_id = models.AutoField(primary_key=True)
    tax_class_id = models.IntegerField()
    tax_rate_id = models.IntegerField()
    based = models.CharField(max_length=10)
    priority = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_tax_rule'


class OcTheme(models.Model):
    theme_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    theme = models.CharField(max_length=64)
    route = models.CharField(max_length=64)
    code = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_theme'


class OcTranslation(models.Model):
    translation_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    language_id = models.IntegerField()
    route = models.CharField(max_length=64)
    key = models.CharField(max_length=64)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_translation'


class OcUpload(models.Model):
    upload_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_upload'


class OcUrlAlias(models.Model):
    url_alias_id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_url_alias'


class OcUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_group_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=9)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    image = models.CharField(max_length=255)
    code = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_user'


class OcUserGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    permission = models.TextField()

    class Meta:
        managed = False
        db_table = 'oc_user_group'


class OcVoucher(models.Model):
    voucher_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    code = models.CharField(max_length=10)
    from_name = models.CharField(max_length=64)
    from_email = models.CharField(max_length=96)
    to_name = models.CharField(max_length=64)
    to_email = models.CharField(max_length=96)
    voucher_theme_id = models.IntegerField()
    message = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    status = models.IntegerField()
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher'


class OcVoucherHistory(models.Model):
    voucher_history_id = models.AutoField(primary_key=True)
    voucher_id = models.IntegerField()
    order_id = models.IntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_voucher_history'


class OcVoucherTheme(models.Model):
    voucher_theme_id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme'


class OcVoucherThemeDescription(models.Model):
    voucher_theme_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'oc_voucher_theme_description'
        unique_together = (('voucher_theme_id', 'language_id'),)


class OcWeightClass(models.Model):
    weight_class_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=15, decimal_places=8)

    class Meta:
        managed = False
        db_table = 'oc_weight_class'


class OcWeightClassDescription(models.Model):
    weight_class_id = models.IntegerField(primary_key=True)
    language_id = models.IntegerField()
    title = models.CharField(max_length=32)
    unit = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'oc_weight_class_description'
        unique_together = (('weight_class_id', 'language_id'),)


class OcZone(models.Model):
    zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=32)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'oc_zone'


class OcZoneToGeoZone(models.Model):
    zone_to_geo_zone_id = models.AutoField(primary_key=True)
    country_id = models.IntegerField()
    zone_id = models.IntegerField()
    geo_zone_id = models.IntegerField()
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'oc_zone_to_geo_zone'


class OldSsanBuilkdiscountBreaks(models.Model):
    qty_range_min = models.IntegerField()
    discount_percent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_ssan_builkdiscount_breaks'


class OldSsanBulkdiscountGroupValues(models.Model):
    bulk_discount_group_id = models.IntegerField(primary_key=True)
    discount_break_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'old_ssan_bulkdiscount_group_values'
        unique_together = (('bulk_discount_group_id', 'discount_break_id'),)


class ProductVariants(models.Model):
    prod_var_id = models.AutoField(primary_key=True)
    productid = models.IntegerField(blank=True, null=True)
    sizeid = models.IntegerField(blank=True, null=True)
    materialid = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    list_price = models.FloatField(blank=True, null=True)
    sale_price = models.FloatField(blank=True, null=True)
    suppleir_id = models.IntegerField(blank=True, null=True)
    supplier_code = models.CharField(max_length=255, blank=True, null=True)
    supplier_price = models.FloatField(blank=True, null=True)
    price_code = models.CharField(max_length=255, blank=True, null=True)
    website_id = models.IntegerField()
    ih_price = models.FloatField(blank=True, null=True)
    digital_artwork = models.IntegerField(blank=True, null=True)
    digital_artwork_price = models.FloatField(blank=True, null=True)
    exclude_free_pnp = models.IntegerField(blank=True, null=True)
    digital_artwork_def = models.IntegerField(blank=True, null=True)
    old_list_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_variants'


class SsanBespokeImage(models.Model):
    size_material_id = models.IntegerField(blank=True, null=True)
    bespoke_cat_type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    svg_json = models.TextField(blank=True, null=True)
    svg_raw = models.TextField(blank=True, null=True)
    png_url = models.CharField(max_length=255, blank=True, null=True)
    sign_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_bespoke_image'


class SsanBespokeImageInfo(models.Model):
    bespokeid = models.IntegerField(db_column='bespokeID')  # Field name made lowercase.
    text_line = models.CharField(max_length=1024, blank=True, null=True)
    image_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_bespoke_image_info'
        unique_together = (('id', 'bespokeid'),)


class SsanBespokeImageSymbols(models.Model):
    bespoke_id = models.IntegerField(primary_key=True)
    symbol_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_bespoke_image_symbols'
        unique_together = (('bespoke_id', 'symbol_id'),)


class SsanBespokeTemplate(models.Model):
    template_path = models.CharField(max_length=255)
    template_desc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssan_bespoke_template'


class SsanBuilkdiscountGroupBreaks(models.Model):
    bulk_discount_group_id = models.IntegerField()
    qty_range_min = models.IntegerField()
    discount_percent = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_builkdiscount_group_breaks'


class SsanBulkdiscountGroups(models.Model):
    group_name = models.CharField(max_length=255)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_bulkdiscount_groups'


class SsanContacts(models.Model):
    firstname = models.CharField(max_length=31, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_contacts'


class SsanFlags(models.Model):
    flag_name = models.CharField(max_length=20, blank=True, null=True)
    flag_tooltip = models.CharField(max_length=255, blank=True, null=True)
    flag_image_blob = models.TextField(blank=True, null=True)
    flag_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_flags'


class SsanOptionClass(models.Model):
    label = models.CharField(max_length=30)
    descr = models.CharField(max_length=100)
    image = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100)
    store_id = models.IntegerField()
    dropdown_title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ssan_option_class'


class SsanOptionClassValues(models.Model):
    option_class_id = models.IntegerField(primary_key=True)
    option_value_id = models.IntegerField()
    order_by = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_option_class_values'
        unique_together = (('option_class_id', 'option_value_id', 'store_id'),)


class SsanOptionTypes(models.Model):
    name = models.CharField(max_length=20)
    descr = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssan_option_types'


class SsanOptionValues(models.Model):
    value_name = models.CharField(max_length=50)
    descr = models.CharField(max_length=100)
    internal_descr = models.CharField(max_length=100)
    type = models.IntegerField()
    productid = models.IntegerField(blank=True, null=True)
    product_variants = models.CharField(max_length=1024)
    extra_option_classid = models.IntegerField(blank=True, null=True)
    price_modifier = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ssan_option_values'


class SsanOrderAlertImages(models.Model):
    alert_imd_id = models.AutoField(primary_key=True)
    alert_img_text = models.CharField(max_length=32, blank=True, null=True)
    alert_img_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_order_alert_images'


class SsanOrderBespokeImage(models.Model):
    order_product_id = models.IntegerField()
    product_var_id = models.IntegerField(blank=True, null=True)
    bespoke_cat_type = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    svg_json = models.TextField(blank=True, null=True)
    svg_export = models.TextField(blank=True, null=True)
    png_url = models.CharField(max_length=255, blank=True, null=True)
    sign_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_order_bespoke_image'


class SsanOrderProductArtworkStatus(models.Model):
    status_title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ssan_order_product_artwork_status'


class SsanOrderProductArtworkStatusHistory(models.Model):
    product_order_id = models.IntegerField(blank=True, null=True)
    product_order_artwork_status_id = models.IntegerField()
    date_status_set = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_order_product_artwork_status_history'


class SsanOrderProductStatus(models.Model):
    status_title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ssan_order_product_status'


class SsanOrderProductStatusHistory(models.Model):
    order_product_id = models.IntegerField(blank=True, null=True)
    order_product_status_id = models.IntegerField()
    date_status_set = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_order_product_status_history'


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


class SsanProductSymbols(models.Model):
    product = models.ForeignKey(OcProduct, models.DO_NOTHING, primary_key=True)
    symbol = models.ForeignKey('SsanSymbols', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ssan_product_symbols'
        unique_together = (('product', 'symbol'),)


class SsanProductTags(models.Model):
    id = models.IntegerField(primary_key=True)
    product_id = models.IntegerField()
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_product_tags'


class SsanProductToBulkDiscounts(models.Model):
    product_id = models.IntegerField(primary_key=True)
    bulk_discount_group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_product_to_bulk_discounts'
        unique_together = (('product_id', 'bulk_discount_group_id'),)


class SsanProductVariantOptions(models.Model):
    prod_var_id = models.IntegerField(primary_key=True)
    option_class_id = models.IntegerField()
    order_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_product_variant_options'
        unique_together = (('prod_var_id', 'option_class_id'),)


class SsanProductVariants(models.Model):
    product_id = models.IntegerField(blank=True, null=True)
    size_material = models.ForeignKey('SsanSizeMaterialComb', models.DO_NOTHING)
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


class SsanPurchaseOrder(models.Model):
    po_id = models.AutoField(primary_key=True)
    po_ref = models.CharField(max_length=50, blank=True, null=True)
    supplier_id = models.IntegerField()
    company = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=32, blank=True, null=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=96, blank=True, null=True)
    telephone = models.CharField(max_length=32, blank=True, null=True)
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
    shipping_custom_field = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    po_status_id = models.IntegerField()
    payment_status_id = models.IntegerField()
    tracking = models.CharField(max_length=64, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    date_shipped = models.DateTimeField(blank=True, null=True)
    date_paid = models.DateTimeField(blank=True, null=True)
    payment_due_date = models.DateTimeField(blank=True, null=True)
    flag_id = models.IntegerField(blank=True, null=True)
    xero_poid = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_purchase_order'


class SsanPurchaseOrderProduct(models.Model):
    order_product_id = models.IntegerField(primary_key=True)
    po_id = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=4)
    total = models.DecimalField(max_digits=15, decimal_places=4)
    tax = models.DecimalField(max_digits=15, decimal_places=4)
    product_variant_id = models.IntegerField()
    is_bespoke = models.IntegerField(blank=True, null=True)
    status_id = models.IntegerField(blank=True, null=True)
    bespoke_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_purchase_order_product'


class SsanQuickNote(models.Model):
    order_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    lead_id = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    date_take_action = models.DateField(blank=True, null=True)
    note_text = models.TextField(blank=True, null=True)
    notes_owner = models.IntegerField(blank=True, null=True)
    notes_email = models.CharField(max_length=255, blank=True, null=True)
    notes_contact = models.CharField(max_length=64, blank=True, null=True)
    notes_telephone = models.CharField(max_length=20, blank=True, null=True)
    notes_complete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_quick_note'


class SsanQuote(models.Model):
    quote_ref = models.CharField(max_length=11, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    lead_id = models.IntegerField(blank=True, null=True)
    quote_date = models.DateField()
    contact_name = models.CharField(max_length=127, blank=True, null=True)
    company_name = models.CharField(max_length=127, blank=True, null=True)
    quote_email = models.CharField(max_length=255, blank=True, null=True)
    quote_telephone = models.CharField(max_length=32, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    website_id = models.IntegerField()
    quote_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_quote'


class SsanQuoteLine(models.Model):
    line_id = models.AutoField(primary_key=True)
    quote_id = models.IntegerField()
    product_variant_id = models.IntegerField(blank=True, null=True)
    product_description = models.CharField(max_length=100, blank=True, null=True)
    product_code = models.CharField(max_length=30, blank=True, null=True)
    product_size = models.CharField(max_length=100, blank=True, null=True)
    product_size_id = models.IntegerField(blank=True, null=True)
    product_material = models.CharField(max_length=100, blank=True, null=True)
    product_material_id = models.IntegerField(blank=True, null=True)
    product_extra = models.CharField(max_length=1024, blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_qty = models.IntegerField()
    product_line_total = models.DecimalField(max_digits=10, decimal_places=2)
    product_tax = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ssan_quote_line'
        unique_together = (('line_id', 'quote_id'),)


class SsanQuoteStatus(models.Model):
    quote_status_text = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'ssan_quote_status'


class SsanRelatedSymbols(models.Model):
    symbol_id = models.IntegerField(primary_key=True)
    related_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_related_symbols'
        unique_together = (('symbol_id', 'related_id'),)


class SsanShipping(models.Model):
    shipping_name = models.CharField(max_length=255)
    shipping_api_url = models.CharField(max_length=255)
    shipping_brand_image = models.CharField(max_length=255)
    shipping_tracking_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssan_shipping'


class SsanSizeMaterialComb(models.Model):
    product_size = models.ForeignKey(SsanProductSizes, models.DO_NOTHING)
    product_material = models.ForeignKey(SsanProductMaterial, models.DO_NOTHING)
    size_material_comb_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ssan_size_material_comb'
        unique_together = (('id', 'product_size', 'product_material'),)


class SsanSupplier(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    address_city = models.CharField(max_length=50)
    address_postcode = models.CharField(max_length=10)
    main_contact = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    web_address = models.CharField(max_length=255, blank=True, null=True)
    account_no = models.CharField(max_length=20, blank=True, null=True)
    sort_code = models.CharField(max_length=20, blank=True, null=True)
    payment_type = models.IntegerField()
    payment_days = models.IntegerField()
    logo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_supplier'


class SsanSymbolCategory(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    default_colour_rgb = models.CharField(db_column='default_colour_RGB', max_length=20, blank=True, null=True)  # Field name made lowercase.
    default_colour_hex = models.CharField(db_column='default_colour_HEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    default_text_hex = models.CharField(db_column='default_text_HEX', max_length=10, blank=True, null=True)  # Field name made lowercase.
    default_colour = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_symbol_category'


class SsanSymbolStandards(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    target_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ssan_symbol_standards'


class SsanSymbols(models.Model):
    image_path = models.CharField(max_length=255, blank=True, null=True)
    refenceno = models.CharField(max_length=48, blank=True, null=True)
    referent = models.CharField(max_length=255, blank=True, null=True)
    function = models.CharField(max_length=1024, blank=True, null=True)
    content = models.CharField(max_length=1024, blank=True, null=True)
    hazard = models.CharField(max_length=1024, blank=True, null=True)
    humanbehav = models.CharField(max_length=1024, blank=True, null=True)
    svg_path = models.CharField(max_length=255, blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)
    standard = models.ForeignKey(SsanSymbolStandards, models.DO_NOTHING, blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image_height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ssan_symbols'


class SsanSymbolsToCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    symbol_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ssan_symbols_to_category'


class SsanTags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'ssan_tags'
