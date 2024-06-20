from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re


def convert_pdf_to_txt():
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open('law1.pdf', 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 999
    caching = True
    pagenos=set()


    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)


    text = retstr.getvalue()


    fp.close()
    device.close()
    retstr.close()
    return text


v = convert_pdf_to_txt()
print(v)
def preprocess_document(document):


    # 3. \n\n을 [para]로 변경
    # document = re.sub(r'법제처\s*\d+\s*국가법령정보센터\s*민법', '', document)
    # document = re.sub(r'법제처\s*\d+\s*국가법령정보센터\s', '', document)
    pattern = re.compile(r'\x0c')  # '\x0c'는 FORM FEED 문자를 나타냅니다.
    document = pattern.sub('', document)
   
    document = document.replace('           제', '[관]제')
    document = document.replace('         제', '[절]제')
    document = document.replace('       제', '[장]제')
    document = document.replace('     제', '[편]제')        
    document = document.replace('\n\n제', '[조]제')
    document = document.replace('\n제', '[조]제')
    document = document.replace('\n\n', ' ')
    document = document.replace('\n ', ' ')
         
    document = re.sub(r'법제처\s*.*', '', document)
   
    # 문서를 줄 단위로 분리
    lines = document.split('\n')
    # 각 줄의 가장 앞에 있는 '민법'이라는 단어를 삭제
    for i in range(len(lines)):
        lines[i] = re.sub(r'^\s*민법\s*', '', lines[i])  
    # 재결합
    document = '\n'.join(lines)
   
    document = document.replace(' \n', ' ')
    document = document.replace('[조]', '\n')    
    document = document.replace('\n제325조의', ' 제325조의')
    document = document.replace('[편]', '\n\n')
    document = document.replace('[장]', '\n\n\n')
    document = document.replace('[절]', '\n\n\n\n')
    document = document.replace('[관]', '\n\n\n\n\n')
   
    # 라인별 분리
    lines = document.split('\n')
    # 정규표현식을 사용하여 '제X조'로 시작하는 부분을 '[조]제X조'로 변경
    for i in range(len(lines)):
        lines[i] = re.sub(r'^(제\d+조)', r'[조]\1', lines[i])
        lines[i] = re.sub(r'^(제\d+편)', r'[편]\1', lines[i])
        lines[i] = re.sub(r'^(제\d+장)', r'[장]\1', lines[i])
        lines[i] = re.sub(r'^(제\d+절)', r'[절]\1', lines[i])
        lines[i] = re.sub(r'^(제\d+관)', r'[관]\1', lines[i])
    # 다시 결합
    document = '\n'.join(lines)    
   
    document = document.replace('\n제', ' 제')    
    document = document.replace('[조]', '')    
    document = document.replace('[편]', '')
    document = document.replace('[장]', '')
    document = document.replace('[절]', '')
    document = document.replace('[관]', '')
    return document    


text = preprocess_document(v)
print(text)


with open('law1.txt', 'w', encoding='utf-8') as file:
    file.write(text)


print("law1.txt에 성공적으로 저장되었습니다.")