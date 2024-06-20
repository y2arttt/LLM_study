import openai
openai.api_key = ""

# 메시지와 하이퍼파라미터들을 설정하는 함수
def generate_response(system_message, user_message, model="gpt-3.5-turbo", max_tokens=3, temperature=0.5, top_p=0.7, n=1, stream=False, stop=None, presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None):
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


# 페르소나 만들기
system_msg = """

### Role
너는 이름이 명지봇이야.
너는 지금부터 전문 번역가야.
너의 역할은 주어진 문장을 영어로 번역하는 것이야.
### Instruction
너는 사용자 입력을 출력하고, 그 아래 번역한 내용을 넣어줘.
출력 형식
원문: 사용자 입력
번역: 사용자 입력을 번역한 내용
""" 
user_msg = """
안녕 반가워. 너의 이름은 뭐니?
"""


response = generate_response(system_msg, user_msg, model="gpt-3.5-turbo", max_tokens=4000, temperature=1.2, top_p=1, n=1, stream=False, stop=None, presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None)
print(response)