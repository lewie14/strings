poem_title = "spring storm"
poem_author = "William Carlos Williams"
print("---------------------Title--------------------------------")
poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)
print("---------------------Upper--------------------------------")
poem_author_fixed = poem_author.upper()
print(poem_author)
print(poem_author_fixed)
print("---------------------Split--------------------------------")

line_one = "The sky has given over"

line_one_words = line_one.split()
# prints ['The', 'sky', 'has', 'given', 'over']
print(line_one_words)
print("-------------------split by comma----------------------------------")
authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

#prints all the names from a list
author_names = authors.split(",")
print(author_names)

#prints all the last names from the list
author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)

print("---------------------split--------------------------------")
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)

print("---------------------join--------------------------------")

reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

print("--------------------join on next line---------------------------------")
#You've been given a list, winter_trees_lines, that contains all the lines to 
#William Carlos Williams poem, Winter Trees. You've been asked to join together 
#the strings in the list together into a single string that can be used to 
#display the full poem. Name this string winter_trees_full.

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)

print("-------------------join - Strip out white space----------------------------------")
#Take the lines. Use strip on each individual line and save into a new
#list called love_maybe_line_stripped.
#join the lines into one multi line string to dispplay poem

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  print(love_maybe_lines_stripped)
  
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print()
print(love_maybe_full)
print("-------------------Replace----------------------------------")

#change the name Tomer to Toomer
toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')
print(toomer_bio_fixed)

print("---------------------Find--------------------------------")

god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)

print("---------------------Format--------------------------------")
def poem_title_card(poet, title):
  return "The poem \"{}\" is written by {}.".format(title, poet)
  
print(poem_title_card("Walt Whitman", "I Hear America Singing"))

print("---------------------Format--------------------------------")
#Keywords are used here to make sure the correct sentence if produce
#since the order of the arguments is different in the function definition
#to their places in the sentence

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title = title, original_work=original_work)
  return poem_desc

my_beard_description = poem_description("1974","Shel Silverstein","My Beard","Where the Sidewalk Ends" )
print(my_beard_description)
