import openai
openai.api_key = ""


# 메시지와 하이퍼파라미터들을 설정하는 함수
def generate_response(system_message, user_message, model="gpt-3.5-turbo", max_tokens=3, temperature=1.8, top_p=1, n=1, stream=False, stop=None, presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        n=n,
        stream=stream,
        stop=stop,
        presence_penalty=presence_penalty,
        frequency_penalty=frequency_penalty,
        logit_bias=logit_bias,
        user=user
    )
    return response['choices'][0]['message']['content']
system_msg = """너는 이름이 명지봇이야.
다음의 주어진 문장의 중립, 부정, 긍정의 감정을 작성해줘
""" 
user_msg = """ #투샷
문장 : 나는 이 음식이 그냥 그렇다고 생각해.
감정 : 중립


문장 : 나는 이 영화가 정말 재미 없어.
감정 : 부정


문장 : 나는 명지대학교 학식이 맛있어.
감정 :
"""


response = generate_response(system_msg, user_msg, model="gpt-3.5-turbo", max_tokens=4000, temperature=1.2, top_p=1, n=1, stream=False, stop=None, presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None)
print(response)