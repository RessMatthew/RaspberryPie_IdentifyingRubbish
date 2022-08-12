# import time;
# ts = int(time.time()*1000)
# print(ts)

import hashlib
import time

timestamp = int(time.time() * 1000)
secretKey = 'd4ad7839a0becf6eebdd7db8be543a35'
sign = hashlib.md5((secretKey + str(timestamp)).encode()).hexdigest()
print(sign)

# password = 'abc123'
# SALE = password[:4]  # 取密码的前4位
# md = hashlib.md5(password.encode())
# print(md.hexdigest())  # 单纯的MD5加密
# md_sale = hashlib.md5((password + SALE).encode())  # MD5加盐加密
# # md5加盐可以将盐拼接在原密码后，也可以使用jion将盐穿插在原密码间
# str(password).join(SALE)  # 将password整体插入SALE的每个元素之间。
# print(str(password) + SALE)
# md5salepwd = md_sale.hexdigest()
# print('加密后为：', md5salepwd)
