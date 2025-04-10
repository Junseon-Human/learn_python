# 필로우는 이미지를 처리하고 다루는 외부 라이브러리
# pip install pillow 로 설치 이후 사용 가능

"""이미지를 캔버스로 만들어서 띄우기"""
# from PIL import Image, ImageTk, ImageFilter
# import tkinter as tk

# # 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다.
# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# # 윈도우를 생성하고 윈도우 안에 캔버스를 생성한다.
# img = Image.open("etc/lenna.png")

# # tk 형식으로 이미지를 변환
# out = img.rotate(45)  # 반 시계 방향으로 45도 회전
# tk_img = ImageTk.PhotoImage(out)

# # tkinter의 캔버스에 영상을 표시한다.
# canvas.create_image(250, 250, image=tk_img)

# window.mainloop()

# """이미지에 블러처리 하기"""

# from PIL import Image, ImageTk
# import tkinter as tk

# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# img = Image.open("etc/lenna.png")

# out = img.filter(ImageFilter.BLUR)  # 이 부분이 블러처리 하는 부분
# tk_img = ImageTk.PhotoImage(out)

# canvas.create_image(250, 250, image=tk_img)

# window.mainloop()

"""메뉴 만들기"""
# import tkinter as tk


# def open():
#     pass


# def quit():
#     window.quit()


# window = tk.Tk()
# menubar = tk.Menu(window)

# filemenu = tk.Menu(menubar)
# filemenu.add_command(label="열기", command=open)
# filemenu.add_command(label="종료", command=quit)

# menubar.add_cascade(label="파일", menu=filemenu)

# window.config(menu=menubar)
# window.mainloop()

"""이미지 처리와 메뉴를 연결해서 만들기"""
# import tkinter as tk
# from PIL import Image, ImageTk, ImageFilter
# from tkinter import filedialog as fd

# im = None
# tk_img = None


# def open():
#     global im, tk_img
#     fname = fd.askopenfilename()
#     im = Image.open(fname)
#     tk_img = ImageTk.PhotoImage(im)
#     canvas.create_image(250, 250, image=tk_img)
#     window.update()


# def quit():
#     window.quit()


# def image_rotate():
#     global im, tk_img
#     out = im.rotate(45)
#     tk_img = ImageTk.PhotoImage(out)
#     canvas.create_image(250, 250, image=tk_img)


# def image_blur():
#     global im, tk_img
#     out = im.filter(ImageFilter.BLUR)
#     tk_img = ImageTk.PhotoImage(out)
#     canvas.create_image(250, 250, image=tk_img)
#     window.update()


# # 윈도우 생성
# window = tk.Tk()
# canvas = tk.Canvas(window, width=500, height=500)
# canvas.pack()

# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar)
# ipmenu = tk.Menu(menubar)
# filemenu.add_command(label="열기", command=open)
# filemenu.add_command(label="종료", command=quit)

# ipmenu.add_command(label="영상회전", command=image_rotate)
# ipmenu.add_command(label="영상흐리게", command=image_blur)

# menubar.add_cascade(label="파일", menu=filemenu)
# menubar.add_cascade(label="영상처리", menu=ipmenu)

# window.config(menu=menubar)
# window.mainloop()

"""이미지 크롭하기"""
from PIL import Image

img = Image.open("etc/june.png")
# print(img.format, img.size, img.mode) # JPEG (204, 192) RGB
# img.show()

box = (76, 3, 156, 183)
crop_img = img.crop(box)
crop_img.save("etc/june_torch.png")
# print(crop_img.format, crop_img.size, crop_img.mode)
# crop_img.show()


"""이미지 크롭하여 원본이미지에 특정 형식으로 붙여넣기"""
"""예제1"""
from PIL import Image

img = Image.open("etc/june.png")
box = (76, 3, 156, 183)
crop_img1 = img.crop(box)

drop = (0, 3, 80, 183)  # 붙여넣을 위치
img.paste(crop_img, drop)
# img.show()

"""예제2"""

img2 = Image.open("etc/june.png")
crop_img2 = crop_img1.resize((40, 90))
crop_img2.save("etc/40x90.png")
drop = (20, 40, 60, 130)
img2.paste(crop_img2, drop)

box = (80, 3, 180, 103)
crop_img3 = img2.crop(box).rotate(90)
drop = (220, 0, 320, 100)
img2.paste(crop_img3, drop)
# img2.show()

"""예제3"""
from PIL import Image

img4 = Image.open("etc/june.png")

box = (76, 3, 156, 333)
crop4 = img4.crop(box)
crop_img4 = crop4.transpose(Image.FLIP_LEFT_RIGHT)
drop = (0, 3, 80, 333)
img4.paste(crop_img4, drop)
img4 = img4.transpose(Image.FLIP_LEFT_RIGHT)
img4.save("etc/flip_june.png")
# img4.show()

"""이미지에 필터 적용해보기"""
from PIL import Image, ImageFilter

img = Image.open("etc/june.png")
img1 = img.filter(ImageFilter.CONTOUR)
img1.save("etc/june_counter.png")

img2 = img.filter(ImageFilter.EMBOSS)
img2.save("etc/june_emboss.png")

img3 = img.filter(ImageFilter.SMOOTH_MORE)
img3.save("etc/june_smooth_more.png")

""""""
img4 = Image.open("etc/june.png")

rgb = img4.split()

(
    r,
    g,
    b,
) = (
    rgb[0],
    rgb[1],
    rgb[2],
)
img4 = Image.merge("RGB", (b, b, g))
img4.save("etc/june_BBG.png")

img5 = Image.merge("RGB", (b, r, g))
img5.save("etc/june_BRG.png")
