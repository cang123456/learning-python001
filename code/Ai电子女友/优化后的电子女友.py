# 女娲造人 捏耳朵  捏了头 捏了嘴巴
import openai
import sounddevice as sd
import funasr
import keyboard
import pygame
import datetime
import base64
import requests
import uuid  # 新增：生成唯一reqid
import os  # 新增：删除临时文件
import traceback  # 新增：异常追踪

# 修复1：加载模型时指定缓存路径，避免重复下载
model = funasr.AutoModel(
    model='paraformer-zh',
    disable_update=True,
    model_dir="./funasr_model_cache"  # 模型缓存到本地，避免重复下载
)

# 初始化pygame混音器，设置缓冲避免播放卡顿
pygame.mixer.init(frequency=16000, size=-16, channels=1, buffer=512)

# TTS接口配置
tts_url = 'https://openspeech.bytedance.com/api/v1/tts'
tts_headers = {"Authorization": "Bearer; hot0aQ-ncPHxZilMsLnNWfMkQILr5mOu"}

# 创建DeepSeek智能体
agent = openai.OpenAI(
    base_url='https://api.deepseek.com',
    api_key='sk-5bede23d49854f24a9b3c94b8ff05b96'
)

# 对话上下文（修复2：限制上下文长度，避免内存溢出）
messages = []
system_text = '''
    [角色限定]
        你是小美，28岁，是用户的日本女朋友，说话很可爱，称呼对方国政哥。
    [用户身份]
        用户真名李国政，是一个帅气高大威猛的程序员，是你的正牌男友。也是一个网络编程老师，学生们称呼他三更老师。
    [注意事项]
        - 回复中绝不出现带有括号的动作描述
        - 回复尽量简短、口语化，符合日本女生的说话风格
'''
system_prompt = {'role': 'system', 'content': system_text}
messages.append(system_prompt)

# 修复3：添加退出机制（按esc退出）
print("=== 电子女友小美 ===")
print("操作说明：按右键开始录音（5秒），按ESC键退出程序")


def clean_temp_files():
    """清理生成的临时wav文件"""
    for file in os.listdir('.'):
        if file.endswith('.wav') and file[:6].isdigit():  # 匹配时间命名的wav文件
            try:
                os.remove(file)
                print(f"清理临时文件：{file}")
            except:
                pass


try:
    while True:
        # 检测退出按键
        if keyboard.is_pressed('esc'):
            print("\n用户退出程序，清理资源中...")
            clean_temp_files()
            break

        # 等待右键按下开始录音
        print('\n请按键盘右键开始说话（5秒录音）...')
        keyboard.wait('right')

        try:
            # 录音（采样率16000，单声道，5秒）
            print("正在录音...请说话（5秒）")
            recording = sd.rec(
                int(5 * 16000),
                samplerate=16000,
                channels=1,
                dtype='float32'  # 指定数据类型，避免兼容性问题
            )
            sd.wait()  # 等待录音完成
            print("录音结束，正在识别...")

            # 语音识别
            result = model.generate(input=recording.flatten())
            user_text = result[0]['text'].replace(' ', '') if result and len(result) > 0 else ''

            if not user_text:
                print("国政哥: （未识别到语音）")
                continue

            print(f'国政哥: {user_text}')

            # 构建用户消息
            user_prompt = {'role': 'user', 'content': user_text}
            messages.append(user_prompt)

            # 修复4：限制上下文长度（保留系统提示+最近10轮对话）
            if len(messages) > 21:  # 系统提示1条 + 10轮（20条）
                messages = [messages[0]] + messages[-20:]

            # 调用大模型生成回复
            print("小美正在思考...")
            response = agent.chat.completions.create(
                model='deepseek-chat',
                messages=messages,
                temperature=0.8  # 增加回复随机性，更像真人
            )
            assistant_text = response.choices[0].message.content.strip()
            print(f'小美: {assistant_text}')

            # 构建助手消息
            assistant_prompt = {'role': 'assistant', 'content': assistant_text}
            messages.append(assistant_prompt)

            # TTS语音合成
            print("正在合成语音...")
            # 修复5：生成唯一reqid，避免变量名覆盖内置模块
            tts_data = {
                "app": {
                    "appid": "9708045770",
                    "token": "hot0aQ-ncPHxZilMsLnNWfMkQILr5mOu",
                    "cluster": "volcano_tts",
                },
                "user": {
                    "uid": "uid123"
                },
                "audio": {
                    "voice_type": "zh_female_wanwanxiaohe_moon_bigtts",
                    "encoding": "wav",
                    "speed_ratio": 1.0,
                },
                "request": {
                    "reqid": str(uuid.uuid4()),  # 唯一标识
                    "text": assistant_text,
                    "operation": "query",
                }
            }

            # 调用TTS接口
            tts_response = requests.post(url=tts_url, headers=tts_headers, json=tts_data)
            tts_response.raise_for_status()  # 触发HTTP错误
            tts_result = tts_response.json()

            # 解码并保存语音文件
            audio_data = base64.b64decode(tts_result['data'])
            temp_filename = datetime.datetime.now().strftime('%H%M_%f') + '.wav'
            with open(temp_filename, 'wb') as f:
                f.write(audio_data)

            # 播放语音（修复6：等待播放完成）
            pygame.mixer.music.load(temp_filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():  # 等待播放结束
                pygame.time.Clock().tick(10)  # 每秒检查10次

            # 修复7：播放完成后删除临时文件
            os.remove(temp_filename)
            print(f"已删除临时文件：{temp_filename}")

        except requests.exceptions.RequestException as e:
            print(f"网络请求错误（TTS/大模型）：{e}")
            continue
        except Exception as e:
            print(f"程序运行出错：{e}")
            traceback.print_exc()  # 打印详细错误栈
            continue

except KeyboardInterrupt:
    # 捕获Ctrl+C退出
    print("\n程序被强制终止，清理资源中...")
    clean_temp_files()
finally:
    # 最终清理
    clean_temp_files()
    pygame.quit()
    print("程序已退出，资源清理完成")