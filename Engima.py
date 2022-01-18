English_alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
print(English_alphabet)
pairing_dictionary2 = {}
pairing_dictionary_list = []
class rotor:
  def __init__(self,code,notch):
    self.rotor_code = []
    for i in code:
      self.rotor_code.append(i)
    self.notch = English_alphabet.index(notch)
global turn
turn = 0

def Rotorspecialist(number):
  if number > 26:
    return 1
  elif number < 1:
    return 26
  elif number >0 and number < 27:
    return number
#"EKMFLGDQVZNTOWYHXUSPAIBRCJ" 1 Q
#"AJDKSIRUXBLHWTMCQGZNPYFVOE" 2 V
#"BDFHJLCPRTXVZNYEIWGAKMUSQO"3 E
#"ESOVPZJAYQUIRHXLNFTGKDCMWB"4 J
#"VZBRGITYUPSDNHLXAWMJQOFECK"5 Z

def shiftcode(shiftlist,shift_input):
  shift = shift_input
  new_result = []
  for i in range(shift,len(shiftlist)):
    new_result.append(shiftlist[i])
  for i in range(0,shift):
    new_result.append(shiftlist[i])
  return new_result

rotor1 = rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ","Q")
rotor2 = rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE","V")
rotor3 = rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO","E")
rotor4 = rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB","J")
rotor5 = rotor("VZBRGITYUPSDNHLXAWMJQOFECK","Z")
print(rotor5.notch)
reflectorA = []
for i in "EJMZALYXVBWFCRQUONTSPIKHGD":
  reflectorA.append(i)
reflectorB = []
for i in "YRUHQSLDPXNGOKMIEBFZCWVJAT":
  reflectorB.append(i)
reflectorC = []
for i in "FVPJIAOYEDRZXWGCTKUQSBNMHL":
  reflectorC.append(i)

rotor_dictionary =  dict([(1,rotor1),(2,rotor2),(3,rotor3), (4,rotor4), (5,rotor5)])
reflector_dictionary = dict([(1,reflectorA),(2,reflectorB ),(3,reflectorC )])
#EJMZALYXVBWFCRQUONTSPIKHGD  reflector A
#YRUHQSLDPXNGOKMIEBFZCWVJAT reflector B
#FVPJIAOYEDRZXWGCTKUQSBNMHL reflector C

#setup the machine
pairing_dictionary_machine = {}

initial_list_pairing = English_alphabet.copy()
while len(initial_list_pairing) > 0:

  other_pair = ""
  while other_pair.upper() not in initial_list_pairing or other_pair.upper() == initial_list_pairing[0]:
    print("Remaining digit:{}".format(initial_list_pairing))
    print(initial_list_pairing[0])
    other_pair = input("Pair:")
  pairing_dictionary_machine[initial_list_pairing[0]] = other_pair.upper()
  initial_list_pairing.remove(initial_list_pairing[0])
  initial_list_pairing.remove(other_pair.upper())
for i, j in pairing_dictionary_machine.items():
  pairing_dictionary2[j] = i 
pairing_dictionary_list.append(pairing_dictionary_machine)
pairing_dictionary_list.append(pairing_dictionary2)
print(pairing_dictionary_list)

rotor_box = [1,2,3,4,5]
rotor_machine = []

for i in range(0,3):
  choice = 100
  while choice not in rotor_box:
    try:
      print("This is the rotor box{}, You can choose rotor to put into the machine".format(rotor_box))
      choice = int(input("Which rotor?"))
    except:
      print("Your choice is not valid")
  rotor_machine.append(choice)
  rotor_box.remove(choice)
print(rotor_machine)

print("There are multiple reflector: \n1.reflector A, \n2.reflector B, \n3.reflector C")
choice = 100
while choice < 1 or choice >3:
  try:
      choice = int(input("Which reflector?"))
  except:
      print("Your choice is not valid")
reflector_machine = choice

rotor_machine_pos = []
for i in range(0,3):
  choice == 100
  try:
      print("Choose initial position for rotor{}".format(i))
      choice = int(input("Input:"))
  except:
      print("Invalid choice")
  rotor_machine_pos.append(choice)

plain_text = input("Put your text here:")
for i in range(0,len(rotor_machine_pos)):
  rotor_machine_pos[i] = rotor_machine_pos[i] -1

def encryption(letter):
  rotor_dictionary_inuse = {}
  for i in range(0,3):
    rotor_dictionary_inuse[i] = rotor_dictionary[rotor_machine[i]]
    rotor_dictionary_inuse[i].rotor_code =  shiftcode(rotor_dictionary_inuse[i].rotor_code,rotor_machine_pos[i])

  letter2 = letter.upper()
  if letter2 in pairing_dictionary_list[0].keys():
    letter2 = pairing_dictionary_list[0][letter2]
  elif letter2 in pairing_dictionary_list[1].keys():
    letter2 = pairing_dictionary_list[1][letter2]

  for i in range(0,3):
    letter2 = rotor_dictionary_inuse[i].rotor_code[English_alphabet.index(letter2)]
  




  letter2  = reflector_dictionary[reflector_machine][English_alphabet.index(letter2)]
  
  for i in range(2,-1,-1):
    letter2 = English_alphabet[rotor_dictionary_inuse[i].rotor_code.index(letter2)]
   


  
    

 
    
  if letter2 in pairing_dictionary_list[0].keys():
    letter2 = pairing_dictionary_list[0][letter2]
  elif letter2 in pairing_dictionary_list[1].keys():
    letter2 = pairing_dictionary_list[1][letter2]



  rotor_machine_pos[0] = rotor_machine_pos[0]+1
  rotor_machine_pos[0] = Rotorspecialist(rotor_machine_pos[0])


  if Rotorspecialist(rotor_machine_pos[0] -1) == rotor_dictionary[rotor_machine[0]].notch :
      rotor_machine_pos[1] = rotor_machine_pos[1] +1
      rotor_machine_pos[1] = Rotorspecialist(rotor_machine_pos[1])

      if Rotorspecialist(rotor_machine_pos[1] -1) ==  rotor_dictionary[rotor_machine[1]].notch :
        rotor_machine_pos[2] = rotor_machine_pos[2] +1
        rotor_machine_pos[2] = Rotorspecialist(rotor_machine_pos[2])
  return letter2


  


encrypted_text = ""
plain_text = plain_text.upper()
for word in plain_text:
  if word not in English_alphabet:
    encrypted_text += word
  else:
    encrypted_text += encryption(word)
print("Encrypted text:{}".format(encrypted_text))


