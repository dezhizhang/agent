
import os
class Config:
    def __init__(self):
        """关闭wtf的csrf保护"""
        self.SECRET_KEY = os.getenv("SECRET_KEY")
        self.WTF_CSRF_ENABLED = False