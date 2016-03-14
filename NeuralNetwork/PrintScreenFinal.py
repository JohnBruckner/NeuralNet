#import wx
import time
import platform




operSys = platform.system()

app = wx.App()  # Need to create an App instance before doing anything
dtime = 0.5 # Time to wait between captures
stime = 10 # Time to wait between starting the scritp and action
sysFlag = False


if operSys == 'Windows' or 'Darwin':
    import PIL
    sysFlag = True

else:
    import wx


def takeScreenshot(imgName, flag):

    if flag == False:
        screen = wx.ScreenDC()
        size = screen.GetSize()
        bmp = wx.EmptyBitmap(size[0], size[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, size[0], size[1], screen, 0, 0)
        del mem  # Release bitmap
        bmp.SaveFile(str(imgName), wx.BITMAP_TYPE_PNG)

    else:
        PIL.ImageGrab.grab().save(str(imgName), "JPEG")


def main(runTime):
    future = time.time() + runTime


    imgName = 1

    while time.time() < future:
        takeScreenshot(imgName)
        imgName += 1
        now = time.time()

    time.sleep(dtime)

print "Input for how long the script will run"
rTime = input()

print "The script will start in {} seconds".format(stime)

time.sleep(stime)
print "The script is now running"

main(rTime, sysFlag)
print "The script has finished running"

input()
