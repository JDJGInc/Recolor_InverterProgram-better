from os import system, name

# define our clear function 

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

#Thank you https://www.geeksforgeeks.org/clear-screen-python/

complete_color_code = """
8107EC40 0000
8107EC42 FF00
8107EC38 0000
8107EC3A FF00
8107ECA0 7306
8107ECA2 0000
8107EC98 3903
8107EC9A 0000
8107EC88 FEC1
8107EC8A 7900
8107EC80 7F60
8107EC82 3C00
8107EC58 FFFF
8107EC5A FF00
8107EC50 7F7F
8107EC52 7F00
8107EC28 0000
8107EC2A 0000
8107EC68 2F0E
8107EC6A 0700
8107EC20 0000
8107EC22 0000
8107EC70 721C
8107EC72 0E00"""



#Insert your color code into complete_color_code(make sure it's still with """ on both sides a.k.a 3 ") - default one is SMG3's Color Code - must be a complete color code with all the hat information, etc. not an uncomplete one(so yes, it needs values, that you wouldn't use normally.)

clear()

#function version: https://repl.it/@JDJGInc_Offical/InvertRecolorProgram-function#main.py

#the first digits like 8(refer to N64 usually, the only color bit is the 4 digits on the right.... - we still need to reinsert them imnto memory)

#explained to me by: https://www.youtube.com/watch?v=5lZ31AlgNzw



Inverted_color_code = [
  
]

Inverted_color_code_inverted = [
  
]

#here to check if both color codes match

lines=complete_color_code.split("\n")

times_ran_1 = 0


while times_ran_1 < len(lines):

  if '' == lines[times_ran_1]:

    times_ran_1 = times_ran_1+1

    Inverted_color_code.append('')

    Inverted_color_code_inverted.append('')

    #it should always be correct, unless the hexcode doesn't work, right

  if not '' == lines[times_ran_1]:

    break

x = int(times_ran_1)

times_ran_program_1 = 0

#to check to make sure it doesn't go over, and sees if the first slot has a blank spot or not(and finds the first one, without a blank spot)


while x < len(lines):

  color_value = lines[x]

  color_value2 = lines[x+1]

  colored_bit=color_value.split(" ")

  colored_bit2 = color_value2.split(" ")

  color_code_front = colored_bit[0]

  color_code_front2 = colored_bit2[0]

  color_section = colored_bit[1]

  color_section2 = colored_bit2[1]


  r = int(color_section[0:2], 16)
  g = int(color_section[2:4], 16)
  b = int(color_section2[0:2], 16)

  r = 0xFF - r
  g = 0xFF - g
  b = 0xFF - b

  #solution suggested by John10v10#5883

  bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

  first_color_line =  bits_used998[0:4].upper()

  second_color_line = bits_used998[4:6].upper()

  color_code_needed = color_code_front+" "+first_color_line

  color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]

  Inverted_color_code.append(color_code_needed)

  Inverted_color_code.append(color_code_needed_2)

  x = x +2

  times_ran_program_1 = times_ran_program_1 + 1

print("all",x-times_ran_1,"of the color code lines ran!")

times_ran_1 = 0


while times_ran_1 < len(Inverted_color_code):

  if '' == Inverted_color_code[times_ran_1]:

    times_ran_1 = times_ran_1+1

  if not '' == Inverted_color_code[times_ran_1]:

    break

z = int(times_ran_1)

while z < len(Inverted_color_code):

  color_value = Inverted_color_code[z]

  color_value2 = Inverted_color_code[z+1]

  colored_bit=color_value.split(" ")

  colored_bit2 = color_value2.split(" ")

  color_code_front = colored_bit[0]

  color_code_front2 = colored_bit2[0]

  color_section = colored_bit[1]

  color_section2 = colored_bit2[1]


  r = int(color_section[0:2], 16)
  g = int(color_section[2:4], 16)
  b = int(color_section2[0:2], 16)

  r = 0xFF - r
  g = 0xFF - g
  b = 0xFF - b

  #solution suggested by John10v10#5883

  bits_used998 = f"{r:0{2}x}{g:0{2}x}{b:0{2}x}"

  first_color_line =  bits_used998[0:4].upper()

  second_color_line = bits_used998[4:6].upper()

  color_code_needed = color_code_front+" "+first_color_line

  color_code_needed_2 = color_code_front2+" "+second_color_line+color_section2[2:4]

  Inverted_color_code_inverted.append(color_code_needed)

  Inverted_color_code_inverted.append(color_code_needed_2)

  z = z +2


if Inverted_color_code_inverted == lines:

  print("\nYour color code was succesfully inverted")

  want_it = "yes"

  want_it2 = "yes"

if not Inverted_color_code_inverted == lines:

  print("\nColor failed....")

  want_it = "yes"

  want_it2 = "yes"




j = int(times_ran_1)

test_string99 = ""


if want_it == "yes":

  print("\nInverted Color Code:")


  while j < len(Inverted_color_code):

    test_string99 = test_string99+(Inverted_color_code[j]+"\n")


    j = j + 1

  print(test_string99)

jdjg = int(times_ran_1)

if want_it2 == "yes":

  print("\nOrginal Color Code that was inverted and was inverted back: ")

  test_string = ""

  while jdjg < len(Inverted_color_code_inverted):

    test_string = test_string+(Inverted_color_code_inverted[jdjg]+"\n")

    jdjg = jdjg + 1

  print(test_string)

  print("\nOrginal color code:")



jdjg_2 = times_ran_1

test_string998 = ""

while jdjg_2 < len(lines):

  test_string998 = test_string998+(lines[jdjg_2]+"\n")

  jdjg_2 = jdjg_2 + 1

print(test_string998)

if test_string == test_string998:

  print("\n run 100% succesfully")

if not test_string == test_string998:

  print("\n didn't run successfully")




#Old inverters(don't work as well):

#https://repl.it/@JDJGInc_Offical/RecolorInverter#main.py

#https://repl.it/@JDJGInc_Offical/RecolorInverter-optimized

while True:

  input("\n press any button to close this window")

  break
