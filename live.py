import pycurl
from io import BytesIO 
import json
from collections import namedtuple

import certifi


# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from pygame import mixer  # Load the popular external library
import playsound as ps
import threading

# This module is imported so that we can  
# play the converted audio 
import os 

mySaveText  =''
def printit():
    global mySaveText 
    # tạo thread chạy 10s 1 lần
    threading.Timer(10.0, printit).start()
    
    iDpost = 'ID của post cần đọc cmt - thường là live' # kiểm tra link live và post ID ra đây
    accToken = 'Token facebook appp'  # tạo 1 facebook app và lấy token access vào page.

    b_obj = BytesIO() 
    crl = pycurl.Curl() 

    crl.setopt(pycurl.CAINFO, certifi.where())

    # Set URL value
    crl.setopt(crl.URL, 'https://graph.facebook.com/v7.0/'+ iDpost + '/comments?limit=1&order=reverse_chronological&access_token='+ accToken)



    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)

    # Perform a file transfer 
    crl.perform() 

    # End curl session
    crl.close()

    # Get the content stored in the BytesIO object (in byte characters) 
    get_body = b_obj.getvalue()

    # Decode the bytes stored in get_body to HTML and print the result 
    #print('Output of GET request:\n%s' % get_body.decode('unicode-escape')) 

    x = json.loads(get_body.decode('unicode-escape'))
    y = x['data']
    z = y[0]
    print(z)
    print(z['from']['name']  + ' đã nói ' +z['message'])
    print(z['message'])



    # The text that you want to convert to audio 
    mytext = z['from']['name']  + ' đã nói ' +z['message']

    # Language in which you want to convert 
    language = 'vi'

    # Passing the text and language to the engine,  
    # here we have marked slow=False. Which tells  
    # the module that the converted audio should  
    # have a high speed 
    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save("chigoogle.mp3") 

    # Playing the converted file 

    if mytext != mySaveText:
        print('save text ne: ' + mySaveText)
        ps.playsound("chigoogle.mp3", True)
        os.remove("chigoogle.mp3")
        mySaveText = mytext
        print('save text sau doc ne: ' + mySaveText)
    else :
        print('Trung comment truoc')


printit()


