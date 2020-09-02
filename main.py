import math
import clear_code

clear_code.clear()

#the first digits like 8(refer to N64 usually, the only color bit is the 4 digits on the right.... - we still need to reinsert them imnto memory)

#explained to me by: https://www.youtube.com/watch?v=5lZ31AlgNzw

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

Inverted_color_code = [

  "",
  
]

Inverted_color_code_inverted = [

  "",
  
]

#here to check if both color codes match

lines=complete_color_code.split("\n")

times_ran_1 = 0


while times_ran_1 < len(lines):

  if '' == lines[times_ran_1]:

    times_ran_1 = times_ran_1+1

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

  first_bit = color_section[0:1]

  second_bit = color_section[1:2]

  third_bit = color_section[2:3]

  fourth_bit = color_section[3:4]

  fifth_bit = color_section2[0:1]

  sixth_bit = color_section2[1:2]

  seventh_bit = color_section2[2:3]

  eighth_bit = color_section2[3:4]

  first_bit_16 = int(first_bit,16)

  second_bit_16 = int(second_bit,16)

  third_bit_16 = int(third_bit,16)

  fourth_bit_16 =  int(fourth_bit,16)

  fifth_bit_16 =  int(fifth_bit,16)
  
  sixth_bit_16 = int(sixth_bit,16)

  inverted_first_bit_16 = 255-int(first_bit_16)

  inverted_second_bit_16 = 255-int(second_bit_16)

  inverted_third_bit_16 = 255-int(third_bit_16)

  inverted_fourth_bit_16 = 255-int(fourth_bit_16)

  inverted_fifth_bit_16 = 255-int(fifth_bit_16)

  inverted_sixth_bit_16 = 255-int(sixth_bit_16)

  #now hex conversions will happen

  inverted_first_bit_16_hex = str(hex(inverted_first_bit_16))[3:4]

  inverted_second_bit_16_hex = str(hex(inverted_second_bit_16))[3:4]

  inverted_third_bit_16_hex = str(hex(inverted_third_bit_16))[3:4]
  
  inverted_fourth_bit_16_hex = str(hex(inverted_fourth_bit_16))[3:4]

  inverted_fifth_bit_16_hex = str(hex(inverted_fifth_bit_16 ))[3:4]

  inverted_sixth_bit_16_hex = str(hex(inverted_sixth_bit_16))[3:4]

  first_color_line = inverted_first_bit_16_hex.upper()+inverted_second_bit_16_hex.upper()+ inverted_third_bit_16_hex.upper()+inverted_fourth_bit_16_hex.upper()

  second_color_line = inverted_fifth_bit_16_hex.upper()+inverted_sixth_bit_16_hex+seventh_bit.upper()+eighth_bit.upper()

  color_code_needed = color_code_front+" "+first_color_line

  color_code_needed_2 = color_code_front2+" "+second_color_line

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

  first_bit = color_section[0:1]

  second_bit = color_section[1:2]

  third_bit = color_section[2:3]

  fourth_bit = color_section[3:4]

  fifth_bit = color_section2[0:1]

  sixth_bit = color_section2[1:2]

  seventh_bit = color_section2[2:3]

  eighth_bit = color_section2[3:4]

  first_bit_16 = int(first_bit,16)

  second_bit_16 = int(second_bit,16)

  third_bit_16 = int(third_bit,16)

  fourth_bit_16 =  int(fourth_bit,16)

  fifth_bit_16 =  int(fifth_bit,16)
  
  sixth_bit_16 = int(sixth_bit,16)

  inverted_first_bit_16 = 255-int(first_bit_16)

  inverted_second_bit_16 = 255-int(second_bit_16)

  inverted_third_bit_16 = 255-int(third_bit_16)

  inverted_fourth_bit_16 = 255-int(fourth_bit_16)

  inverted_fifth_bit_16 = 255-int(fifth_bit_16)

  inverted_sixth_bit_16 = 255-int(sixth_bit_16)

  #now hex conversions will happen

  inverted_first_bit_16_hex = str(hex(inverted_first_bit_16))[3:4]

  inverted_second_bit_16_hex = str(hex(inverted_second_bit_16))[3:4]

  inverted_third_bit_16_hex = str(hex(inverted_third_bit_16))[3:4]
  
  inverted_fourth_bit_16_hex = str(hex(inverted_fourth_bit_16))[3:4]

  inverted_fifth_bit_16_hex = str(hex(inverted_fifth_bit_16 ))[3:4]

  inverted_sixth_bit_16_hex = str(hex(inverted_sixth_bit_16))[3:4]

  first_color_line = inverted_first_bit_16_hex.upper()+inverted_second_bit_16_hex.upper()+ inverted_third_bit_16_hex.upper()+inverted_fourth_bit_16_hex.upper()

  second_color_line = inverted_fifth_bit_16_hex.upper()+inverted_sixth_bit_16_hex.upper()+seventh_bit.upper()+eighth_bit.upper()

  color_code_needed = color_code_front+" "+first_color_line

  color_code_needed_2 = color_code_front2+" "+second_color_line

  Inverted_color_code_inverted.append(color_code_needed)

  Inverted_color_code_inverted.append(color_code_needed_2)

  z = z +2


if Inverted_color_code_inverted == lines:

  print("\nYour color code was succesfully inverted")

  want_it = "yes"

  want_it2 = input("\nWant the orginal to test the difference?: ")

if not Inverted_color_code_inverted == lines:

  print("\nColor failed....")

  want_it = input("\n Want it anyway? (yes or no) - default is no: ")

  want_it2 = "yes"




j = 0


if want_it == "yes":

  print("\nInverted Color Code:")


  while j < len(Inverted_color_code):

    print(Inverted_color_code[j])

    j = j + 1

jdjg = 0

if want_it2 == "yes":

  print("\nOrginal Color that was inverted and was inverted back: ")

  while jdjg < len(Inverted_color_code_inverted):

    print(Inverted_color_code_inverted[jdjg])

    jdjg = jdjg + 1





#Old inverters(don't work as well):

#https://repl.it/@JDJGInc_Offical/RecolorInverter#main.py

#https://repl.it/@JDJGInc_Offical/RecolorInverter-optimized


