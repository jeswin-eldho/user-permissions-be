from rest_framework.views import APIView
from rest_framework.response import Response as DRFResponse

from djangoProject.permissions.models import User, Role
from djangoProject.permissions.serializers import UserSerializer, RoleSerializer


class UserView(APIView):

    @staticmethod
    def post(request):
        try:
            data = request.data
            user = data["user"]
            roles = data["roles"]
            user_db = User.objects.prefetch_related("roles").get(name=user["name"])
            user_db.roles.clear()

            for role in roles:
                role_db = Role.objects.get(id=role)
                user_db.roles.add(role_db)
        except Exception as e:
            print(e)
            return DRFResponse(status=500, data={"message": "Something went wrong"})

        return DRFResponse(status=200, data={"message": "Successfully added user"})

    @staticmethod
    def get(request):
        name = request.GET.get("name", "")

        user_db = User.objects.get(name=name)
        user_data = UserSerializer(user_db).data
        return DRFResponse(status=200, data={"data": user_data})


class RoleView(APIView):

    @staticmethod
    def get(request):
        roles = Role.objects.all()
        roles_data = RoleSerializer(roles, many=True).data
        return DRFResponse(status=200, data={"data": roles_data})


class UsersView(APIView):

    @staticmethod
    def get(request):
        users = User.objects.all()
        users = UserSerializer(users, many=True).data
        return DRFResponse(status=200, data={"data": users})
