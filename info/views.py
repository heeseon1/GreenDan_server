from django.http import JsonResponse
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import History
from .models import QnA, Scrap, Report
from .serializers import QnASerializer, ScrapSerializer, ReportSerializer

# Create your views here.

# QnA 뷰 (전체)
class AllQnaAPIView(APIView):
    def get(self, request):
        email = request.user.email

        if email:
            try:
                qnas = QnA.objects.filter(email=email).order_by('-id')
                serializer = QnASerializer(qnas, many=True)
                result = {
                    "code": 200,
                    "message": "성공적으로 수행됐습니다!",
                    "result": serializer.data
                }
                return JsonResponse(result, status=status.HTTP_200_OK)
            except qnas.DoesNotExist:
                result = {
                    "code": 404,
                    "message": "문의를 찾을 수 없습니다!",
                }
                return JsonResponse(result, status=status.HTTP_404_NOT_FOUND)
        else:
            result = {
                "code": 400,
                "message": "등록된 이메일이 아닙니다!",
            }
            return JsonResponse(result, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = QnASerializer(data=request.data)
        if serializer.is_valid():
            email = request.user.email
            serializer.validated_data['email'] = email

            serializer.save()
            result = {
                "code": 201,
                "message": "성공적으로 생성됐습니다!",
                "result": serializer.data
            }
            return JsonResponse(result, status=status.HTTP_201_CREATED)
        else :
            print(serializer.errors)
            result = {
                "code": 400,
                "message": "요청에 실패했습니다.",
                "result": serializer.data
            }
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# QnA 뷰 (상세)
class QnaAPIView(APIView):
    def get(self, request, pk):
        qna = get_object_or_404(QnA, id=pk)
        serializer = QnASerializer(qna)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return JsonResponse(result, status=status.HTTP_200_OK)

    def put(self, request, pk):
        qna = get_object_or_404(QnA, id=pk)
        serializer = QnASerializer(QnA, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = {
                "code": 200,
                "message": "성공적으로 수행됐습니다!",
                "result": serializer.data
            }
            return JsonResponse(result, status=status.HTTP_200_OK)

        result = {
            "code": 400,
            "message": "요청에 실패했습니다.",
            "result": serializer.data
        }
        return JsonResponse(result, status=status.HTTP_400_BAD_REQUEST)



# 스크랩 뷰
class ScrapAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ScrapSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, email):
        email = request.GET.get('email')

        if email:
            try:
                scraps = Scrap.objects.filter(email=email).order_by('-id')
                serializer = ScrapSerializer(scraps, many=True)
                result = {
                    "code": 200,
                    "message": "성공적으로 수행됐습니다!",
                    "result": serializer.data
                }

                return JsonResponse(result, status=status.HTTP_200_OK)

            except scraps.DoesNotExist:
                result = {
                    "code": 404,
                    "message": "해당 스크랩을 찾을 수 없습니다!",
                }
                return JsonResponse(result, status=status.HTTP_404_NOT_FOUND)
        else:
            result = {
                "code": 400,
                "message": "이메일이 없습니다!",
            }
            return JsonResponse(result, status=status.HTTP_400_BAD_REQUEST)


# 제보 뷰 (전체)
class AllReportAPIView(APIView):
    def get(self, request):
            try:
                reports = Report.objects.all().order_by('-id')
                serializer = ReportSerializer(reports, many=True)
                result = {
                    "code": 200,
                    "message": "현재 등록된 문의사항입니다.",
                    "result": serializer.data
                }
                return JsonResponse(result, status=status.HTTP_200_OK)
            except Exception as e:
                result = {
                    "code": 500,
                    "message": "서버 에러입니다",
                }
                return JsonResponse(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# 제보 뷰 (상세)
class ReportAPIView(APIView):
    def get(self, request, pk):
        report = get_object_or_404(Report, id=pk)
        serializer = ReportSerializer(report)
        result = {
            "code": 200,
            "message": "성공적으로 수행됐습니다!",
            "result": serializer.data
        }
        return JsonResponse(result, status=status.HTTP_200_OK)

    def put(self, request, pk):
        report = get_object_or_404(Report, id=pk)
        serializer = ReportSerializer(report, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = {
                "code": 200,
                "message": "성공적으로 수행됐습니다!",
                "result": serializer.data
            }
            return Response(result, status=status.HTTP_200_OK)
        result = {
            "code": 400,
            "message": "요청에 실패했씁니다.",
            "result": serializer.data
        }
        return JsonResponse(result, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = {
                "code": 201,
                "message": "성공적으로 생성됐습니다!",
                "result": serializer.data
            }
            return JsonResponse(result, status=status.HTTP_201_CREATED)
        result = {
            "code": 400,
            "message": "요청에 실패했습니다.",
            "result": serializer.data
        }
        return JsonResponse(result, status=status.HTTP_400_BAD_REQUEST)