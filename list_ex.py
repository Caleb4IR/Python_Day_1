scrambled_message = "world the save to time no is there"
#there is no time to save the world

words = scrambled_message.split()

correct_order = words[7], words[6], words[5], words[4], words[3], words[2], words[1], words[0]

correct_sentence = ' '.join(correct_order)

print(correct_sentence)

#Or
scrambled_list = scrambled_message.split(' ')
print(" ".join(scrambled_list[::-1]))
