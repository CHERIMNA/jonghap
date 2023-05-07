import os
import sys
import urllib.request
import json
from google.cloud import translate_v2 as translate 
import requests
import openai


class TranslateByApi :
    
    def __init__(self, api , sourceLang , targetLang , text) :
        self.api = api 
        self.sourceLang = sourceLang
        self.targetLang = targetLang
        self.text = text 
   
    def translatePapago(self) :

        client_id = "e3OYwDXm_2XWrqMBwcYl" # 개발자센터에서 발급받은 Client ID 값
        client_secret = "" # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(self.text)
        data = "source="+ self.sourceLang+"&target=" + self.targetLang +"&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read().decode('utf-8')
            result = json.loads(response_body)
            translated_text = result['message']['result']['translatedText']
            #print(translated_text)
            return translated_text

        else:
            print("Error Code:" + rescode)

    def translateGoogle(self) :
        
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\taehee\Desktop\JongHap\fourth-arena-323500-6d674cca19f3.json'
        client = translate.Client()

        #text = 'Örvendek'
        text = self.text

        result = client.translate(text, target_language=self.targetLang,source_language= self.sourceLang)
        # print(result)
        # print(result['translatedText'])
        return result['translatedText']

    def translateKakao(self) : 
        # text = '안녕하세요'
        # source = 'kr'
        # target = 'en'

        text = self.text
        source = self.sourceLang
        target = self.targetLang
        
        url = 'https://dapi.kakao.com/v2/translation/translate'
        headers = {'Authorization': 'KakaoAK '}
        data = {'src_lang': source, 'target_lang': target, 'query': text}
        
        response = requests.post(url=url, headers=headers, data=data)
        
        if response.status_code == 200:
            result_tmp = response.json()['translated_text']
            result = ''
            for result_x in result_tmp:
                result += result_x[0]
                result += '\n'
            print(result)
            return result
        else:
            print(response)
            print('Error Code:' + str(response.status_code))

    def translateDeepL(self) :
        url = "https://deepl-translator.p.rapidapi.com/translate"

        payload = {
            "text": "This is a example text for translation.",
            "source": "EN",
            "target": "ZH"
        }
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "4c2f2d461emsh12db67afd36e355p11f400jsn7e0e6d9aead6",
            "X-RapidAPI-Host": "deepl-translator.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.json())

        return response.json()
    
    def translateGpt(self) : 
        openai.api_key = "sk-8DD....." # API Key
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": ""}]
        )

        print(completion)
        pass

       

    def translate(self) :
        if self.api == 'kakao' :
            return self.translateKakao()
        elif self.api == 'google' : 
            return self.translateGoogle()
        elif self.api == 'papago' : 
            return self.translatePapago()
        elif self.api == 'deepl' : 
            return self.translateDeepL()
        elif self.api == 'gpt' : 
            return self.translateDeepL()        



        