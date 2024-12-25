from django.test import TestCase, Client
from rest_framework.test import APITestCase
from .models import Equation
from .serializers import EquationSerializer

# Create your tests here.

class EndpointTest(APITestCase):
    def setUp(self):
        self.equation = Equation.objects.create(
            id = 1,
            definition = "ENDPOIT TEST. NOT A REAL EQUATION"
        )

    def test_get_equation(self):
        response = self.client.get('/equation_service/equation/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['definition'], self.equation.definition)

    def test_edit_equation(self):
        new_definition = "NEW DEFINITION"
        response = self.client.post('/equation_service/equation/1/edit/', {'definition': new_definition})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['definition'], new_definition)

    def test_create_equation(self):
        response = self.client.post('/equation_service/equation/2/edit/', {'definition': self.equation.definition})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['definition'], self.equation.definition)
        self.assertEqual(Equation.objects.get(pk=2).definition, self.equation.definition)
