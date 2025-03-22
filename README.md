# mcp-server-wechat
实现pc端微信的mcp服务功能
就这么一个文件,自行安装依赖,自行创建虚拟环境.

vscode+cline

大致在 C:\Users\Administrator\AppData\Roaming\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json 增加如下
```
{
    "mcp-wechat": {
      "command": "D:\\PythonCode\\mcp-wechat\\mcp-wechat\\.venv\\Scripts\\python",
      "args": [
        "D:\\PythonCode\\mcp-wechat\\mcp-wechat\\main.py"
      ],
      "disabled": false,
      "autoApprove": [
        "wechat"
      ]
    }
}
```
"D:\\PythonCode\\mcp-wechat\\mcp-wechat\\main.py" 换成你文件位置 
"D:\\PythonCode\\mcp-wechat\\mcp-wechat\\.venv\\Scripts\\python" 换成你的虚拟环境位置
