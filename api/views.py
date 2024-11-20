from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Demo.utils.response_format import CustomResponse



class ProtectView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return CustomResponse(data="hello",code=20000,msg="测试msg")




class ChartDataView(APIView):
    permission_classes = [IsAuthenticated]  # 添加权限控制，确保只有认证用户能访问

    def get(self, request):
        data_axis = ['点', '击', '柱', '子', '或', '者', '两', '指', '在', '触', '屏', '上', '滑', '动', '能', '够', '自', '动', '缩', '放']
        data = [220, 182, 191, 234, 290, 330, 310, 123, 442, 321, 90, 149, 210, 122, 133, 334, 198, 123, 125, 220]
        y_max = 500

        response_data = {
            "data": {
                "dataAxis": data_axis,
                "data": data,
                "yMax": y_max
            },
        }

        return CustomResponse(data=response_data, code=200, msg='请求成功')