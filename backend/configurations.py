import os.path

SECRET_KEY = 'django-insecure-5s!y*ks5mr+8%mo-!of7h$_io1)mx3z8ur#1ksr8fgz76lj$9y'

DEBUG = True

CAS_SERVER_URL = 'https://pass.sdu.edu.cn/cas/'
# CAS_SERVER_URL = 'http://127.0.0.1:3000/cas/'

# CAS 版本
CAS_VERSION = '3'
# 存入所有 CAS 服务端返回的 User 数据。
CAS_APPLY_ATTRIBUTES_TO_USER = True

# django日志目录
LOGGING_DIR = os.path.abspath('./log')

HOME_PAGE = "https://info.tsxt.sdu.edu.cn/"

ROOT_UID = 192168000000

# user MinIO storage

