from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from .models import *
from .serializers import *

class AllocationTests(TestCase):

    def setUp(self):
       
        self.tech1 = Technology.objects.create(name="Python")
        self.tech2 = Technology.objects.create(name="Django")
        self.tech3 = Technology.objects.create(name="React")

        self.project = Project.objects.create(
            name="Projeto Backend",
            start_date=datetime(2025, 1, 1),
            end_date=datetime(2025, 2, 2),
        )
        self.project.Technologies.add(self.tech2)

        self.developer1 = Developer.objects.create(name="Dev1")
        self.developer2 = Developer.objects.create(name="Dev2")
        self.developer2.technologies.add(self.tech2)
        self.developer1.technologies.add(self.tech1)

        self.allocation_data = {
            'project': self.project.id,
            'developer': self.developer1.id,
            'hours': 40,
        }

        Allocation.objects.create(project=self.project, developer=self.developer1, hours=40)

    def test_tecnologias_associadas(self):
        
        serializers = AllocationSerializer(data=self.allocation_data)
        self.assertFalse(serializers.is_valid())
        self.assertIn('non_field_errors', serializers.errors)
        self.assertEqual(
            serializers.errors['non_field_errors'][0],
            'Developer does not have the required technology for the project.'
        )

    def test_allocation_date(self):
        project_data = {
            'name': 'Projeto Backend',
            'start_date': datetime(2022, 1, 1).date(),
            'end_date': datetime(2021, 1, 1).date(),  
            'Technologies': [self.tech2.id],  
        }
        serializer = ProjectSerializer(data=project_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('non_field_errors', serializer.errors)
        self.assertEqual(
            serializer.errors['non_field_errors'][0],
            'The end date must be later than the start date.'
    
        )

    def test_limit_hours_allocation(self):

        allocation_data = {
            'developer': self.developer2.id,
            'project': self.project.id,
            'hours': 350, 
        }
        serializers = AllocationSerializer(data=allocation_data)
        self.assertFalse(serializers.is_valid())
        self.assertIn('non_field_errors', serializers.errors)
        self.assertEqual(
            serializers.errors['non_field_errors'][0], 
            'Total allocated hours cannot exceed the planned hours for the project.'
        )
