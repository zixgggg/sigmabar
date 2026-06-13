import dearpygui.dearpygui as dpg
import subprocess
import time
import configparser
import ewmh_thing
from pathlib import Path
dpg.create_context()
config = configparser.ConfigParser()
config_path=str(Path.home())+"/.config/sigmabar/config.ini"
config.read(config_path)
print(f"config.read():{config.read(config_path)}")
all_cmd_output=""

with dpg.window(tag="win"):
    with dpg.group(horizontal=True):
        dpg.add_text(all_cmd_output,tag="all_cmd_tag")

bar_width=int(config.get("sigma_bar","width",fallback=1920))
bar_height=int(config.get("sigma_bar","height",fallback=30))
bar_height_is_font_size=config.getboolean("sigma_bar","bar_height_is_font_size",fallback=False)
bar_and_text_gap=int(config.get("sigma_bar","bar_and_text_gap",fallback=0))
bar_split_sign=config.get("sigma_bar","split_sign",fallback="   |   ")
update_gird=float(config.get("sigma_bar","update_grid",fallback=0.5))
font=config.get("sigma_bar","font",fallback="")
font_size=int(config.get("sigma_bar","font_size",fallback=20))
background_color_r=int(config.get("sigma_bar","background_color_r",fallback=0))
background_color_g=int(config.get("sigma_bar","background_color_g",fallback=0))
background_color_b=int(config.get("sigma_bar","background_color_b",fallback=0))
text_color_r=int(config.get("sigma_bar","text_color_r",fallback=255))
text_color_g=int(config.get("sigma_bar","text_color_g",fallback=255))
text_color_b=int(config.get("sigma_bar","text_color_b",fallback=255))
if bar_height_is_font_size==True:
    final_bar_height=font_size+bar_and_text_gap
else:
    final_bar_height=bar_height
print(f"""
bar_width={bar_width}
bar_height={bar_height}
bar_height_is_font_size={bar_height_is_font_size}
final_bar_height={final_bar_height}
bar_split_sign={bar_split_sign}
update_gird={update_gird}
font={font}
font_size={font_size}
bar_height_is_font_size={bar_height_is_font_size}
bar_and_text_gap={bar_and_text_gap}
background_color_r={background_color_r}
background_color_g={background_color_g}
background_color_b={background_color_b}
text_color_r={text_color_r}
text_color_g={text_color_g}
text_color_b={text_color_b}
""")
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg,value=(background_color_r,background_color_g,background_color_b),category=dpg.mvThemeCat_Core)#background color
        dpg.add_theme_color(dpg.mvThemeCol_Text,value=(text_color_r,text_color_g,text_color_b),category=dpg.mvThemeCat_Core)#text color
        dpg.add_theme_style(dpg.mvStyleVar_WindowPadding,x=0,y=0)
dpg.bind_theme(global_theme)
if(font!=""):
    with dpg.font_registry():
        with dpg.font(font, int(font_size)) as text_font_id:
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
dpg.create_viewport(title="sigma_bar",resizable=False,width=bar_width,height=final_bar_height,decorated=False,always_on_top=True,disable_close=True)#x_pos=bar_x,y_pos=bar_y
dpg.setup_dearpygui()
dpg.show_viewport()
ewmh_thing.set_dock()
while dpg.is_dearpygui_running():
    blocks_output_list=[]
    for block in config.sections():#取得所有區塊的特定區塊
        if block == "sigma_bar":
            continue
        cmd_to_run = config.get(block, "command", fallback="")
        cmd_label=config.get(block,"label",fallback="")
        #cmd=subprocess.check_output(config[block]["command"],shell=True).decode("utf-8").strip()
        cmd=subprocess.check_output(cmd_to_run,shell=True).decode("utf-8").strip()
        """
        取得所有區塊的所有值：
        for block in config.sections():#取得所有區塊的特定區塊
            keys=config.options(block)#取得特定區塊所有鍵
            for key in keys:
                value=config[block][key]#取得特定鍵下的值
        """
        if cmd_to_run!="":
            cmd = subprocess.check_output(cmd_to_run, shell=True).decode("utf-8").strip()
            blocks_output_list.append(cmd_label+cmd)
        elif cmd_label!="":
            blocks_output_list.append(cmd_label)
    all_cmd_output = bar_split_sign.join(blocks_output_list)
        
    dpg.set_value("all_cmd_tag",all_cmd_output)
    all_cmd_output=""
    #print("[sigmabar] this will run every update_grid")
    dpg.render_dearpygui_frame()
    time.sleep(update_gird)
#dpg.start_dearpygui()
dpg.destroy_context()
