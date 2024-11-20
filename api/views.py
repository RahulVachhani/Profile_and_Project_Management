
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from myprojects.models import Project, Review
from .serializers import ProjectSerializers

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'GET /api'},
        {'GET /api/projects'},
        {'GET /api/projects/id'},
        {'POST /api/projects/id/votes'},


        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProjects(request):
    # print("USER: ",request.user)
    projects = Project.objects.all()
    serializers = ProjectSerializers(projects, many=True)
    # print(serializers)
    # print(type(serializers))
    return Response(serializers.data)


@api_view(['GET'])
def getProject(request,pk):
    project = Project.objects.get(id = pk)
    serializers = ProjectSerializers(project, many=False)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def getProjectsVote(request,pk):
    project = Project.objects.get(id = pk)
    user = request.user.profile
    data = request.data

    review, created = Review.objects.get_or_create(
       owner = user,
       project = project
    )
    review.value = data.get("value","up")
    # print(review.value)

    review.save()
    project.getVoteCount

    serializer = ProjectSerializers(project, many=False)

    return Response(serializer.data)



