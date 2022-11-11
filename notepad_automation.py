from pywinauto.application import Application

app = Application().start('notepad.exe',timeout=10)
main_dlg = app.UntitledNotepad
main_dlg.wait('visible')

main_dlg.Edit.type_keys("Hello Everyone, This is Adbhutam...",with_spaces=True)
main_dlg.menu_select("File -> Save")
# main_dlg.print_control_identifiers()
main_dlg = app.SaveAs
# x = main_dlg.print_control_identifiers()

file_name_input = main_dlg.child_window(title="*.txt", class_name="Edit").wrapper_object()
file_name_input.type_keys("Test Notepad file.txt",with_spaces=True)

# main_dlg.print_control_identifiers()

save_btn = main_dlg.child_window(title="&Save",class_name="Button").wrapper_object()
save_btn.click()

main_dlg = app.ConfirmSaveAs
# main_dlg.print_control_identifiers()

overwrite_input = main_dlg.child_window(title="&Yes",class_name="Button").wrapper_object()
overwrite_input.click()

# cancel_btn = main_dlg.child_window(title="Cancel", class_name="Button").wrapper_object()
# cancel_btn.click()
# child_window(title="Cancel", class_name="Button")