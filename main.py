import dearpygui.dearpygui as dpg
import subprocess
import time
import configparser
dpg.create_context()
config = configparser.ConfigParser()
config.read("config.ini")
all_cmd=""

with dpg.window(tag="win"):
    with dpg.group(horizontal=True):
        dpg.add_text(all_cmd,tag="all_cmd_tag")
        #dpg.add_spacer(width=20)
        #dpg.add_text(i,tag="cpu_tag")
i=1
for block in config.sections():#取得所有區塊的特定區塊
    cmd_to_run = config.get(block, "command", fallback="")
    cmd_label=config.get(block,"label",fallback="")
    bar_width=int(config.get("sigma_bar","width",fallback=1920))
    bar_height=int(config.get("sigma_bar","height",fallback=30))
    bar_x=int(config.get("sigma_bar","x",fallback=0))
    bar_y=int(config.get("sigma_bar","y",fallback=0))
    bar_split_sign=config.get("sigma_bar","split_sign",fallback=" | ")
    text_font=config.get("sigma_bar","font",fallback="")
    text_size=int(config.get("sigma_bar","font_size",fallback=20))
    #cmd=subprocess.check_output(config[block]["command"],shell=True).decode("utf-8").strip()
    cmd=subprocess.check_output(cmd_to_run,shell=True).decode("utf-8").strip()
    """
    取得所有區塊的所有值：
    for block in config.sections():#取得所有區塊的特定區塊
        keys=config.options(block)#取得特定區塊所有鍵
        for key in keys:
            value=config[block][key]#取得特定鍵下的值
    """
    if i!=len(config.sections()):
        if i==1 and cmd_to_run=="":
            all_cmd=all_cmd+cmd_label+cmd
        else:
            all_cmd=all_cmd+cmd_label+cmd+bar_split_sign
        i=i+1
    else:
        #if i==len(config.sections()):
        all_cmd=all_cmd+cmd_label+cmd
        
if(text_font!=""):
    with dpg.font_registry():
        with dpg.font(text_font, int(text_size)) as text_font_id:
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)      # 英文
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full) # 中文
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)     # 日文
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Korean)       # 韓文
                dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)     # 俄文
                # 手動加入 Nerd Fonts 的圖示區間 (PUA 區)
                dpg.add_font_range(0xE000, 0xF8FF)
    dpg.bind_font(text_font_id)
else:
    pass

dpg.set_primary_window("win", True)
dpg.create_viewport(title="sigma_bar",resizable=False,x_pos=bar_x,y_pos=bar_y,width=bar_width,height=bar_height,decorated=False,always_on_top=True,disable_close=True)
dpg.setup_dearpygui()
dpg.show_viewport()
while dpg.is_dearpygui_running():
    
    dpg.set_value("all_cmd_tag",all_cmd)

    print("this will run every frame")
    dpg.render_dearpygui_frame()
    time.sleep(0.5)
#dpg.start_dearpygui()
dpg.destroy_context()
