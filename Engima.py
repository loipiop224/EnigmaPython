
import string
import random

# Define the rotors and their wiring configurations
#A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor_4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor_5 = "VZBRGITYUPSDNHLXAWMJQOFECK"

english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Define the reflector wiring configuration
reflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflectorA = "EJMZALYXVBWFCRQUONTSPIKHGD"
reflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"

changed = True


# Define the Enigma machine class
class Enigma:

  def __init__(self):

    #Setting up the rotor's default setting
    self.rotors = ["", "", ""]
    self.positions = [0, 0, 0]
    self.rotor_1_default = (rotor_1, 0, 0)
    self.rotor_2_default = (rotor_2, 0, 1)
    self.rotor_3_default = (rotor_3, 0, 2)
    self.reflector_default = (reflectorA)

 
    

    self.plugboard_default = {
      'A': 'B',
      'C': 'D',
      'E': 'F',
      'G': 'H',
      'I': 'J',
      'K': 'L',
      'M': 'N',
      'O': 'P',
      'Q': 'R',
      'S': 'T',
      'U': 'V',
      'W': 'X',
      'Y': 'Z',
      'B': 'A',
      'D': 'C',
      'F': 'E',
      'H': 'G',
      'J': 'I',
      'L': 'K',
      'N': 'M',
      'P': 'O',
      'R': 'Q',
      'T': 'S',
      'V': 'U',
      'X': 'W',
      'Z': 'Y'
    }

    self.setting_list = [
      self.rotor_1_default, self.rotor_2_default, self.rotor_3_default,
      self.reflector_default,
    self.plugboard_default
    ]

  def change_rotor(self, rotor, position, order):

    self.rotors[order - 1] = rotor
    self.positions[order - 1] = position
  

  def set_plugboard(self, plugboard):
    self.plugboard = plugboard

  def change_default_setting(self):
    self.setting_list[0] = (self.rotors[0], 0,self.positions[0])
    self.setting_list[1] = (self.rotors[1], 1,self.positions[1])
    self.setting_list[2] = (self.rotors[2], 2,self.positions[2])
    self.setting_list[3] = self.reflector
    self.setting_list[4] = self.plugboard

  def set_reflector(self, reflector):
    self.reflector = reflector

  def setting_plugboard(self):
    english_alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(
    )
    pairing_dictionary2 = {}
    pairing_dictionary_list = []
    pairing_dictionary_machine = {}
    final_dictionary = {}
    initial_list_pairing = english_alphabet.copy()
    while len(initial_list_pairing) > 0:

      other_pair = ""
      while other_pair.upper() not in initial_list_pairing:
        print("Remaining digit:{}".format(initial_list_pairing))
        print(initial_list_pairing[0])
        other_pair = input("Pair:")
      pairing_dictionary_machine[initial_list_pairing[0]] = other_pair.upper()

      if other_pair.upper() == initial_list_pairing[0]:
        initial_list_pairing.remove(initial_list_pairing[0])
      else:
        initial_list_pairing.remove(initial_list_pairing[0])
        initial_list_pairing.remove(other_pair.upper())

    for i, j in pairing_dictionary_machine.items():
      pairing_dictionary2[j] = i
    pairing_dictionary_list.append(pairing_dictionary_machine)
    pairing_dictionary_list.append(pairing_dictionary2)
    print(pairing_dictionary_list)
    final_dictionary = pairing_dictionary_list[0]
    final_dictionary.update(pairing_dictionary_list[1])
    print("Final plugboard:")
    print(final_dictionary)

    self.set_plugboard(final_dictionary)

  def reset_machine(self):
    rotor1_setting = self.setting_list[0]
    rotor2_setting = self.setting_list[1]
    rotor3_setting = self.setting_list[2]
    reflector_setting =  self.setting_list[3]
    plugboard_setting = self.setting_list[4]
    self.change_rotor(rotor1_setting[0],rotor1_setting[1],rotor1_setting[2])
    self.change_rotor(rotor2_setting[0],rotor2_setting[1],rotor2_setting[2])
    self.change_rotor(rotor3_setting[0],rotor3_setting[1],rotor3_setting[2])
    self.set_reflector(reflector_setting)
    self.set_plugboard(plugboard_setting)
    
  def process_position(self, position):
    if position >= 26:
      return 0
    elif position <= -1:
      return 25
    else:
      return position

  def plugboard_swap(self, letter):
    return self.plugboard[letter]

  def shift_rotor(self):
    for i in range(0, 2):
      self.rotors[i] = self.rotors[i][self.positions[i]::] + self.rotors[i][
        0:self.positions[i]]

  def encrypt(self, message):
    # Convert the message to uppercase and remove any spaces or punctuation
    message = message.upper()

    # Encrypt each letter of the message using the Enigma machine
    ciphertext = ""
    for letter in message:
      if letter in english_alphabet:

        #Swap letter through plugboard
        letter = self.plugboard_swap(letter)

        # Encrypt the letter

        input_letter = english_alphabet.index(letter)
        for i in range(3):

          rotor_output = self.rotors[i][self.process_position(input_letter)]
          input_letter = self.process_position(
            english_alphabet.index(rotor_output))

        #Channel Through the reflector
        output_letter = self.reflector[self.process_position(input_letter)]

        for i in range(2, -1, -1):
          input_letter = self.rotors[i].index(output_letter)
          output_letter = english_alphabet[self.process_position(input_letter)]

        #Put through one final plugboard shuffle

        ciphertext += self.plugboard_swap(output_letter)

        self.positions[0] += 1
        if self.positions[0] == 26:
          self.positions[0] = 0
          self.positions[1] += 1
        if self.positions[1] == 26:
          self.positions[1] = 0
          self.positions[2] += 1
        if self.positions[2] == 26:
          self.positions[2] = 0
        self.shift_rotor()
        print("Current rotor positions:", self.positions)

        # Rotate the rotors
      else:
        ciphertext += letter
    return ciphertext


# Set the nachine to default setting
enigma = Enigma()
enigma.reset_machine()

print("Welcome to enigma machine  -Nhat Nguyen")
while True:

  print(
    "1. Encrypt/Decrypt text \n2.Change Machine's setting \n3.Reset machine \n4.Exit program"
  )
  option = int(input("Input:"))

  if (option == 1):
    message = input("Message to be encrypted:")
    print("Encrypted text: ", enigma.encrypt(message))

  elif (option == 2):
    current_setting = enigma.setting_list.copy()
    while (option != 5):
      print(
        "1.Change rotor \n2.Change reflector \n3.Replug the plugboard \n4.Save setting to default setting \n5.Go back"
      )

      option = int(input("Input:"))
      if (option == 1):
        print("Which order from 1-3?")
        order = int(input("Input:"))
        print("Which rotor from 1-5?")
        rotor = int(input("Input:"))

        if (rotor == 1):
          rotor = rotor_1
        elif (rotor == 2):
          rotor = rotor_2
        elif (rotor == 3):
          rotor = rotor_3
        elif (rotor == 3):
          rotor = rotor_3
        elif (rotor == 3):
          rotor = rotor_3
        else:
          print("Invalid choice, rotor 1 automatically choosed")
          rotor = rotor_1
        print("Which starting position from 1-26?")

        position = int(input("Input:")) - 1

        enigma.change_rotor(rotor, position, order)

      elif (option == 2):
        print(
          "There are multiple reflector: \n1.reflector A, \n2.reflector B, \n3.reflector C"
        )

        print("Choose one reflector from 1-3")
        input = int(input("Input:"))
        if (input == 1):
          reflector = reflectorA
        elif (input == 2):
          reflector = reflectorB
        elif (input == 3):
          reflector = reflectorC
        enigma.set_reflector(reflector)
      elif (option == 3):
        enigma.setting_plugboard()
      elif (option == 4):
        enigma.change_default_setting()
      elif (option == 5):
        break

  elif (option == 3):
    enigma.reset_machine()

    print("Machine resetted!")
  elif (option == 4):
    print("Exitting...")
    break
