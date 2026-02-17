from enum import Enum

class HttpCode(str,Enum):
    """HTTP基础业务状态码"""
    # 成功状态
    SUCCESS = "success"
    # 失败状态
    FAIL = "fail"
    # 未找到
    NOT_FOUND = "not_found"
    # 未授权
    UNAUTHORIZED = "unauthorized"
    # 无权限
    FORBIDDEN = "forbidden"
    # 验证失败
    VALIDATION_ERROR = "validation_error"
