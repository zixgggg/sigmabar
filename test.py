import dearpygui.dearpygui as dpg
import configparser
from pathlib import Path

# 1. 讀取設定檔
config = configparser.ConfigParser()
config_path = Path.home() / ".config/sigmabar/config.ini"
config.read(config_path)
text_size = config.get("sigma_bar", "font")

# 2. 初始化 DPG
dpg.create_context()

# 這裡必須建立一個真實的視窗或 Group 作為測量基準
with dpg.window(label="Main", tag="main_window"):
    dpg.add_text("123", tag="target_text")

dpg.create_viewport(title='Sigma Bar', width=200, height=100)
dpg.setup_dearpygui()
dpg.show_viewport()

# 🔥 關鍵點 1：強制讓 GPU 渲染第一幀（喚醒字型與尺寸數據）
dpg.render_dearpygui_frame() 

# 🔥 關鍵點 2：這時候呼叫 get_text_size，絕對有值！
size = dpg.get_text_size(text="123")
print(f"文字寬高: {size}")

# 💡 安全示範：如果要拿元件寬度，拿視窗或實體元件的，不要拿 Tab Bar
window_width = dpg.get_item_width("main_window")
print(f"視窗寬度: {window_width}")

dpg.destroy_context()
