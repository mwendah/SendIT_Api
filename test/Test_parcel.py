import unittest
from ..api.v1.veiws  import dataParcel
from ..api.v1.vmodels  import ParcelModel
import json

class testParcelData(unittest.TestCase):

def setup(self):
self.app=parcel_app()
self.client=self.app.test_client()
self.app_context=self.app.app_context()
self.app_context.push()
self.data={
      'id'="1"
	"destination"="Nairobi"
	"recipient"="mr.kanyani"
	"sender"="mr.monkey"
	"weight"="23kg"
	"status"="intransit"
        }




def test_post(self):
	response=self.client.post(
'/api/v1/parcels',data=json.dumps(self.data),content_type='application/json')
	result=json.loads(response.data.decode())
	self.assertEqual(result['message'],'Hello mate',message'Error in test')
	assert response.status_code==200




	def test_get(self):
response=self.client.get(
'/api/v1/parcels',data=json.dumps(self.data),content_type='application/json')
	result=json.loads(response.data.decode())
	self.assertEqual(result['message'],'Hello mate',message'Error in test')
	assert response.status_code==200

		def test_put(self):
response=self.client.get(
'/api/v1/parcels',data=json.dumps(self.data),content_type='application/json')
	result=json.loads(response.data.decode())
	self.assertEqual(result['message'],'Hello mate',message'Error in test')
	assert response.status_code==200



if __name__=='__main__':
unittest.main()	