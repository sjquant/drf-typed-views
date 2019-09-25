from .decorators import typed_action, typed_api_view, typed_method
from .param_settings import ParamSettings


def Query(*args, **kwargs):
    return ParamSettings("query_param", *args, **kwargs)


def Path(*args, **kwargs):
    return ParamSettings("path", *args, **kwargs)


def CurrentUser(*args, **kwargs):
    return ParamSettings("current_user", *args, **kwargs)


def Body(*args, **kwargs):
    return ParamSettings("body", *args, **kwargs)


def Param(*args, **kwargs):
    return ParamSettings(*args, **kwargs)
