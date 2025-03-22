import mcp.server
import wxauto
from wxauto import WeChat

wx = WeChat()


my_mcp=mcp.server.FastMCP("wechat")

@my_mcp.tool()
def send_text(text:str,nick_name:str):
    '''发送文本信息给指定的昵称的群或者个人'''
    wx.SendMsg(text,nick_name)
    return "ok"

@my_mcp.tool()
def send_files(files_path:str|list,nick_name:str):
    '''发送文件(包含图片等文件)给指定的群或者个人'''
    wx.SendFiles(files_path,nick_name)
    return "ok"

send_text("你好","群1")

my_mcp.run()