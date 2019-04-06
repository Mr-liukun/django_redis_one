
from redis import StrictRedis
from django.http import HttpResponse
import pymysql
import json

def mysql(request):
    pydb = pymysql.connect("172.17.0.2", "root", "123456", "onedb")
    cu = pydb.cursor()
    cu.execute("select id, name, score from student")
    re = cu.fetchall()
    return HttpResponse(json.dumps(re), content_type="application/json")

def redis(request):
    sr = StrictRedis(host="172.17.0.3", port=6379, db=0, decode_responses=True)

    sr.set("name", "liukun")
    sr.set("id", "1")
    list1 = [sr.get("name"), sr.get("id")]

    return HttpResponse(list1)

