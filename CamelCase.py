# this program takes a users sentence and turns it into camel case
# keeps the first letter lowercase
print('Please enter a sentence in any sort of case! I will make it camel case for you!')
# takes the users input and makes all of it lowercase, and then
# capitalizes the first letter in each word
sentence = input().lower().title()
# checks to see if any letters are anything but letters
# displays warning for the user that the camel case may be incorrect
for char in sentence:
    if not char.isalpha():
        print('You will not get the desired camelCase since there are symbols!')
        input('But I shall print for you anyways... press enter')
        break
# replaces the spaces with no spaces to the words are put together
sentence = sentence.replace(' ', '')
# takes the first letter out and keeps the rest of the sentence
firstLetterGone = sentence[1:]
# then takes the first letter and lowercases it6
makeFirstLetterLower = sentence[0].lower()
# puts the lowercase first letter onto the sentenve again
fullSentence = makeFirstLetterLower + firstLetterGone
# displays the users sentence
print(fullSentence)
