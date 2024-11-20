from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

class CustomResponse(Response):
    def __init__(self, data=None, code=200, msg="Success", status=200, template_name=None, headers=None, content_type=None):
        """
        :param data: 响应数据
        :param code: 自定义业务状态码
        :param msg: 提示信息
        :param status: HTTP 状态码
        :param template_name: 模板名称（可选）
        :param headers: 头部信息
        :param content_type: 内容类型
        """
        response_data = {
            "code": code,
            "data": data,
            "msg": msg,
        }

        # 初始化 Response 的基础部分
        super().__init__(response_data, status=status, template_name=template_name, headers=headers, content_type=content_type)

        # 手动设置 accepted_renderer 和 accepted_media_type
        self.accepted_renderer = JSONRenderer()
        self.accepted_media_type = 'application/json'

        # 确保 renderer_context 被正确设置
        self.renderer_context = {
            'view': None,  # 你可以根据需要设置视图上下文
            'request': None  # 你可以根据需要设置请求上下文
        }

