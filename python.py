import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init
init(autoreset = True)

def print_loop():
    while True:
        print(Fore.GREEN + "Listening...",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)

def Translate_Hindi_To_English(text):
    english_text = translate(text,"en-us")
    return english_text

def speech_to_text_python():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_dumping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noice(source)
        
        while True:
            print(Fore.GREEN + "Listening...",end="",flush=True)

            # Now see use "try" because this saves as from error
            # Simply say if user doesn't speaks then there not should be any error 
            try:
                audio = recognizer.listen(source,timeout = None)  
                # if listening timeout happens dont do anything
                
                print("\r" + Fore.LIGHTBLUE_EX + "Recog..." , end="",flush= True)
                # "\r" removes privious mission and Fore.lightblue add colours 
                # and "reco..." prints and by end and flush code ends
                
                recognizer_text = recognizer.recognize_google_cloud(audio).lower()
                #processes recourded audio and convert it to text using google 
                #cloud speetch to text apl
                
                if recognizer_text():
                    trans_text = Translate_Hindi_To_English(recognizer_text)
                    print("\r" + Fore.BLUE + "Translated: " + trans_text)
                    return trans_text
                else:
                    return ""
            except sr.UnknownValueError:
                recognizer_text = ""

            finally:
                #In Python, the finally block is a special code block that is 
                #guaranteed to execute, regardless of whether an exception occurs
                #within a try block. It's often used to clean up resources, like 
                #closing files or database connections, ensuring that they are released
                #properly, even if an error happens.

                print("\r",end="",flush= True)
            
            os.system("cls" if os.name == "nt" else "clear")
            #Is used to clear the terminal
            #depending on the operating system. Here's an explanation:

            #The os module in Python provides a way to interact with the operating system
            
            #os.name is an attribute of the os module that gives you a string 
            #representing the operating system.

            #os.name == "nt": This is the condition being tested.
            #os.name returns the name of the operating system

            #"cls": This is the value returned if the condition is true

        stt_thread = threading.Thread(target = speech_to_text_python)
        #STT stands for Speech-to-Text
        #Threading in Python refers to the ability to run multiple 
        #parts of a program (threads) concurrently

        #Thread is a class in the threading module that represents a single thread 
        #of execution.

        print_thread = threading.Thread(target = print_loop)
        #Is used to create a new thread that will run the print_loop function 
        #concurrently with the main program or other threads.

        stt_thread.start()
        print_loop.start()

        stt_thread.join()
        print_loop.join()


speech_to_text_python()



        



                
        
            




    