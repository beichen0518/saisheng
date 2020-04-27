# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from ranking_list.models import TBRanking_list


def ranking_list_search(request):
    client_num = request.GET.get("client_num")
    high_grade = request.GET.get("high_grade")
    low_grade = request.GET.get("low_grade")
    if not client_num:
        return JsonResponse({"code": 1001, "msg": "参数错误", "data": {}})
    client = TBRanking_list.objects.filter(client_num=client_num).first()
    if not client:
        return JsonResponse({"code": 1002, "msg": "数据异常", "data": {}})
    client_dict = {"id": client.id, "client_num": client.client_num, "grade": client.grade}
    query = TBRanking_list.objects
    if high_grade and low_grade:
        query = query.order_by("-grade")[int(high_grade):int(low_grade)]
    else:
        query = query.all().order_by("-grade")
    ranking_list = query.values()
    result = {"code": 0, "msg": "success"}
    result["data"] = list(ranking_list)
    result["data"].append(client_dict)
    return JsonResponse(result)

def post_grade(request):
    client_num = request.POST.get("client_num")
    grade = request.POST.get("grade")
    print(client_num)
    if not all([client_num, grade]):
        return JsonResponse({"code": 1001, "msg": "参数错误", "data":{}})
    client = TBRanking_list.objects.filter(client_num=client_num).first()
    if client:
        client.grade = grade
        client.save()
    else:
        TBRanking_list.objects.create(
            client_num=client_num,
            grade=int(grade)
        )

    return JsonResponse({"code":0, "msg": "success", "data":{}})
