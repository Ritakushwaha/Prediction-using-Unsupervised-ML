import random

Name_list = ['Pragya','Rita','Unmisha','Bhola','Sonakshi','Yogesh','Sachin Narayanan','Adarsh Dubey','Sai Kalyan Pola',
'Abhishek','Adarsh Poojari','Pramod Menon','Priyal','Amit','Dhruv','DJ','Nishant','Sameer Kesarkar','Naresh',
'Sowjanya','Ishan Bothra','Shubham Bose','Priya Kumari','Inderpreet','Sudha Kumari','Neha','Vamshi','Rajan','Surajnarayan',
'Sagar','Prachi','Piyush','Sachin Wagh','Ayushi Bajpai','Sarupya','Anubha','Harish','Aman','Siddharth','Charishma',
'Praveen','Mehar','Silpa','Bhavani','Shibil','Akansha','Srikanth Venanka','Srikanth Arroju', 'Vishal', 'Surabhi']

task_list = ['Tongue Twister :\nचांदनी रात में चार चुड़ैल चुर्की पकड़ कर चुटुर चुटुर चना चबाये\nRepeat 5 times',
             'Never Have I Ever?',
             'Tongue Twister :\nBlack background, brown background\n Repeat 5 times',
             'Mimicry of the Next Person',
             'Tongue Twister :\nBetty bought some butter, but the butter was bitter,\n so betty bought some better butter to make the bitter butter better\nRepeat 5 times.',
             'Acting -  Shahrukh Khan or Rajnikanth',
             'Tongue Twister :\nसमझ समझ के समझ को समझो, समझ समझना भी एक समझ है\nसमझ समझ के जो ना समझे मेरी समझ में वो ना समझ है\nRepeat 5 times',
             'Guess the movie name:\nRishte me hum tumahre baap lagate hai, Naam hai ShahenShah',
             'Complete the Dailogue from Gadar - Ek Prem Katha:\nTumhara Pakistan jindabad hai isse hume koi.... ',
             'Guess the movie name :\nIf you think you are Bad, I am your Dad',
             '(a^3 - b^3) = ?',
             'Guess the personality',
             'First programming language',
             'Tell any jokes',
             'Most funny moment in Project',
             'Name the seven continents',
             'Finland Prime Minister Name',
             'Act like Narendra Modi',
             'Formula - Volume of cylinder',
             'Alphabets in your native language',
             'Poem other than - Twinkle Twinkle',
             "India's Current President",
             "Find Difference between two pictures\nYou have 50 seconds."]

def display_name():
  while len(Name_list)>0:
      name = random.choice(Name_list)
      Name_list.remove(name)
      return name


def display_task():
    while len(task_list) > 0:
        task = random.choice(task_list)
        return task
