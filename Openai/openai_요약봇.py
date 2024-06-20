import openai
openai.api_key = "  "


# 메시지와 하이퍼파라미터들을 설정하는 함수
def generate_response(system_message, user_message, model="gpt-3.5-turbo", max_tokens=5500, temperature=0, top_p=1, n=1, stream=False, stop=None, presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None):
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


# 예시 사용법
system_msg = """

### Instruction
너는 편집자야
너는 텍스트의 내용을 제목을 제외한 모든 문단을 분석하고 요약 해서 JSON형식으로 저장해야 해
형식은 아래와 같아
key:문단, value:요약 내용
예시
"문단1": "인공지능의 발전은 직업과 소득 구조에 큰 변화를 일으키고 있으며, 이로 인해 노동 시장의 재편이 일어나고 있음"

Lets`s think step by step
"""
text = """
#텍스트
인공지능의 발전과 직업 및 소득의 변화

인공지능(AI)의 발전은 직업과 소득 구조에 큰 변화를 일으키고 있습니다. 노동 시장의 재편은 직업의 성격과 소득 분포에 심대한 영향을 미치고 있습니다. 본 에세이에서는 AI가 직업과 소득에 미치는 영향을 분석하고, 이에 대한 대응 방안을 제시하고자 합니다.

AI 기술의 발전으로 단순하고 반복적인 작업은 AI와 로봇에 의해 대체되고 있습니다. 제조업, 물류, 서비스 업종에서 로봇이 인간의 노동을 대신하며, 이는 해당 분야의 일자리 감소로 이어지고 있습니다.

그러나 AI는 새로운 직업 기회도 창출합니다. 데이터 과학자, 머신러닝 엔지니어 등의 직업이 생겨났으며, 자율주행차, 스마트 헬스케어 등 AI 기술을 활용한 새로운 산업에서도 많은 일자리가 창출되고 있습니다. 이러한 변화는 직업의 재교육과 전환을 필요로 하며, 새로운 기술 습득의 중요성이 커지고 있습니다.

AI 도입은 소득 분포에도 큰 변화를 초래합니다. 고도로 숙련된 기술직의 수요 증가로 이들 직업의 소득은 상승하고 있지만, 자동화로 대체 가능한 직업에 종사하던 노동자들은 실직하거나 낮은 임금을 받게 되어 소득 불균형이 심화될 수 있습니다.
또한 AI 기업의 부상으로 일부 기업가와 투자자들은 막대한 수익을 올리고 있습니다. 이로 인해 상위 1%의 소득이 증가하고, 중산층과 하위 계층의 소득은 상대적으로 정체되거나 감소하는 양상을 보이고 있습니다. 이러한 소득 불균형은 사회적 불안정성을 초래할 수 있으며, 이에 대한 대책 마련이 중요합니다.

AI의 발전에 따른 직업과 소득의 변화에 대응하기 위해 몇 가지 중요한 방안이 필요합니다. 첫째, 교육과 재교육 프로그램을 강화해야 합니다. 빠르게 변화하는 기술 환경에 적응하기 위해서는 지속적인 학습이 필요하며, 정부와 기업은 이를 지원하는 체계를 구축해야 합니다.
둘째, 사회 안전망을 강화해야 합니다. 일자리 변동성과 불확실성이 증가하는 시대에 실직자와 저소득층을 보호하기 위한 사회 안전망이 필수적입니다. 기본소득제 도입, 실업보험 강화, 직업 재교육 지원 등의 방안을 고려할 수 있습니다.
셋째, 소득 불균형을 해소하기 위한 정책이 필요합니다. 세금 정책을 통해 고소득층과 기업의 이익을 공정하게 분배하고, 중산층과 저소득층의 소득을 증대시키는 방안을 마련해야 합니다. 또한 기업은 사회적 책임을 다하고 공정한 노동 환경을 조성해야 합니다.

인공지능의 발전은 직업과 소득 구조에 큰 변화를 초래하고 있습니다. 자동화와 새로운 기술의 도입으로 일부 직업은 사라지고, 새로운 직업이 생겨나며, 소득 불균형이 심화되고 있습니다. 이러한 변화에 효과적으로 대응하기 위해서는 교육과 재교육, 사회 안전망 강화, 소득 불균형 해소를 위한 정책이 필요합니다. AI 시대의 도래는 도전과 기회를 동시에 제공하며, 이를 잘 활용하는 것이 앞으로의 사회적 안정과 번영을 위한 열쇠가 될 것입니다.



"""


user_msg = f"""


{text}


"""


response = generate_response(system_msg, user_msg, model="gpt-3.5-turbo", max_tokens=500, temperature=0.5, top_p=1, n=1, stream=False, stop=None, presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None)
print(response)