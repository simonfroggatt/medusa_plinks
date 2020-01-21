import json
from . import constants
from apps.xero_toolkit.xeromanager import XeroAuthManager

class XeroItem:
    def __init__(self):
        return


class XeroContact(XeroItem):

    __XERO_ENDPOINT = 'Contacts'
    __PAYMENT_TERMS = ['DAYSAFTERBILLDATE','DAYSAFTERBILLMONTH', 'OFCURRENTMONTH', 'OFFOLLOWINGMONTH']

    def __init__(self):
        #note we are using the same case as xero uses
        self.__ContactID = None
        self.__ContactNumber = None
        self.__AccountNumber = None
        self.__ContactStatus = None
        self.__Name = None
        self.__FirstName = None
        self.__LastName = None
        self.__EmailAddress = None
        self.__SkypeUserName = None
        self.__BankAccountDetails = None
        self.__TaxNumber = None
        self.__AccountsReceivableTaxType = None
        self.__AccountsPayableTaxType = None
        self.__Addresses = []
        self.__Phones = []
        self.__IsSupplier = None
        self.__IsCustomer = None
        self.__DefaultCurrency = "GBP"
        self.__ContactPersons = None
        self.__SalesDefaultAccountCode = None
        self.__PaymentTerms = None
        self.__Website = None
        self.__Balances = None
        return

    def load_contact(self, xero_contact_id):
        #given the contact id get the info from XERO
        return

    def create_contact(self, contact_data):
        if contact_data['company']:
            self.__Name = contact_data['company']
        else:
            self.__Name = contact_data['firstname'] + ' ' + contact_data['lastname']
        if contact_data['firstname']:
            self.__FirstName = contact_data['firstname']
        if contact_data['lastname']:
            self.__LastName = contact_data['lastname']
        if contact_data['email']:
            self.__EmailAddress = contact_data['email']

        return

    def add_address(self, address_book):
        for address_data in address_book:
            address_xero = {'AddressType':'POBOX', 'Country': 'GB'}
            if address_data['address_1']:
                address_xero['AddressLine1'] = address_data['address_1']
            if address_data['address_2']:
                address_xero['AddressLine2'] = address_data['address_2']
            if address_data['city']:
                address_xero['City'] = address_data['city']
            if address_data['postcode']:
                address_xero['PostalCode'] = address_data['postcode']
            if address_data['telephone']:
                self.add_telephone(address_data['telephone'])

        self.__Addresses.append(address_xero)

    def add_telephone(self, phonenumber):
        phone_xero = {'PhoneType': 'DEFAULT'}
        phone_xero['PhoneNumber'] = phonenumber
        self.__Phones.append(phone_xero)

    def save_contact(self, xero_auth_class):
        endpoint = 'Contacts'
        contact_dict = {
            "Name": self.__Name,
            "FirstName": self.__FirstName,
            "LastName": self.__LastName,
            "EmailAddress": self.__EmailAddress,
            "Addresses" : self.__Addresses,
            "AccountsReceivableTaxType": "OUTPUT",
            "AccountsPayableTaxType": "INPUT",
            "DefaultCurrency": "GBP"
        }

        if xero_auth_class.save_to_xero(endpoint, contact_dict):
            xero_reponse = xero_auth_class.get_xero_response()
            if xero_reponse['Contacts']:
                xero_reponse_contact = xero_reponse['Contacts'][0]
                self.__ContactID = xero_reponse_contact['ContactID']
            else:
                self.__ContactID = None
        else:
            self.__ContactID = None

        return self.__ContactID


#_address["AddressType"] = "POBOX"
#        _address["AddressLine1"] = addresses["AddressLine1"]
#        _address["AddressLine2"] = addresses["AddressLine2"]
#       _address["AddressLine3"] = addresses["AddressLine3"]
#       _address["AddressLine4"] = addresses["AddressLine4"]
#       _address["City"] = addresses["City"]
#       _address["Region"] = addresses["Region"]
#       _address["PostalCode"] = addresses["PostalCode"]
#       _address["Country"] = addresses["Country"]
#       self["Addresses"] = dict(Address=_address)


class XeroInvoice(XeroItem):

    def __init__(self):
        self.__Type = 'ACCREC'
        self.__Contact  = None
        self.__LineItems = []
        self.__Date = None
        self.__LineAmountTypes = 'Exclusive'
        self.__InvoiceNumber = None
        self.__Reference = None
        self.__Status = 'AUTHORISED'
        self.__SubTotal = 0.00
        self.__TotalTax = 0.00
        self.__Total = 0.00
        self.__InvoiceID = None
        return

    def create_invoice(self,order_data, xero_contact_id):
        self.__Contact = xero_contact_id
        self.__Date = order_data['date_added']
        self.__InvoiceNumber = 'SSAN-' + str(order_data['order_id'])
        if order_data['purchase_order_ref']:
            self.__Reference = order_data['purchase_order_ref']


    def add_order_lines(self, order_lines):
        lineitem = {}
        for product_line in order_lines:
            lineitem['Description'] = product_line['name'] + '(' + product_line['model'] + ')' + '\n' + \
                                      'Size: ' + product_line['size_name'] + '\n' + \
                                      'Material: ' + product_line['material_name']
            lineitem['Quantity'] = product_line['quantity']
            lineitem['UnitAmount'] = format(product_line['price'], '.2f')
            lineitem['LineAmount'] = format(product_line['total'], '.2f')
            #lineitem['TaxType'] = 'OUTPUT'
            lineitem['AccountCode'] = '200'

        self.__LineItems.append(lineitem)

    def add_shipping(self, shipping_rate):
        lineitem = {}
        lineitem['Description'] = 'Shipping on order'
        lineitem['Quantity'] = 1
        lineitem['UnitAmount'] = shipping_rate
        #lineitem['TaxType'] = 'OUTPUT'
        lineitem['AccountCode'] = '280'

        self.__LineItems.append(lineitem)

    def set_totals(self, subtotal, tax, total):
        self.__SubTotal = subtotal
        self.__TotalTax = tax
        self.__Total = total

    def save_invoice(self, xero_auth_class):
        post_fix = ''
        endpoint = 'Invoices'
        invoice_dict = {
            "Type": self.__Type,
            "Contact": {
                "ContactID":  self.__Contact
            },
            "InvoiceNumber": self.__InvoiceNumber + post_fix,
            "DateString": self.__Date,
            "DueDateString": self.__Date,
            "Status": self.__Status,
            "LineAmountTypes": self.__LineAmountTypes,
            "SubTotal": self.__SubTotal,
            "TotalTax": self.__TotalTax,
            "Total": self.__Total,
            "LineItems": self.__LineItems
        }
        if self.__Reference:
            invoice_dict['Reference'] = self.__Reference

        invoices_data = {"Invoices": [invoice_dict]}
        if xero_auth_class.save_to_xero(endpoint, invoices_data):
            xero_reponse = xero_auth_class.get_xero_response()
            if xero_reponse['Invoices']:
                xero_reponse_contact = xero_reponse['Invoices'][0]
                self.__InvoiceID = xero_reponse_contact['InvoiceID']
            else:
                self.__InvoiceID = None
        else:
            self.__InvoiceID = None

        return self.__InvoiceID



