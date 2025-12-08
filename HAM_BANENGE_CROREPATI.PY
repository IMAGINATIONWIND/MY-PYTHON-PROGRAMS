
import time

print("Namaskar! Main hoon Amitabh Bachchan, aur aapka swagat karta hoon aaj ke Kaun Banega Crorepati mein\n")
print("To kya suru kiya jaaye?\n")

a = input("A. Haan B. Nahi kripya jawab dein:    \n")

if a == "A":
    print("Toh chaliye shuru karte hain\n")
    print("ye raha apki dhan rashi ka road map\n")
    
    
    def dhanrashi():
     t = 1
     for i in range(1, 9):
        
        t=t*10 
        print("Question", i)
        print("₹",t)
    dhanrashi()
    
    def countdown_timer(seconds):
       while seconds:
         mins, secs = divmod(seconds, 60)
         timer = '{:02d}:{:02d}'.format(mins, secs)
         print(timer, end="\r")
         time.sleep(1)
         seconds -= 1

       print("Timer finished!")

    def prizemoney(integer):
    
     if integer == 0:
         print("aapko milte hain 1000 rupees\n")
     else:
          a = 0
          a = 10**integer
          return a

    def question(n):
     listofquestions = ["Question 1: What is the capital of India ?" ,"Question 2:  What is the capital city of France?" ,"Question 3:  Which famous French landmark is known for its iron lattice structure? ","Question 4:  Which French painter is famous for his Water Lilies series ? ","Question 5:  Which French pastry is a flaky, buttery delight often eaten for breakfast?" ,"Question 6: What is the name of the French national anthem?" ," Question 7 : Which famous French fashion designer is known for the creation of the little black dress " ," Question 8 : Which French region is known for its wine production?"]
     listofoptions = ["A. Mumbai B. Delhi C. Kolkata D. Chennai "," A. Paris B. London C. Berlin D. Rome" ," A. Eiffel Tower B. Big Ben C. Statue of Liberty D. Sydney Opera House ", "A. Claude Monet B. Vincent Van Gogh C. Pablo Picasso D. Leonardo Da Vinci "," A. Croissant B. Macaron C. Eclair D. Mille-feuille "," A. La Marseillaise B. God Save the Queen C. The Star-Spangled Banner D. O Canada" ," A. Yves Saint Laurent B. Coco Chanel C. Christian Dior D. Karl Lagerfeld" ," A. Provence B. Normandy C. Brittany D. Alsace"]
     listofanswers = ["B","A","A","A","A","A","B","A"]
    
     print("Toh ye raha apka swaal\n")
     print(listofquestions[n-1])
     print("you have 30 seconds to think about the answer of the question and your time starts now\n")
     print(listofoptions[n-1])
     countdown_timer(30)
     print("to answer the question, type the option\n")
     answer = input("Enter your answer: ")
     
     def abhitakki_dhanrashi(n):
        if n == 0:
            return 1000
        else:
         a = 10
         r = 10
         Z= a * (1 - r**n) / (1 - r)
        
        return Z
        print(Z)
     
     if answer == listofanswers[n-1]:
         print("Congratulations! Aapka jawab sahi hai\n")
         print("aap jeet chuke hain",prizemoney(n),"rupees\n")
         print("aapka prize money abhi tak hai",abhitakki_dhanrashi(n),"rupees\n")
         print("taalliiyyaa\n")
         print("Chaliye aage badhte hain\n")
         print("ye raha aapka agla sawaal\n")
         n = n+1
         question(n)
     else:
        print("Aapka answer galat hai\n")
        print("aap ghar lekar jaa rahe hain ",abhitakki_dhanrashi(n-1),"rupees\n")
        exit()
    def startgame():
        n = 1
        question(n)
    startgame()

elif (a == "B"):
    print("OK , to hum aapka wait kar rahe hain")
    exit()

