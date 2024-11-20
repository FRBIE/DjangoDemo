from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging
logger = logging.getLogger(__name__)
def custom_exception_handler(exc, context):
    logger.error(f"Exception: {exc}, Context: {context}")
    """
    自定义异常处理器
    """
    # 调用默认的异常处理器
    response = exception_handler(exc, context)

    if response is not None:
        # 捕获认证相关的异常并自定义返回格式
        if response.status_code == 401:
            response.data = {
                "code": 40003,
                "data": None,
                "msg": "无权限"
            }
        elif response.status_code == 403:
            response.data = {
                "code": 40004,
                "data": None,
                "msg": "权限不足"
            }
    else:
        # 捕获非 DRF 处理的异常
        response = Response({
            "code": 50000,
            "data": None,
            "msg": "服务器内部错误"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
