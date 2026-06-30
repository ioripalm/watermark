from blind_watermark import WaterMark
import sys

mode=sys.argv[1]

if mode=='embed':
    img=sys.argv[2]
    wm=sys.argv[3]
    out=sys.argv[4]
    bwm=WaterMark(password_img=1,password_wm=1)
    bwm.read_img(img)
    bwm.read_wm(wm,mode='str')
    bwm.embed(out)
    print(len(bwm.wm_bit))

if mode=='extract':
    img=sys.argv[2]
    bwm=WaterMark(password_img=1,password_wm=1)
    wm=bwm.extract(img,wm_shape=int(sys.argv[3]),mode='str')
    print(wm)