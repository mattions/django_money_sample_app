# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Bill.price_currency'
        db.add_column('myapp_bill', 'price_currency',
                      self.gf('djmoney.models.fields.CurrencyField')(default='GBP'),
                      keep_default=False)

        # Adding field 'Bill.price'
        db.add_column('myapp_bill', 'price',
                      self.gf('djmoney.models.fields.MoneyField')(max_digits=10, decimal_places=2, default_currency='GBP'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Bill.price_currency'
        db.delete_column('myapp_bill', 'price_currency')

        # Deleting field 'Bill.price'
        db.delete_column('myapp_bill', 'price')


    models = {
        'myapp.bill': {
            'Meta': {'object_name': 'Bill'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price': ('djmoney.models.fields.MoneyField', [], {'max_digits': '10', 'decimal_places': '2', 'default_currency': "'GBP'"}),
            'price_currency': ('djmoney.models.fields.CurrencyField', [], {'default': "'GBP'"})
        }
    }

    complete_apps = ['myapp']