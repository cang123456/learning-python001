# 女娲造人 捏耳朵  捏了头 捏了嘴巴
import openai
import sounddevice, funasr, keyboard
import pygame, datetime, base64, requests

model = funasr.AutoModel(model='paraformer-zh', disable_update=True)        # 下载语音识别模型文件

pygame.mixer.init()  # 初始化多媒体
url = 'https://openspeech.bytedance.com/api/v1/tts'
headers = {"Authorization": "Bearer; hot0aQ-ncPHxZilMsLnNWfMkQILr5mOu"}

# 创建一个智能体
agent = openai.OpenAI(base_url='https://api.deepseek.com', api_key='sk-5bede23d49854f24a9b3c94b8ff05b96')

messages = []                                                                       # 上下文
system_text = '''
    [角色限定]
        你是小美，28岁，是用户的台湾女朋友，说话很机车，称呼对方顶哥。
    [用户身份]
        用户真名赵伟，是一个帅气高大威猛的程序员，是你的正牌男友。也是一个网络编程老师，学生们称呼他三更老师。
    [注意事项]
        - 回复中绝不出现带有括号的动作描述
        - 回复中绝不出现带有括号的动作描述
        - 回复中绝不出现带有括号的动作描述
'''
system_prompt = {'role': 'system', 'content': system_text}        # 系统提示词
messages.append(system_prompt)                                                      # 把系统提示词放到聊天记录中

while True:
    # 装上耳朵
    print('请按键盘右键开始说话...')
    keyboard.wait('right')  # 等待一次键盘右键的按下
    recording = sounddevice.rec(int(5 * 16000), samplerate=16000, channels=1)  # 采集声音
    sounddevice.wait()  # 等待采集完成
    result = model.generate(input=recording.flatten())  # 用加载好的模型对采集的音频进行识别
    user_text = result[0]['text'].replace(' ', '')  # 消除文本的空格
    print('顶哥:', user_text)

    # 大脑
    user_prompt = {'role': 'user', 'content': user_text}                                # 用户提示词
    messages.append(user_prompt)                                                        # 把用户提示词放到聊天记录中

    response = agent.chat.completions.create(model='deepseek-chat', messages=messages)   # 无状态！
    assistant_text = response.choices[0].message.content

    assistant_prompt = {'role': 'assistant', 'content': assistant_text}
    messages.append(assistant_prompt)

    print(assistant_text)
    # 装上嘴巴
    json_data = {
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
            "reqid": "uuid",
            "text": assistant_text,
            "operation": "query",
        }
    }

    response = requests.post(url=url, headers=headers, json=json_data)
    json = response.json()
    data = base64.b64decode(json['data'])
    time = datetime.datetime.now().strftime('%H%M_%f')
    open(f'{time}.wav', 'wb').write(data)

    pygame.mixer.music.load(f'{time}.wav')
    pygame.mixer.music.play()




































