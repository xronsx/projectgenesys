#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Club(models.Model):
	club_number = models.IntegerField(primary_key=True)
	club_name = models.CharField(unique=True, max_length=255)
	company_name = models.CharField(max_length=255)
	file_date = models.DateTimeField('fecha admision', auto_now_add = False)
	record_time_stamp = models.CharField(max_length=255)

	def __unicode__(self):
		return self.club_name

class Member(models.Model):
	member_number = models.IntegerField(primary_key=True)
	club_number = models.ForeignKey(Club, related_name="club_number_de")
	first_name = models.CharField(max_length=255)
	middle_initial = models.CharField(max_length=255, blank = True)
	last_name = models.CharField(max_length=255)
	gender = models.CharField(max_length=255, blank = True)
	address_line_1 = models.CharField(max_length=600, blank = True)
	address_line_2 = models.CharField(max_length=600, blank = True)
	city = models.CharField(max_length=255, blank = True)
	state = models.CharField(max_length=255, blank = True)
	zip_code = models.IntegerField(blank = True)
	zip_plu4 = models.IntegerField(blank = True)
	country = models.CharField(max_length=255, blank = True)
	bad_addr_flag = models.CharField(max_length=255, blank = True)
	home_phone = models.CharField(max_length=255, blank = True)
	work_phone = models.CharField(max_length=255, blank = True)
	work_extension = models.CharField(max_length=255, blank = True)
	cell_phone = models.CharField(max_length=255, blank = True)
	emer_phone = models.CharField(max_length=255, blank = True)
	ssn = models.CharField(max_length=255, blank = True)
	driver_license = models.CharField(max_length=255, blank = True)
	date_of_birth = models.CharField(max_length=255, blank = True)
	email = models.CharField(max_length=255, blank = True)
	barcode = models.CharField(max_length=255, blank = True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

class Formadepago(models.Model):
	member_number = models.ForeignKey(Member, related_name="member_number_de")
	draft_under_first_name = models.CharField(max_length=255)
	draft_under_last_name = models.CharField(max_length=255)
	bank_routing_number = models.CharField(max_length=255, blank = True)
	bank_account_number = models.CharField(max_length=255, blank = True)
	bank_account_type = models.CharField(max_length=255, blank = True)
	credit_card_number = models.CharField(max_length=255)
	credit_card_expire = models.CharField(max_length=255)
	credit_card_type = models.CharField(max_length=255)

	def __unicode__(self):
		return self.draft_under_first_name + ' ' + self.draft_under_last_name

class Pagos(models.Model):
	member_number = models.ForeignKey(Member, related_name="member_number_dee")
	first_due_date = models.DateTimeField('fecha primer debito', auto_now_add = False)
	over_payment = models.IntegerField(blank = True)
	number_of_payments = models.IntegerField(blank = True)
	down_payment = models.IntegerField(blank = True)
	last_payment_code = models.CharField(max_length=255, blank = True)
	last_payment_amount = models.IntegerField(blank = True)
	last_payment_date = models.DateTimeField('fecha ultimo debito', auto_now_add = False)
	last_payment_description = models.CharField(max_length=255, blank = True)

	def __unicode__(self):
		return self.member_number.first_name + ' ' + member_number.last_name

class Deuda(models.Model):
	member_number = models.ForeignKey(Member, related_name="member_number_deee")
	expire_date = models.DateTimeField('fecha en que inicia la deuda', auto_now_add = False)
	next_due_amount = models.IntegerField(blank = True)
	payments_remaining = models.IntegerField(blank = True)
	balance_remaining = models.IntegerField(blank = True)
	total_past_due_amt = models.IntegerField(blank = True)
	past_due_30_ene = models.IntegerField(blank = True)
	past_due_31_60 = models.IntegerField(blank = True)
	past_due_61_90 = models.IntegerField(blank = True)
	past_due_91_and_up = models.IntegerField(blank = True)
	late_fees_balance = models.IntegerField(blank = True)
	oldest_late_fee = models.DateTimeField('fecha de servicio mas antiguo', auto_now_add = False)
	oldest_due_date = models.DateTimeField('fecha de la dueda más antigua', auto_now_add = False)
	oldest_amount_due = models.DateTimeField('', auto_now_add = False)
	last_invoice_scheduled = models.DateTimeField('ultima factura programada', auto_now_add = False)
	pending_cancel_amount = models.IntegerField(blank = True)
	last_late_fee = models.IntegerField(blank = True)
	last_service_fee = models.IntegerField(blank = True)

	def __unicode__(self):
		return self.member_number.first_name + ' ' + member_number.last_name