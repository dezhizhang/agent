
class Config:
    def __init__(self):
        """关闭wtf的csrf保护"""
        self.WTF_ENABLED = False