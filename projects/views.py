from django.http import JsonResponse

from projects.models import Project


def get_projects(request):
    query_set = Project.objects.all()
    projects_list = {
        'projects': []
    }
    for item in query_set:
        projects_list['projects'].append(item.get_json())
    return JsonResponse(projects_list)
