from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds.")
from Body.Speak import speak
from Features.Clap import Tester
print(">> Starting The Jarvis : Wait For Few Seconds More")
from Main import maintaskexe
import whatsapp
def MainExecution():

    speak("Hello Sir")
    speak("I'm Jarvis, I'm Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data)

        valuereturn=maintaskexe(Data)
        if valuereturn==True:
            pass
        if len(Data)<3:
            pass
        
        elif "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)        
        else:
            Reply = ReplyBrain(Data)
            speak(Reply)

def ClapDetect():

    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()

# 10% 
