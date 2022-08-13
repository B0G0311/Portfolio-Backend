from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Project, Technology
from .serializers import ProjectSerializer, TechnologySerializer


# Create your views here.
class TechnologyView(APIView):
    def get(self, request):
        """
        List the technologies already created
        """
        technologies = Technology.objects.all()
        serializer = TechnologySerializer(technologies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create the Technology tag
        """
        data = {
            'technology': request.data.get('technology'),
        }
        serializer = TechnologySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProjectListApiView(APIView):

    def get(self, request):
        """
        List all the items for a given requested user
        """

        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create the Project with given data
        """

        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'technology': request.data.get('technology'),
            # 'image': request.data.get('image'),
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailApiView(APIView):

    def get_object(self, project_id):
        """
        Helper method to get the object with given todo_id
        """
        try:
            return Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return None

    def get(self, project_id):
        """
        Helper method to get the object with given project_id
        """
        project_instance = self.get_object(project_id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProjectSerializer(project_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update
    def put(self, request, project_id):
        """
        updates the project item with given project_id if exists
        """
        project_instance = self.get_object(project_id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'technology': request.data.get('technology'),
            # 'image': request.data.get('image'),
        }
        serializer = ProjectSerializer(instance=project_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    def delete(self, project_id):
        """
        Deletes the project item with given project_id if exists
        """
        project_instance = self.get_object(project_id)
        if not project_instance:
            return Response(
                {"res": "Object with project id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        project_instance.delete()
        return Response(
            {"res": "object deleted!"},
            status=status.HTTP_200_OK
        )
