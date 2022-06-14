
import pixellib
from pixellib.tune_bg import alter_bg
import cv2

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
output = change_bg.change_bg_img(f_image_path = "sample.jpg",b_image_path = "background.jpg")
cv2.imwrite("img.jpg", output)




'''
#>PixelLib supports tensorflow's version (2.0 - 2.4.1)
#>To check your verson `$pip show tensorflow` so no to `$pip install --upgrade tensorflow`
#>TensorFlow v2.1 is not compatibile with Python >3.8 (...)

import pixellib
from pixellib.tune_bg import alter_bg

change_bg = alter_bg()
change_bg.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")
change_bg.color_bg("sample.jpg", colors = (0,128,0), output_image_name="colored_bg.jpg")
'''