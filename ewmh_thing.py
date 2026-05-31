import ewmhlib
root=ewmhlib.EwmhRoot()
def set_dock():
    for i in root.getClientList():
        win_obj=ewmhlib.EwmhWindow(i)
        #print(win_obj.getName())
        if(win_obj.getName()=="sigma_bar"):
            win_obj.setWmWindowType("_NET_WM_WINDOW_TYPE_DOCK")

