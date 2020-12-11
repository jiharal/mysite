from rest_framework.decorators import api_view
from . import models
from rest_framework.response import Response


class CommentsAPI(object):
    @api_view(["GET"])
    def get_all(request):
        resp = models.CommentsModel.objects.using('mongo').all()
        # print(resp)
        json_response = {
            'data': list(resp),
        }
        return Response(json_response)

    # @api_view(["GET"])
    # def get_detail(request):

    # @api_view(["POST"])
    # def create(request):

    # @api_view(["PUT"])
    # def update(request):

    # @api_view(["DELETE"])
    # def delete(request):
