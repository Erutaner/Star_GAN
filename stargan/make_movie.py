from moviepy.editor import VideoFileClip, clips_array, TextClip, CompositeVideoClip
import os
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})


# 视频文件路径
video_folder = r"D:\桌面\武大本科期间文件\大三下文件\深度学习与强化学习\张几2021301041093作业视频代码"

# 视频文件名列表
video_files = ['original.mp4', 'angry.mp4', 'contemptuous.mp4', 'disgusted.mp4',
               'fearful.mp4', 'happy.mp4', 'sad.mp4', 'surprised.mp4']

# 统一的视频分辨率
target_resolution = (240, 320)

# 加载视频并添加标题
clips = []
for video_file in video_files:
    clip = VideoFileClip(os.path.join(video_folder, video_file)).resize(target_resolution)
    # 提取标题（去除.mp4）
    title = video_file.split('.')[0]
    # 创建文本clip
    txt_clip = TextClip(title, fontsize=24, color='white', bg_color='black')
    txt_clip = txt_clip.set_duration(clip.duration).set_position(("center", "top"))
    # 合并视频与文本
    video = CompositeVideoClip([clip, txt_clip])
    clips.append(video)

# 将clips数组组成2x4矩阵
final_clip = clips_array([[clips[0], clips[1], clips[2], clips[3],\
                          clips[4], clips[5], clips[6], clips[7]]])

# 输出视频路径
output_video_path = os.path.join(video_folder, 'combined_video.mp4')

# 写入文件
final_clip.write_videofile(output_video_path, codec='libx264')

print(f"合并后的视频已保存至 {output_video_path}。")