from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Store


class StoreAPI(object):
    @api_view(["GET"])
    def get_all(request):
        resp = Store.objects.all().values()
        json_resp = {
            "data": resp
        }
        return Response(json_resp)

    @api_view(["GET"])
    def get_detail(request, id):
        try:
            data = Store.objects.get(id=id)
            json_resp = {
                "data": data,
            }
            return Response(json_resp)
        except Store.DoesNotExist as err:
            print(err)
            json_resp = {
                "code": status.HTTP_204_NO_CONTENT,
                "message": f"{err} Store id is {id}",
            }
            return Response(json_resp, status=status.HTTP_204_NO_CONTENT)
