# 9 AUGUST 2020
# IG DP GRABBER
# BY PRADEEP RAJ (M.P.R)

import instaloader
from PIL import Image

m = instaloader.Instaloader()

dp = input('Type the Username : ')

download = m.download_profile(dp,profile_pic_only=True)
pil = Image.open(downloaded)
pil.show()
#m.download_tagged(dp)