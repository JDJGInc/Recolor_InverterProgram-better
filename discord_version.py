    #this code goes under a command
    
    ##the first digits like 8(refer to N64 usually, the only color bit is the 4 digits on the right.... - we still need to reinsert them imnto memory)

    #explained to me by: https://www.youtube.com/watch?v=5lZ31AlgNzw

    complete_color_code = message.content.split(" ",2)[-1]

    #Insert your color code into complete_color_code(make sure it's still with """ on both sides a.k.a 3 ") - default one is SMG3's Color Code - must be a complete color code with all the hat information, etc. not an uncomplete one(so yes, it needs values, that you wouldn't use normally.)

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

    useful_info = "all"+" "+str(x-times_ran_1)+" "+"of the color code lines ran!"

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

      inverting_results = ("Your color code was succesfully inverted")

      want_it = "yes"

      want_it2 = "yes"

    if not Inverted_color_code_inverted == lines:

      inverting_results = ("Color code Inverting failed....")

      want_it = "yes"

      want_it2 = "yes"

    
    required_info=useful_info+"\n"+inverting_results

    required_info99 = discord.Embed(title="Results",description=required_info)

    await message.channel.send(embed=required_info99)




    j = int(times_ran_1)

    test_string99 = ""


    if want_it == "yes":

      while j < len(Inverted_color_code):

        required_recolor_lines=Inverted_color_code[j]+"\n"

        test_string99 = test_string99+required_recolor_lines

        j = j + 1

      inverted_information=discord.Embed(title="Inverted Color Code:",description=test_string99)

      await message.channel.send(embed=inverted_information)

      

    jdjg = int(times_ran_1)

    if want_it2 == "yes":

      test_string = ""

      while jdjg < len(Inverted_color_code_inverted):

        useful_info = Inverted_color_code_inverted[jdjg]+"\n"

        test_string = test_string+useful_info

        jdjg = jdjg + 1

      values_needed=discord.Embed(title="Orginal Color Code that was inverted and was inverted back: ",description=test_string)

      await message.channel.send(embed=values_needed)

      good_file = int(times_ran_1)

      let_us_see=len(complete_color_code)

      orginal_color_code = complete_color_code[good_file:let_us_see]

      final_return=discord.Embed(title="Orginal color code:",description=orginal_color_code)

      await message.channel.send(embed=final_return)

    return