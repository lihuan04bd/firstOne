# 上传操作分两种
# 1 直接可以输入的 send_keys(),输入上传的全路径即可
# 2 window 控件导致的上传 selenium 操作不了
# selenium 操作的都是 h5 相关的元素
#  用 python 的 pywin32 和 spy++
#与 window 系统交互的
#适用 ie firefox chrome
# pip install pywin32
import win32gui
import win32con

def upload(file_path):
    dialog = win32gui.FindWindow("#32770","打开")# 找到一级窗口
    #找到窗口
    comboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)

    comboBox = win32gui.FindWindowEx(comboBoxEx32,0,"ComboBox",None)

    edit = win32gui.FindWindowEx(comboBox,0,"Edit",None)
    button = win32gui.FindWindowEx(comboBox,0,"Button",None)

    file_path = ""
    win32gui.SendMessage(edit,win32con.VM_SETTEXT,None,file_path)
    import time
    time.sleep(5)
    win32gui.SendMessage(dialog,win32con.VM_COMMOD,1,button)