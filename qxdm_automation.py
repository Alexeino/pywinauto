from pywinauto.application import Application
import time
import pywinauto.mouse as mouse
from pywinauto.timings import TimeoutError

# import psutils

first_title = "QXDM_Pro_5.1.320 - Qualcomm HS-USB Diagnostics 9091 (COM7)"
disconnected_title = "QXDM_Pro_5.1.320 (Disconnected)"
sdm845_title = "Qualcomm HS-USB Diagnostics 9091 (COM7)"

try:

    # app = Application(backend="uia").connect(title=first_title,timeout=10)
    app = Application(backend="uia").connect(title_re=r"^QXDM_Pro_5.1.320.*", timeout=10)
    print("App already running")
except TimeoutError:
    print("App not running. Starting QXDM")
    app = Application(backend="uia").start("C:\\Program Files (x86)\\Qualcomm\\QXDM5\\QXDM.exe", timeout=70).connect(
        title_re=r"^QXDM_Pro_5.1.320.*", timeout=10)

top_dlg = app.top_window()
top_title = top_dlg.texts()[0]
print(top_title)


def connect_to_device():
    main_dlg = app.QXDMPro51320Disconnected
    main_dlg.set_focus()
    time.sleep(2)
    # main_dlg.print_control_identifiers()

    toolbar = main_dlg.child_window(title="toolBar", auto_id="QXDMWindow.toolBar",
                                    control_type="ToolBar").wrapper_object()

    # main_dlg.print_control_identifiers()
    try:
        dvc_dlg = main_dlg.child_window(title="Device Selection", auto_id="QXDMWindow.DeviceSelectionDialogClass",
                                        control_type="Window").wrapper_object()
    except Exception as e:
        print("Device Selection Window not open - ")
        connect_btn = main_dlg.child_window(title="Connect", control_type="Button").wrapper_object()
        connect_btn.click_input()
        dvc_dlg = main_dlg.child_window(title="Device Selection", auto_id="QXDMWindow.DeviceSelectionDialogClass",
                                        control_type="Window").wrapper_object()

    # print(dir(dvc_dlg))

    try:
        sdm485_item = main_dlg.child_window(title="Qualcomm HS-USB Diagnostics 9091 (COM7)",
                                            control_type="DataItem").wrapper_object()
        sdm485_item.click_input()
    except Except as e:
        print(e)

    connect_device = main_dlg.child_window(title="Connect",
                                           auto_id="QXDMWindow.DeviceSelectionDialogClass.m_pConnectionTabs.qt_tabwidget_stackedwidget.tab_5._connectDiagButton",
                                           control_type="Button").wrapper_object()
    connect_device.click_input()
    time.sleep(2)
    # main_dlg.print_control_identifiers()

    try:
        g_app = Application(backend="uia").connect(title="Golden DMC Check", timeout=10)
        g_dlg = g_app.GoldenDMCCheck
        # g_dlg.print_control_identifiers()
        yes_btn = g_dlg.child_window(title="Yes", control_type="Button").wrapper_object()
        yes_btn.click_input()

    except Exception as e:
        print("Exception - ", e)


if top_title == disconnected_title:
    print("QXDM is not connected")
    connect_to_device()
elif top_title == first_title:
    print("QXDM is already connected to 9091 (COM7)")




