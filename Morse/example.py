from morse import *

user_input = input("Enter String: ")

# Create Instance Of Morse Class ( You Can Pass A Custom Alphabet As A Dictionary Here. )
instance = Morse()
converted_to_morse_text = instance(user_input)  # Call Morse Function

############################
####     Real Morse     ####
print(instance.raw_morse)  #
####     Real Morse     ####
############################

###################################################################
# A Morse With Escaped chars That Can Be Recovered With This Code #
print(instance.last_morse)                                        #
# A Morse With Escaped chars That Can Be Recovered With This Code #
###################################################################

recovered_from_morse_text = instance(
    converted_to_morse_text, mode=Mode.decrypt)  # Call Morse Function With Mode.decrypt ( unmorse )

print(recovered_from_morse_text)
