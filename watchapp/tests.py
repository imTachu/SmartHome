from django.test import TestCase
from watchapp.models import Property
import csv
import os
import logging
from watchapp import views

log = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create your tests here.
#API

'''

class Request:
    def __init__(self):
        self.POST = {}
        self.FILES = {}
    def add_value(self,bound,value):
        self.POST[bound] = value
    def add_file(self, name,file):
    	self.FILES[name] = file

class PropertyFileTestCase(TestCase):
	def setUp(self):
		self.test_file = '/Users/gdbs887/Dropbox/Andes/4101_ProcesosAgiles/py/workspace/venv/watchapp/SmartHome/smarthome/static/test/PropertyLoad.csv'
		self.image1 = '/Users/gdbs887/Dropbox/Andes/4101_ProcesosAgiles/py/workspace/venv/watchapp/SmartHome/smarthome/static/test/python_logo.jpg'
		self.image2 = '/Users/gdbs887/Dropbox/Andes/4101_ProcesosAgiles/py/workspace/venv/watchapp/SmartHome/smarthome/static/test/python-logo.png'
		self.request1 = Request()
		self.request1.add_file("PropertyLoad",open(self.test_file, 'rb'))
		self.request1.add_file("image1",open(self.image1, 'rb'))
		self.request1.add_file("image2",open(self.image2, 'rb'))

	def test_file_structure(self):
		res = views.validate_structure_data(self.request1.FILES['PropertyLoad'],"str")
		log.debug("test_file_structure: res: " + str(res))
		unitRes = True
		reader = csv.reader(self.request1.FILES['PropertyLoad'], delimiter = ',')
		for row in reader:
			 log.debug("test_file_structure: " + str(len(row)))
			 for r in row :
			 	if type(r) is not str :
			 		unitRes = False
			 		break
			 if not unitRes :
			 	break
		self.request1.FILES['PropertyLoad'].close()
		log.debug("test_file_structure: unitRes: " + str(unitRes))
		self.assertEqual(unitRes,res)

	def test_file_extension(self):
		self.assertEqual('.csv',views.get_file_extension(self.request1.FILES['PropertyLoad'].name))
		self.assertEqual('.jpg',views.get_file_extension(self.request1.FILES['image1'].name))
		self.assertEqual('.png',views.get_file_extension(self.request1.FILES['image2'].name))

	def test_file_row_insert(self):
		views.upload_propertys(self.request1.FILES['PropertyLoad'])
		#count_propertys = 2
		count_propertys = len(Property.objects.all());
		file_read = self.request1.FILES['PropertyLoad']
		row_count = sum(1 for row in file_read)
		log.debug("test_file_row_insert: file count: " + str(row_count))
		log.debug("test_file_row_insert: db count: " + str(count_propertys))
		self.assertEqual(row_count,count_propertys)

	def test_file_data_existence(self):
		res = views.validate_structure_data(self.request1.FILES['PropertyLoad'],"str")
		file_read = self.request1.FILES['PropertyLoad']
		row_count = sum(1 for row in file_read)
		unitRes = True if row_count > 0 else False
		log.debug("test_file_data_existence: Val S-D: " + str(res))
		log.debug("test_file_data_existence: Row count: " + str(row_count))
		self.assertEqual(res,unitRes)


'''





