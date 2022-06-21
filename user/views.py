from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from user.serializers import UserSignupSerializer


class UserView(APIView):
    permission_classes = [permissions.AllowAny]       # 누구나 view 접근 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인된 사용자만 view 접근 가능
    # permission_classes = [permissions.IsAdminUser]     # admin 유저만 view 접근 가능
    
    def get(self, request):
        return Response({"msg": "get method!!" })
    def post(self, request):
        return Response({"msg": "post method!!" })
    def put(self, request):
        return Response({"msg": "put method!!" })
    def delete(self, request):
        return Response({"msg": "delete method!!" })

class UserApiView(APIView):
    # 로그인
    @csrf_exempt
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

    #@로그아웃
    def delete(self, request):
        logout(request)
        return Response({"message": "logout success!"})

    #회원가입
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입 완료!"})
        else:
            print(serializer.errors)
            return Response({"message": "가입 실패!"})