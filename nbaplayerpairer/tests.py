from django.test import TestCase
from django.test.client import RequestFactory

from .forms import InputForm
from .views import get_heights

#Testing user input form
class InputFormTest(TestCase):

    #Test if only accepts integer input
    def test_non_integer_input(self): 
        form = InputForm(data={"user_input": "text"})
        self.assertTrue(not form.is_valid())
    
    #Test if zero input is accepted 
    def test_zero_input(self): 
        form = InputForm(data={"user_input": 0 })
        self.assertTrue(form.is_valid())
    
    #Test if negative input is not accepted
    def test_negative_input(self): 
        form = InputForm(data={"user_input": -1 })
        self.assertTrue(not form.is_valid())

#Testing get-heights view
class GetHeightsView(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    def test_details(self):
        request = self.factory.get('nbaplayers/')
        response = get_heights(request)
        self.assertEqual(response.status_code, 200)