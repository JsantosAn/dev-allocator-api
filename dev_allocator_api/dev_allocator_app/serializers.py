from rest_framework import serializers
from .models import Developer, Project, Allocation, Technology
from datetime import datetime
from django.db import models

def validate_technology_match(project_technologies, developer_technologies):
    if not project_technologies.intersection(developer_technologies):
        raise serializers.ValidationError(
            'Developer does not have the required technology for the project.',
            code='non_field_errors'
        )

def calculate_planned_hours(start_date, end_date):
    working_hours_per_day = 8
    return (end_date - start_date).days * working_hours_per_day

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    technologies = serializers.PrimaryKeyRelatedField(
        queryset=Technology.objects.all(), 
        many=True, 
        write_only=True
    )
    technology_names = serializers.SerializerMethodField()

    class Meta:
        model = Developer
        fields = '__all__'
        read_only_fields = ['technology_names']

    def get_technology_names(self, obj):
        return [tech.name for tech in obj.technologies.all()]

    def validate(self, data):
        if not data.get('technologies'):
            raise serializers.ValidationError('Developer must have at least one technology.')
        return data

class ProjectSerializer(serializers.ModelSerializer):
    technologies = serializers.PrimaryKeyRelatedField(
        queryset=Technology.objects.all(),
        many=True,
        write_only=True
    )
    technology_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['technology_names']

    def get_technology_names(self, obj):
        return [tech.name for tech in obj.Technologies.all()]

    def validate(self, data):
        if not data.get('technologies'):
            raise serializers.ValidationError('Project must have at least one technology.', code='non_field_errors')
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError('The end date must be later than the start date.', code='non_field_errors')
        return data

class AllocationSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), write_only=True)
    developer = serializers.PrimaryKeyRelatedField(queryset=Developer.objects.all(), write_only=True)
    project_info = serializers.SerializerMethodField()
    developer_info = serializers.SerializerMethodField()

    class Meta:
        model = Allocation
        fields = ['id', 'project', 'developer', 'hours', 'project_info', 'developer_info']

    def get_project_info(self, obj):
        project = obj.project
        return {
            'id': project.id,
            'name': project.name,
            'start_date': project.start_date,
            'end_date': project.end_date,
            'planned_hours': calculate_planned_hours(project.start_date, project.end_date),
            'technology_names': [tech.name for tech in project.Technologies.all()]
        }

    def get_developer_info(self, obj):
        developer = obj.developer
        return {
            'id': developer.id,
            'name': developer.name,
            'technology_names': [tech.name for tech in developer.technologies.all()]
        }

    def validate(self, data):
        project = data['project']
        developer = data['developer']
        hours = data['hours']

        project_technologies = set(project.Technologies.values_list('id', flat=True))
        developer_technologies = set(developer.technologies.values_list('id', flat=True))
        validate_technology_match(project_technologies, developer_technologies)

        if not project.start_date <= datetime.now().date() <= project.end_date:
            raise serializers.ValidationError('Allocation must be within project duration', code='non_field_errors')

        total_allocated_hours = (
            Allocation.objects.filter(project=project)
            .exclude(id=self.instance.id if self.instance else None)
            .aggregate(total_hours=models.Sum('hours'))['total_hours'] or 0
        )
        planned_hours = calculate_planned_hours(project.start_date, project.end_date)

        if total_allocated_hours + hours > planned_hours:
            raise serializers.ValidationError(
                'Total allocated hours cannot exceed the planned hours for the project.',
                code='non_field_errors'
            )

        return data