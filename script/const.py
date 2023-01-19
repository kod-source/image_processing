"""
Constant types in Python.
"""


class _const:
    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const (%s)" % name)
        self.__dict__[name] = value


import sys

sys.modules[__name__] = _const()

# ファイル名を指定
_const.FILE_NAME = "10k.jpg"
# 画像が保存されているファイルパス
_const.FILE_PATH = "img/" + _const.FILE_NAME
# 希望値（誤差率の計算で使用）
_const.DESIRED_VALUE = 10000
