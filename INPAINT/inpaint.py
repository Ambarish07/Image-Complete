import numpy as np
import cv2


# mouse movements 

class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv2.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv2.imshow(self.windowname, self.dests[0])
        cv2.imshow(self.windowname+": Mask",self.dests[1])
    def on_mouse(self, event, x, y, flags, param):
        pt = (x,y)
        if event == cv2.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv2.EVENT_LBUTTONUP:
            self.prev_pt = None
        if self.prev_pt and flags & cv2.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv2.line(dst,self.prev_pt, pt, color, 5)
            self.dirty = True
            self.prev_pt = pt
            self.show()



print("Inpaint")

#Read image in color mode
img = cv2.imread("1 (6).jpg",1)
img = cv2.resize(img,(500,500))    # change to 500 * 500 px
if img is None:
    print('Failed to load image file')
    exit(0)
img_mask = img.copy()

inpaintMask = np.zeros(img.shape[:2], np.uint8)
# print("came here1")
sketch = Sketcher('image',[img_mask, inpaintMask], lambda :((255,255,255), 255))

while True:
    ch = cv2.waitKey(0)

    if ch == 27:     #Esc key
        # print("breaking...")
        break
    if ch == ord('t'):
        res = cv2.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
        # print("came here2")
        cv2.imshow("Inpaint TELEA Recovered",res)
    if ch == ord('n'):
        res = cv2.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv2.INPAINT_NS)
        # print("came here3")
        cv2.imshow("Inpaint NS Recovered ",res)
    if ch == ord('r'):
        img_mask[:] = img
        inpaintMask[:]=0
        sketch.show()
        # print("came here...")
print("Completed")

cv2.destroyAllWindows()