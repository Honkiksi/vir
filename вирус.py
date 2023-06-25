import win32api 
import win32con
import time

d = win32api.EnumDisplayDevices(None, 0);
dm = win32api.EnumDisplaySettings(d.DeviceName, win32con.ENUM_CURRENT_SETTINGS)

while True:
    orientation = (dm.DisplayOrientation + 2) % 4

    dm.DisplayOrientation = orientation
    dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
    dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION

    win32api.ChangeDisplaySettingsEx(d.DeviceName, dm)
    time.sleep(0.5)