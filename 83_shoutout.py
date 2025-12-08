import win32com.client

a= []
flag=0
while flag == False:
    x = input("enter the name : ")
    a.append(x)
    print('do you want to add one more name')
    t = input(" ").lower()
    if t == "yes": flag = False
    else : flag = True
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(a)
