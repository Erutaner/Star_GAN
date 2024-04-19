import cv2
import os

# 定义输入输出路径
input_folder = '/root/autodl-tmp/data/custom/label6'
output_folder = '/root/autodl-tmp/data/custom/label6/video'

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 准备图片文件名列表
images = [f"frame_{i}.jpg" for i in range(140)]
images = [img for img in images if os.path.isfile(os.path.join(input_folder, img))]

# 读取第一张图片以获取图片尺寸
frame = cv2.imread(os.path.join(input_folder, images[0]))
height, width, layers = frame.shape

# 设置视频编码器和输出视频的参数
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用mp4v编码器
output_video_path = os.path.join(output_folder, 'output_video_sad.mp4')
video = cv2.VideoWriter(output_video_path, fourcc, 30, (width, height))

# 逐张图片读取并添加到视频中
for image in images:
    video.write(cv2.imread(os.path.join(input_folder, image)))

# 释放视频写入器
video.release()

print(f"视频已保存为 {output_video_path}。")
