# -*- coding: utf-8 -*-
"""
Author: BigCat
"""
import os

URL = "https://chart.cp.360.cn/kaijiang/ssq/"
path = "lotId=220051&chartType=undefined&spanType=3&span={}_{}&r=0.1195010473229372#roll_132"

BOLL_NAME = [
    ("红球", "red"),
    ("蓝球", "blue")
]

train_data_path = "data/"
train_data_file = "data.csv"

# 模型相关参数
windows_size = 3
batch_size = 1
sequence_len = 6
red_n_class = 33
red_epochs = 1
red_embedding_size = 32
red_hidden_size = 32
red_layer_size = 1
blue_n_class = 16
blue_epochs = 1
blue_embedding_size = 32
blue_hidden_size = 32
blue_layer_size = 1

# 模型训练参数
red_learning_rate = 0.001
red_beta1 = 0.9
red_beta2 = 0.999
red_epsilon = 1e-08
blue_learning_rate = 0.001
blue_beta1 = 0.9
blue_beta2 = 0.999
blue_epsilon = 1e-08

# 模型路径
model_path = os.getcwd() + "/model/"
red_ball_model_path = model_path + "/red_ball_model/"
blue_ball_model_path = model_path + "/blue_ball_model/"

# 模型名
pred_key_name = "key_name.json"
red_ball_model_name = "red_ball_model"
blue_ball_model_name = "blue_ball_model"
extension = "ckpt"

# 日志路径
log_path = os.getcwd() + "/log/"
access_log = log_path + "access.log"
error_log = log_path + "error.log"
