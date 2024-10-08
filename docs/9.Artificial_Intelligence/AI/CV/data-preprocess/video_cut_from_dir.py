import os
import threading
import webbrowser
from multiprocessing import cpu_count
from shutil import copy
import PySimpleGUI as sg
from moviepy.video.io.VideoFileClip import VideoFileClip
import argparse

# 视频切割：
# 使用命令
# python3 video_cut_from_dir.py --source ../../data/0001 --target ../../data/0001 --duration 5

stop = False

parser = argparse.ArgumentParser(description='')
parser.add_argument('--source', type=str, help='source path', required=True)
parser.add_argument('--target', type=str, help='target path', required=True)
parser.add_argument('--duration', type=int, help='duration', required=True)
args = parser.parse_args()

def subclips_from_dir(dir_path,new_dir,clip_duration):
    print('程序开始读入视频文件')
    # if not os.path.exists(values['SOURCE-DIR']):print('目录不存在');return
    if not os.path.exists(dir_path):print('目录不存在');return
    file_num,file_list,clip_duration = 0,[],int(clip_duration)

    for home, dirs, files in os.walk(dir_path):
        for file_name in files:
            file_list.append(os.path.join(home, file_name))
            file_num += 1

    print(f'已读取到{file_num}个文件。')
    for idx,all_file_name in enumerate(file_list,1):
        if stop:print('\n已终止处理！');return

        new_path_all = all_file_name.replace(dir_path,new_dir)
        new_path_dir,new_path_name = os.path.split(new_path_all)
        new_path_ext = os.path.splitext(new_path_name)[1]

        if not os.path.exists(new_path_dir):os.makedirs(new_path_dir)

        video = VideoFileClip(all_file_name)
        print(f'[{idx}/{file_num}]已读取视频： ' + all_file_name)

        video_duration = video.duration
        if video_duration<clip_duration:
            copy(all_file_name,new_path_all)
        else:
            for i in range(clip_duration,int(video_duration),clip_duration):
                write_path = new_path_all.replace(new_path_ext,f'_{i-clip_duration}_{i-1}' + new_path_ext)
                sub_video = video.subclip(i-clip_duration, i-1)
                try:
                    sub_video.write_videofile(write_path,threads=cpu_count()//2,audio_codec="aac")
                except:
                    print(write_path+'写文件时出现错误！！！')
                print('已切割： ' +write_path)

            if i<video_duration:
                write_path = new_path_all.replace(new_path_ext,f'_{i}_{video_duration}' + new_path_ext)
                video.subclip(i).write_videofile(write_path,threads=cpu_count()//2)
                print( '已切割： ' + write_path)
    print('\n已全部处理完成。')

if __name__ == "__main__":

    subclips_from_dir(args.source,args.target,args.duration)


    # def subclips_from_dir_thread(source,target,duration):
    #     threading.Thread(target=subclips_from_dir, args=(source,target,duration,), daemon=True).start()

    # sg.theme('DarkBrown4')
    # layout = [
    #           [sg.Text('视频文件夹（支持多级文件）:'), ],
    #             [sg.InputText(key='SOURCE-DIR',enable_events=True),sg.FolderBrowse('...',initial_folder=os.getcwd())],
    #           [sg.Text('存放目录:')],
    #             [sg.InputText(key='TARGET-DIR'), sg.FolderBrowse('...')],
    #           [sg.Text('切割时长:'),sg.InputText(size=(5,1),key='DURATION'),sg.Text('秒')],
    #           [sg.Button('开始切割'), sg.Button('停止切割'),sg.Button('退出程序'),sg.Text("Powered by ESword",enable_events=True,expand_x=True,justification='center')],
    #             [],

    # ]

    # window = sg.Window('视频批量分割器 V1.0', font='微软雅黑 15', layout=layout ,icon=ico)


    # while True:
    #     event, values = window.read()

    #     if event == sg.WIN_CLOSED or event == '退出':  # if user closes window or clicks cancel
    #         break
    #     elif event == '开始切割':
    #         if values['SOURCE-DIR'] and values['TARGET-DIR'] and str.isdigit(values['DURATION']) :
    #             stop = False
    #             subclips_from_dir_thread(values['SOURCE-DIR'],values['TARGET-DIR'],values['DURATION'])
    #         else:msg('请添加信息！！！')
    #     elif event == '停止切割':
    #         stop=True
    #     elif event =='SOURCE-DIR' and values[event]!='':
    #         new_dir = values[event]+'_clip'
    #         window['TARGET-DIR'].update(new_dir)
    #     elif event=='Powered by ESword':webbrowser.open('https://blog.csdn.net/Ejzq1')

    # window.close()
