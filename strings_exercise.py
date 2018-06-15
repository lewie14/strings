#Take the list of poems and make it so that we can display the name, title and publication date
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#step 1 - See what is currently looks like when printed
print(highlighted_poems)

#step 2 - split by commas and save in highlighted_poems_list and print
highlighted_poems_list = highlighted_poems.split (",")
print(highlighted_poems_list)

#step 3 - Clean out the whitespace by making an empty list highlighted_poems_stripped
#iterate through highlighted_poems_list and append results to highlighted_poems_stripped

highlighted_poems_stripped = []

for line in highlighted_poems_list :
  highlighted_poems_stripped.append(line.strip())

print(highlighted_poems_stripped)

#step 4 - Break up all the information for each poem into its own list
#Create an empty list called highlighted_poems_details
#iterate through highlighted_poems_stripped and split each string around the colon
#and append into highlighted_poems_details

highlighted_poems_details = []

for line in highlighted_poems_stripped:
  highlighted_poems_details.append(line.split(':'))
  
print(highlighted_poems_details)

#step 5 - Create 3 empty lists called titles, poets and dates

titles = []
poets = []
dates = []

#step 6 - separate out all of the titles, the poets, and the publication dates into their own lists.
#iterate through highlighted_poems_details and for each list in the list append the appropriate 
#elements into the lists titles, poets, and dates.

for item in highlighted_poems_details:
	titles.append(item[0])
	poets.append(item[1])
	dates.append(item[2])	
	
print(titles)
print(poets)
print(dates)

#step 7 - Write a loop that uses .format to print out the string
#----The poem TITLE was published by POET in DATE.

for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))
