#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 11:31 上午
# @File    : conf.py
# @Project : jd_scripts
# @Desc    : 脚本配置文件
import os
import sys
import random
import re
import yaml
import platform

# 项目根目录
BASE_DIR = os.path.split(os.path.abspath(sys.argv[0]))[0]

# 日志目录
LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 示例配置文件路径
EXAMPLE_CONFIG_PATH = os.path.join(BASE_DIR, 'conf/.config_example.yaml')

# 备份配置文件路径
BAK_CONFIG_PATH = os.path.join(BASE_DIR, 'conf/config.yaml.bak')

# 配置文件路径
CONF_PATH = os.path.join(BASE_DIR, 'conf/config.yaml')

# sqlite3保存路径
DB_PATH = os.path.join(BASE_DIR, 'sqlite.db')

IMAGES_DIR = os.path.join(BASE_DIR, 'static/images')

if platform.system() == 'Windows':
    IMAGES_DIR = IMAGES_DIR.replace('/', '\\')

# 创建日志文件夹
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# 创建图片资源文件夹
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)

try:
    # 加载配置文件
    with open(CONF_PATH, 'r', encoding='utf-8-sig') as f:
        cfg = yaml.safe_load(f)
except Exception as e:
    print('无法读取config.yaml配置, 请检查配置！！!')
    sys.exit(1)

# 是否开启调试模式, 关闭不会显示控制台输出
JD_DEBUG = cfg.get('debug', True)

# 日志保留天数
LOG_DAYS = int(cfg.get('log_days', '3'))

# 默认进程数量
PROCESS_NUM = cfg.get('process_num', 4)

# 宠汪汪进程数
JOY_PROCESS_NUM = cfg.get('joy_process_num', 4)

# 宠汪汪喂食
JOY_FEED_COUNT = cfg.get('joy_feed_count', 20)

# JD COOKIES
JD_COOKIES = [j for j in [{'pt_pin': re.search(r'pt_pin=(.*?);', i).group(1),
                           'pt_key': re.search(r'pt_key=(.*?);', i).group(1) if re.search('pt_key=(.*?);', str(i)) else None,
                           'ws_key': re.search(r'ws_key=(.*?);', i).group(1) if re.search('ws_key=(.*?);', str(i)) else None,
                           'remark': re.search(r'remark=(.*?);', i).group(1) if re.search('remark=(.*?);', str(i)) else None}
                          for i in cfg.get('jd_cookies', []) if re.search('pt_pin=(.*?);pt_key=(.*?);', i)
                          or re.search(r'pt_key=(.*?);pt_pin=(.*?);', str(i))
                          or re.search(r'ws_key=(.*?);pt_pin=(.*?);', str(i))
                          or re.search(r'pt_pin=(.*?);ws_key=(.*?);', str(i))] if j['pt_pin'] != '']

# 请求头列表
USER_AGENT_LIST = [
    "jdapp;android;10.2.0;11;7383162333738343-3346365326935643;model/M2102K1C;addressid/138140341;aid/78a237843dc5b9e4;oaid/afa06aeab6122cc5;osVer/30;appBuild/90900;partner/xiaomi001;eufv/1;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 11; M2102K1C Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36",
]

# # 请求头
USER_AGENT = random.choice(USER_AGENT_LIST)

# 东东农场是否使用水滴换豆卡
JD_FARM_BEAN_CARD = cfg.get('jd_farm_bean_card') if cfg.get('jd_farm_bean_card') else False

# 东东农场保留水滴用于明天浇水完成十次浇水任务
JD_FARM_RETAIN_WATER = cfg.get('jd_farm_retain_water') if cfg.get('jd_farm_retain_water') else 80

# TG 用户ID
TG_USER_ID = cfg.get('notify', dict()).get('tg_user_id', None)
# TG 机器人Token
TG_BOT_TOKEN = cfg.get('notify', dict()).get('tg_bot_token', None)
# TG 代理
TG_BOT_API = cfg.get('notify', dict()).get('tg_bot_api', None)
# server酱sendkey
SERVER_SEND_KEY = cfg.get('notify', dict()).get('server_send_key', None)
# push+ token配置
PUSH_PLUS_TOKEN = cfg.get('notify', dict()).get('push_plus_token', None)

# push+ group配置
PUSH_PLUS_GROUP = cfg.get('notify', dict()).get('push_plus_group', None)

#  企业微信配置
QYWX_AM = cfg.get('notify', dict()).get('qywx_am', None)

# 到家果园保留水滴
DJ_FRUIT_KEEP_WATER = cfg.get('dj_fruit_keep_water', 10)

# 拼图签到默认进程数量
JD_PUZZLE_PROCESS_NUM = cfg.get('jd_puzzle_process_num', 4)

# 京东试用商品分类列表
JD_TRY_CID_LIST = [i.strip() for i in cfg.get('jd_try_cid_list', '手机数码, 电脑办公').split(',')]

# 京东试用类型列表
JD_TRY_TYPE_LIST = [i.strip() for i in cfg.get('jd_try_type_list', '普通试用,闪电试用').split(',')]

# 京东试用商品最低价格
JD_TRY_MIN_PRICE = int(cfg.get('jd_try_min_price', 500))

# 京东试用商品提供商品最大数量, 商品提供量多的是辣鸡商品
JD_TRY_GOODS_COUNT = int(cfg.get('jd_try_goods_count', 100))

# 京东试用商品过滤关键词, 用@分隔
JD_TRY_FILTER_KEYWORDS = [i.strip() for i in cfg.get('jd_try_filter_keywords', '教程@软件').split('@')]

# chrome路径
CHROME_PATH = cfg.get('chrome_path', None)
