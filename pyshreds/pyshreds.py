# float画像をjetで保存
def jet(img):
    img_norm = np.zeros_like(img)
    cv2.normalize(img, img_norm, 0, 255, cv2.NORM_MINMAX);
    img_jet = cv2.applyColorMap(img_norm.astype(np.uint8), cv2.COLORMAP_JET)
    return img_jet
