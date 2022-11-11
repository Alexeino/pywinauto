from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import time
app = Application().start('calc.exe',timeout=10)
time.sleep(10)
app.connect(title="Calculator",timeout=10)
dialog = app['Calculator']
dialog.print_control_identifiers()

dialog.set_focus()
mouse.click(coords=(787,465))
time.sleep(5)
mouse.click(coords=(870,471))
time.sleep(5)
mouse.click(coords=(787,465))
time.sleep(5)
mouse.click(coords=(873,518))