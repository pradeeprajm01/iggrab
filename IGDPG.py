# 9 AUGUST 2020
# IG DP GRABBER
# BY PRADEEP RAJ (M.P.R)

import instaloader


m = instaloader.Instaloader()

dp = input('Type the Username : ')

download = m.download_profile(dp,profile_pic_only=True)

#m.download_tagged(dp)
