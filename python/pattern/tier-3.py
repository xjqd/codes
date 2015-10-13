#!/bin/python
class Data(object):
	"""Data store class"""
	products = {
		'milk':{'price':1.50, 'quantity':10},
		'eggs':{'price':0.20, 'quantity':100},
		'cheese':{'price':2.00, 'quantity':10}
		   }
	li = ['a', 'b', 'c']
        # descriptor
	def __get__(self,obj,klas):
	#def get__(self):
		print "Fetching from Data Store"
		return {'products': self.products}


class BusinessLogic(object):
	""" Business logic holding data store instances """
	data = Data()
	
	def product_list(self):
		return self.data['products'].keys()
		#wrong return self.data.products.keys()
		#return self.data['li']
	
	def product_information(self, product):
		return self.data['products'].get(product,None)
	

class Ui(object):
	""" UI interface class """
	
	def __init__(self):
		self.business_logic = BusinessLogic()

	def get_product_list(self):
		print "PRODUCT LIST"
		for product in self.business_loigc.product_list():
			print product
		print " "

	def get_product_information(self, product):
		product_info = self.business_logic.product_information(product)
		if product_info:
			print "PRODUCT INFORMATION"
			print 'Name:{0}, Price:{1:.2f}, Quantity{2:}'.format(product_info.title(),
						product_info.get('price', 0),
						product_info.get('quantity', 0))
		else:
			print 'That product "{0}" does not exist in the records'.format(product)

if __name__=="__main__":
	d = Data();
	#print d.get__()
	b = BusinessLogic()
	print b.product_list()

