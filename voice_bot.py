# import requests
# import speech_recognition as sr
# import pyttsx3 

# converter = pyttsx3.init() 
# converter.setProperty('rate', 150) 
# converter.setProperty('volume', 0.7) 
# voices = converter.getProperty('voices')
# converter.setProperty('voice', voices[1].id)
  
# rec = sr.Recognizer()

# bot_message = ""

# # define a function to convert speech to text
# def STT():
#     with sr.Microphone(device_index=0) as source:
#         print("Jarvis is Listening...")
#         message = rec.listen(source)
#     try:
#         query = rec.recognize_google(message, language="en-us")
#         print("You Said : {}".format(query))
#         return query # return the text from speech
#     except sr.UnknownValueError as e:
#         print("Could not understand audio: ", e)
#         return None # return None if speech is unintelligible
#     except sr.RequestError as e:
#         print("Could not request results: ", e)
#         return None # return None if request error occurs
#     except Exception as e:
#         print("Other error: ", e)
#         return None # return None for other errors

# def TTS(text):
#     engine = pyttsx3.init() # khởi tạo động cơ chuyển văn bản thành giọng nói
#     engine.say(text) # nói văn bản đã cho
#     engine.runAndWait() # chạy và đợi cho đến khi hoàn thành

# # Khởi tạo biến bot_message và message
# message = ""

# # Gửi yêu cầu POST đến webhook của rasa để nhận câu trả lời từ bot
# r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Xin chào"})

# # In ra câu trả lời của bot
# print("Bot nói, ", end=' ')
# for i in r.json():
#     bot_message = i['text']
#     print(f"{bot_message}")

# # Chuyển câu trả lời của bot thành giọng nói và lưu vào file welcome.mp3
# TTS(bot_message)
# print('Đã lưu')

# # Phát file âm thanh đã chuyển
# subprocess.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', "welcome.mp3", '--play-and-exit'])

# # Lặp lại cho đến khi bot hoặc người dùng nói "Tạm biệt" hoặc "Cảm ơn"
# while bot_message != "Tạm biệt" or bot_message != "Cảm ơn":

#     # Nhập văn bản từ bàn phím
#     message = input("Hãy nhập văn bản bạn muốn nói: ")
    
#     # Nếu không có văn bản được nhập, tiếp tục vòng lặp
#     if len(message) == 0:
#         continue
    
#     print("Đang gửi tin nhắn...")

#     # Gửi yêu cầu POST đến webhook của rasa để nhận câu trả lời từ bot
#     r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

#     # In ra câu trả lời của bot
#     print("Bot nói, ", end=' ')
#     for i in r.json():
#         bot_message = i['text']
#         print(f"{bot_message}")

#     # Chuyển câu trả lời của bot thành giọng nói và lưu vào file welcome.mp3
#     TTS(bot_message)
#     print('Đã lưu')

#     # Phát file âm thanh đã chuyển
#     subprocess.call(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', "welcome.mp3", '--play-and-exit'])
# define a function to convert text to speech
# def TTS(text):
#     if text: # check if text is not empty or None
#         converter.say(text) # say the text
#         converter.runAndWait() # wait until the speech is finished

# # use a while loop to keep listening and responding
# while(True):
#     query = STT() # call the STT function and assign the result to query
#     if query == "bye" or query == "exit": # check if the user wants to end the conversation
#         break # break out of the loop
#     elif query: # check if query is not None
#         r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message":query}) # send the query to Rasa server
#         for i in r.json():
#             print("Jarvis Said : {}".format(i['text'])) # print the response from Rasa
#             bot_message = i['text'] # assign the response to bot_message
#             TTS(bot_message) # call the TTS function with bot_message as argument
# Nhập các thư viện cần thiết
# Nhập các thư viện cần thiết
# import requests
# import speech_recognition as sr
# import pyttsx3 
# import threading
# from rasa_sdk import Action
# rec = sr.Recognizer()

# def STT():
#     with sr.Microphone(device_index=0) as source:
#         print("Jarvis is Listening...")
#         message = rec.listen(source)
#     try:
#         query = rec.recognize_google(message, language="en-us")
#         print("You Said : {}".format(query))
#         return query
#     except sr.UnknownValueError as e:
#         print("Could not understand audio: ", e)
#         return None
#     except sr.RequestError as e:
#         print("Could not request results: ", e)
#         return None
#     except Exception as e:
#         print("Other error: ", e)
#         return None

# def TTS(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def send_message(message):
#     global bot_message
#     r = requests.get('http://localhost:5165/model/parse', params={"text": message})
    
#     intent = r.json()["intent"]["name"]
    
#     print(f"Intent: {intent}")
    
#     TTS(intent)

# bot_message = ""
# message = ""

# send_message("hi")

# while bot_message != "bye" or bot_message != "thank":
#     message = STT()   
#     if message is None:
#         continue  
#     print("Sending...")
#     thread = threading.Thread(target=send_message, args=(message,))
#     thread.start()