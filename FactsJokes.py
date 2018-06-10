import random

def facts(entities, entity, values):
    try:
        fact = ""
        beauty = 0
        celebrity = 0
        disaster = 0
        fashion = 0
        food = 0
        health = 0
        history = 0
        hot = 0
        kids = 0
        lifestyle = 0
        nature = 0
        personal = 0
        place = 0
        science = 0
        travel = 0
        interesting = -1

        fact_type = str(values[entities.index(entity)])
        if (fact_type == "beauty fact") or (fact_type == "beauty facts") \
                or (fact_type == "fact about beauty") or (fact_type == "facts about beauty"):
            beauty = 1

        elif (fact_type == "celebrity fact") or (fact_type == "celebrity facts") \
                or (fact_type == "fact about celebrity") or (fact_type == "facts about celebrity") \
                or (fact_type == "fact about celebrities") or (fact_type == "facts about celebrities"):
            celebrity = 1

        elif (fact_type == "disaster fact") or (fact_type == "disaster facts") \
                or (fact_type == "fact about disaster") or (fact_type == "facts about disaster") \
                or (fact_type == "fact about disasteres") or (fact_type == "facts about disasteres"):
            disaster = 1

        elif (fact_type == "fashion fact") or (fact_type == "fashion facts") \
                or (fact_type == "fact about fashion") or (fact_type == "facts about fashion"):
            fashion = 1

        elif (fact_type == "food fact") or (fact_type == "food facts") \
                or (fact_type == "fact about food") or (fact_type == "facts about food"):
            food = 1

        elif (fact_type == "health fact") or (fact_type == "health facts") \
                or (fact_type == "fact about health") or (fact_type == "facts about health"):
            health = 1

        elif (fact_type == "history fact") or (fact_type == "history facts") \
                or (fact_type == "fact about history") or (fact_type == "facts about history")\
                or (fact_type == "historian fact") or (fact_type == "historian facts"):
            history = 1

        elif (fact_type == "hot fact") or (fact_type == "hot facts"):
            hot = 1

        elif (fact_type == "kid fact") or (fact_type == "kid facts") \
                or (fact_type == "fact about kid") or (fact_type == "facts about kid")\
                or (fact_type == "kids fact") or (fact_type == "kids facts") \
                or (fact_type == "fact about kids") or (fact_type == "facts about kids"):
            kids = 1

        elif (fact_type == "lifestyle fact") or (fact_type == "lifestyle facts") \
                or (fact_type == "fact about lifestyle") or (fact_type == "facts about lifestyle"):
            lifestyle = 1

        elif (fact_type == "nature fact") or (fact_type == "nature facts") \
                or (fact_type == "fact about nature") or (fact_type == "facts about nature")\
                or (fact_type == "biological fact") or (fact_type == "biological facts") \
                or (fact_type == "fact about biology") or (fact_type == "facts about biology"):
            nature = 1

        elif (fact_type == "personal fact") or (fact_type == "personal facts") \
                or (fact_type == "fact about personal") or (fact_type == "facts about personal")\
                or (fact_type == "person fact") or (fact_type == "person facts") \
                or (fact_type == "fact about person") or (fact_type == "facts about person"):
            personal = 1

        elif (fact_type == "place fact") or (fact_type == "place facts") \
                or (fact_type == "fact about place") or (fact_type == "facts about place") \
                or (fact_type == "fact about places") or (fact_type == "facts about places"):
            place = 1

        elif (fact_type == "science fact") or (fact_type == "science facts") \
                or (fact_type == "fact about science") or (fact_type == "facts about science")\
                or (fact_type == "scientific fact") or (fact_type == "scientific facts"):
            science = 1

        elif (fact_type == "travel fact") or (fact_type == "travel facts") \
                or (fact_type == "fact about travel") or (fact_type == "facts about travel")\
                or (fact_type == "traveling fact") or (fact_type == "traveling facts"):
            travel = 1

        else:
            interesting = int(random.random()) * 14

        if beauty == 1 or interesting == 0:
            i = int(random.random()) * 9
            if i == 0:
                fact = 'Lipstick was an essential item in World War II'

            elif i == 1:
                fact = 'The left side of the face is prettier than the right'

            elif i == 2:
                fact = 'Kitchen beauty treatments began in the middle ages'

            elif i == 3:
                fact = 'Maybelline was named after a girl called Mable'

            elif i == 4:
                fact = 'Believe it or not, back in the 1930s, radioactive beauty products were quite popular.'

            elif i == 5:
                fact = 'A 1991 study proved that the female politicians who employed the services of a ' \
                       'professional makeup artists and photographers were 30% more likely to win people’s votes.'

            elif i == 6:
                fact = 'Max Factor began his cosmetics business when he was manufacturing greasepaint ' \
                       'for stage actors and actresses.\n' \
                       'It was also Max factor, incidentally, who coined the phrase makeup. ' \
                       'Until then, it had always been referred to simply as cosmetics.'

            elif i == 7:
                fact = 'A study conducted by a psychologist Maria Agthe found that the very attractive looking ' \
                       'applicants for graduate scholarships received less favourable reviews from interviewers.'

            elif i == 8:
                fact = 'The Egyptians used to drink their perfume.'

            elif i == 9:
                fact = 'It has been proved that women are more attracted to men who attract the attention of ' \
                       'other women. British psychologist Benedict Jones found that women find a man more attractive ' \
                       'when he is being smiled at by other women.'

            else:
                fact = 'Beautiful people earn about 5% more than their average-looking colleagues.'

            return fact

        elif celebrity == 1 or interesting == 1:
            i = int(random.random()) * 14
            if i == 0:
                fact = 'George Washington Became an Official Surveyor When He Was 17 Years Old'

            elif i == 1:
                fact = 'George Washington Was Only 20 When He Took over a 1,000 Acre Estate'

            elif i == 2:
                fact = 'Einstein Created Modern Physics With 4 Papers in 1 Miracle Year,'

            elif i == 3:
                fact = 'In 3 Years Albert Einstein Went from Obscurity to Celebrity'

            elif i == 4:
                fact = 'Albert Einstein Read Euclid and Kant When He Was 10 Years Old'

            elif i == 5:
                fact = 'Albert Einstein Failed His First Entrance Exam to College in 1895'

            elif i == 6:
                fact = 'Cleopatra Was Not Egyptian, She Was Greek'

            elif i == 7:
                fact = 'Christopher Columbus Taught Himself 3 Languages'

            elif i == 8:
                fact = 'When he was young, Quentin Tarantino used to watch an average of 200 theater movies per year.'

            elif i == 9:
                fact = 'As a child, Johnny Depp was allergic to chocolate.'

            elif i == 10:
                fact = 'Orlando Bloom has swinophobia, which is a fear of pigs!'

            elif i == 11:
                fact = 'Bruce Willis admits to taking drugs as a teenager.'

            elif i == 12:
                fact = 'Morgan Freeman has a private pilot’s license, which he earned at the age of 65!'

            elif i == 13:
                fact = 'Rihanna’s first name is Robyn.'

            elif i == 14:
                fact = 'Cleopatra Was the Last Pharaoh of Egypt'

            else:
                fact = 'Wayne Rooney was only sixteen years old when he first played for Everton.'

            return fact

        elif disaster == 1 or interesting == 2:
            i = int(random.random()) * 9
            if i == 0:
                fact = '250,000 Jews Were Killed in Europe Long Before the Holocaust'

            elif i == 1:
                fact = 'Katrina Was the Strongest Hurricane Ever Recorded on the Gulf'

            elif i == 2:
                fact = 'There Were Only Enough Lifeboats for 1,178 People on The Titanic'

            elif i == 3:
                fact = 'It Took Over 70 Years for the Titanic Wreck to Be Found'

            elif i == 4:
                fact = 'When Storms Produce More Than One Tornado It’s Called an ‘Outbreak’'

            elif i == 5:
                fact = 'Tornadoes Have Been Witnessed on Every Continent Except Antarctica'

            elif i == 6:
                fact = 'Up to 10,000 people die a year as a result of an earthquake.'

            elif i == 7:
                fact = 'Hurricanes have winds of at least 74 miles per hour.'

            elif i == 8:
                fact = 'Floods are the number one deadly disaster in the United States accounting for over ' \
                       '46 percent of disaster related deaths according to disaster facts.'

            elif i == 9:
                fact = 'The state that has the largest risk for tsunamis is Hawaii with over one a year.'

            else:
                fact = 'Every year over 25.8 million people are affected by a natural disaster across the world.'

            return fact

        elif fashion == 1 or interesting == 3:
            i = int(random.random()) * 9
            if i == 0:
                fact = 'Did you know that in 15th century, being pregnant was considered as fashionable and if girls ' \
                       'weren’t pregnant, they would hide pillows under their dresses to fake a baby bump?'

            elif i == 1:
                fact = 'In the 18th century, high heels were so much wide-spread that even children wore it. '

            elif i == 2:
                fact = 'Completely unbelievable, but it is a fact that the first ever fashion magazine named ' \
                       'Le Mercure Galant was aimed at male audience. The magazine was published in 1678, ' \
                       'while only 16 years later a fashion magazine for women appeared in the sale. '

            elif i == 3:
                fact = 'Trends for skirts were substantially influenced by the invention of automobile in 18-19th ' \
                       'century. After the invention skirts became shorter in order to allow women easily and ' \
                       'comfortably step into automobile. '

            elif i == 4:
                fact = 'How would you feel if wearing a hat was a mandatory requirement coming from your government? ' \
                       'You think it’s funny? Not at all. Elizabeth I loved hats so much that she made it ' \
                       'compulsory for all females over the age of 7 to wear hats on Sundays and holidays. ' \
                       'Anyone who refused to do so was stiffly fined.'

            elif i == 5:
                fact = 'Thanks to Napoleon Bonaparte for buttons on jacket sleeves which he ordered to attach ' \
                       'to prevent soldiers from wiping off their runny noses on their sleeves.'

            elif i == 6:
                fact = 'The world’s most valuable fashion brand is Louis Vuitton with the worth of $23 billion.'

            elif i == 7:
                fact = 'There is a name for a person who collects ties - "Grabatologist".'

            elif i == 8:
                fact = 'One billion rabbits are killed each year so that their fur can be used in clothing or ' \
                       'for lures in fly-fishing or trim on craft items.'

            elif i == 9:
                fact = 'The first official Fashion Week started in 1943 in New York. Its main purpose was to distract' \
                       ' the attention away from French fashion during World War II and kickstart the way ' \
                       'for American designers.'

            else:
                fact = 'All women should be thanking Mary Phelps, a New York socialite, for creating the modern bra. ' \
                       'The ones she made and patented in 1914 were very unlike the ones we wear today, though. ' \
                       'Hers were made of handkerchiefs.'

            return fact

        elif food == 1 or interesting == 4:
            i = int(random.random()) * 9
            if i == 0:
                fact = 'The average person eats for a life of 20-25 tons of food.'

            elif i == 1:
                fact = 'In Japan, sold ice cream flavored octopus, buffalo tongue, cactus, chicken wings and crab.'

            elif i == 2:
                fact = 'In Colombia, the cinema instead of popcorn offers a bag of fried giant ants.'

            elif i == 3:
                fact = 'Want kebab alligator? Go to South Louisiana, USA.'

            elif i == 4:
                fact = 'On the streets of Indonesia sell smoked bats. '

            elif i == 5:
                fact = 'In Japan, the jellyfish are exquisite delicacy, despite the presence of a dangerous poison. ' \
                       'If the dish to cook properly, death is inevitable.'

            elif i == 6:
                fact = 'And in a restaurant in New York you can submit an omelet worth $ 1,000. It consists of an ' \
                       'entire lobster and 280 grams of caviar, eggs, potatoes and whiskey. '

            elif i == 7:
                fact = 'Originally Carrots are purple in color.'

            elif i == 8:
                fact = 'The most stolen food in the world is cheese.'

            elif i == 9:
                fact = 'Honey can last for 3000 years, it is the only food item that will never get rotten.'

            else:
                fact = 'The juice that contains a small amount of alcohol is Orange juice.'

            return fact

        elif health == 1 or interesting == 5:
            i = int(random.random()) * 9
            if i == 0:
                fact = '20 Million Americans Have Died from Smoking in the Last 50 Years'

            elif i == 1:
                fact = '1 in 10 Deaths of 20-64 Year Olds Are due to Alcohol'

            elif i == 2:
                fact = '93 Million Americans are Affected by Obesity'

            elif i == 3:
                fact = 'Excess Body Fat Causes Type 2 Diabetes in 77% of Women and 64% of Men'

            elif i == 4:
                fact = 'Marijuana is the Most Widely Used Drug in the World'

            elif i == 5:
                fact = 'Marijuana Accounts for 48% of Drug Arrest in the United States'

            elif i == 6:
                fact = '1/3 of all cancers are preventable.'

            elif i == 7:
                fact = '33% of those who drink four or more caffeinated beverages, such as soda or coffee,' \
                       ' daily are put at a higher risk for sleep apnea'

            elif i == 8:
                fact = 'On average, right-handed people live 9 years longer than left-handed people.'

            elif i == 9:
                fact = 'Out of the 206 bones in the human adult’s body, 106 are in the hands and feet.'

            else:
                fact = 'During a sneeze, all of your bodily functions momentarily stop, even your heart.'

            return fact

        elif history == 1 or interesting == 6:
            i = int(random.random()) * 19
            if i == 0:
                fact = 'Cleopatra Was the Last Pharaoh of Egypt'

            elif i == 1:
                fact = 'Humans have been hunter-gatherers for 99% of their history.'

            elif i == 2:
                fact = 'Humans are 50% heavier and four inches taller in the past 100 years than ' \
                       'they have been throughout most of human history.'

            elif i == 3:
                fact = 'In 5,000 years of human history, only one disease has been eradicated: smallpox.'

            elif i == 4:
                fact = 'When Columbus "discovered" the Americas, the continent was already inhabited by 90 million' \
                       ' people which was a third of the world’s population.'

            elif i == 5:
                fact = 'Leif Erikson is regarded as the first European to land in North America, nearly ' \
                       '500 years before Columbus.'

            elif i == 6:
                fact = 'We Are Living In The Most Peaceful Time In Human History.'

            elif i == 7:
                fact = 'WW1 was the sixth deadliest conflict in world history.'

            elif i == 8:
                fact = 'The Afghan War is the longest war in U.S. history.'

            elif i == 9:
                fact = 'Napoleon wasn’t short. He was actually above the average Frenchman.'

            elif i == 10:
                fact = 'About 100 billion people have died in all human history.'

            elif i == 11:
                fact = 'Interracial marriage was banned in the U.S. for much of its history: from 1776 to 1967.'

            elif i == 12:
                fact = 'The first car accident occurred in 1891, in Ohio.'

            elif i == 13:
                fact = 'From 1814 to 1830, the flag of the Kingdom of France was plain white.'

            elif i == 14:
                fact = 'Life expectancy in Ancient Rome was from 20 to 30 years.'

            elif i == 15:
                fact = 'Christmas was illegal in the U.S. until 1836 as it was considered an Ancient Pagan Holiday.'

            elif i == 16:
                fact = 'The Aztecs sacrificed 1% of their population every year, or about 250,000 people.'

            elif i == 17:
                fact = 'Proportionally speaking, the most destructive war in modern history was the War of the ' \
                       'Triple Alliance, which took the lives of over 60% of Paraguay’s ' \
                       'population, leaving a woman/man ratio of 4 to 1.'

            elif i == 18:
                fact = 'Estimates for the total number of people killed in wars throughout all of ' \
                       'human history range from 150 million to 1 billion.'

            elif i == 19:
                fact = 'If Earth’s history were condensed into 24 hours, life would’ve appeared at 4am, land plants ' \
                       'at 10:24pm, dinosaur extinction at 11:41pm and human history would’ve begun at 11:58:43pm.'

            else:
                fact = 'In 536 A.D., there was a worldwide dust cloud that blocked out the sun for a year, ' \
                       'resulting in widespread famine and disease.'

            return fact

        elif hot == 1 or interesting == 7:
            i = int(random.random()) * 20
            if i == 0:
                fact = '20 Million Americans Have Died from Smoking in the Last 50 Years'

            elif i == 1:
                fact = '1 in 3 Cancer Deaths Are Caused by Smoking'

            elif i == 2:
                fact = '70% of States Have Gay Marriage, 15 States Ban It'

            elif i == 3:
                fact = '170 Thousand Billion Watts from the Sun Hits Earth Every Moment'

            elif i == 4:
                fact = 'When We Eat Fruits and Vegetables We Get Calories from the Sun'

            elif i == 5:
                fact = 'Vitamin D is Created in Our Body by Solar Energy'

            elif i == 6:
                fact = 'The First Solar Power Station Was Built in 1912'

            elif i == 7:
                fact = '800 Million to 600 Million Years Ago the Earth Was Covered in Ice'

            elif i == 8:
                fact = 'A Change in the Earth’s Temperature Has a Domino Effect on Weather'

            elif i == 9:
                fact = 'Madame Curie’s notebooks are still radioactive. Researchers wishing to study them must ' \
                       'sign a waiver in order to do so.'

            elif i == 10:
                fact = 'When Twister was introduced in 1966, it was denounced by critics as "sex in a box."'

            elif i == 11:
                fact = 'There are more lifeforms living on your skin than there are people on the planet.'

            elif i == 12:
                fact = 'OJ Simpson was originally cast to play Terminator, but the studio was afraid that no ' \
                       'one would buy him as a remorseless killer.'

            elif i == 13:
                fact = 'Leonardo da Vinci could write with one hand and draw with the other at the same time.'

            elif i == 14:
                fact = 'The last man to walk on the moon, Gene Cernan, promised his daughter he’d write her initials ' \
                       'on the moon. He did, and her initials, “TDC,” will probably be on the moon ' \
                       'for tens of thousands of years.'

            elif i == 15:
                fact = 'The Mimic Octopus can not only change colours, but will mimic the shapes of other animals,' \
                       ' like the flounder, lionfish, and sea snakes.'

            elif i == 16:
                fact = 'Twenty percent of office coffee mugs contain fecal matter.'

            elif i == 17:
                fact = 'If you were to remove all of the empty space from the atoms that make up every human on ' \
                       'earth, the entire world population could fit into an apple.'

            elif i == 18:
                fact = 'The three wealthiest families in the world have more assets than the' \
                       ' combined wealth of the forty-eight poorest nations.'

            elif i == 19:
                fact = 'The biggest traffic jam lasted for more than 10 days, with cars only moving 0.6 miles a day.'

            elif i == 20:
                fact = 'When adjusted for inflation, John D. Rockefeller is the richest man in the history ' \
                       'of the world with a net worth 10 times more than Bill Gates.'

            else:
                fact = 'Dueling is legal in Paraguay as long as both parties are registered blood donors.'

            return fact

        elif kids == 1 or interesting == 8:
            i = int(random.random()) * 9
            if i == 0:
                fact = 'Former billionaire Chuck Feeney has given away over 99% of his 6.3 Billion dollars to help' \
                       ' under privileged kids go to college. He is now worth $2 million dollars.'

            elif i == 1:
                fact = 'The longest study of humans ever conducted, the 75 years long Harvard grant study found ' \
                       'that professional success in life comes from having done chores as a kid.'

            elif i == 2:
                fact = 'U.K. kids spend less time outside than prison inmates.'

            elif i == 3:
                fact = 'Bilingual children appear to get a head start on empathy-related skills such as learning ' \
                       'to take someone else’s perspective.'

            elif i == 4:
                fact = 'Kids in cars are 12 times more distracting for drivers than talking on cell phones.'

            elif i == 5:
                fact = 'In 2013, a 17-year old kid named Tyler Hadley murdered his parents and hid ' \
                       'their bodies in a locked bedroom so he could throw a huge house party.'

            elif i == 6:
                fact = 'Doctor Who was originally an educational show, with episodes set in the future ' \
                       'to teach kids about science, and episodes set in the past to teach them history.'

            elif i == 7:
                fact = 'We typically do not start to think of foods as "too sweet" until our bone growth stops. ' \
                       'Younger children have virtually no limit to the amount of sugar they find palatable.'

            elif i == 8:
                fact = 'When researchers offered kids broccoli or a chocolate bar, four out of five picked the ' \
                       'chocolate but when an Elmo sticker was placed on the broccoli, 50 % chose the broccoli.'

            elif i == 9:
                fact = 'In 1994, a Russian pilot named Yaroslav Kudrinsky let his 15-year-old son ' \
                       'and 12-year-old daughter try to fly an aircraft.'

            else:
                fact = 'If a set of identical twin women married a set of identical twin men ' \
                       'and subsequently had kids, their children would genetically be siblings.'

            return fact

        elif lifestyle == 1 or interesting == 9:
            i = int(random.random()) * 9
            if i == 0:
                fact = 'One of the popular hobbies among women is shopping. They will love to buy accessories ' \
                       'and fashion items that they do not need just because they are sold with discount promo.'

            elif i == 1:
                fact = 'One of the phenomenal masterpieces from the greatest artist Leonardo Da Vinci is the ' \
                       'painting of Mona Lisa. If you scrutinize the face of this beautiful woman, you will see ' \
                       'that she has not eyebrows.  It was a fashion in such era to shave the eyebrows if you want' \
                       'to be considered as a beautiful woman.'

            elif i == 2:
                fact = 'The development of technology is well represented through internet. You can gain a lot ' \
                       'of information about education, science, fashion, technology and health easily by accessing ' \
                       'internet. If someone is bothering you every day, you just have to teach his or her to use ' \
                       'internet. Trust me that they will never disturb you for weeks.'

            elif i == 3:
                fact = 'Cell phone is the fourth point of life facts. It is another invasion of technology to human ' \
                       'life. People love to use cell phone when they want to communicate. In US, more than 30 ' \
                       'million of mobile phones are used by the citizens on a daily basis.'

            elif i == 4:
                fact = 'Olive is included as a species of a small tree. It is the member of family Oleaceae. ' \
                       'The fascinating fact lies on the life span of Olive. It can live up to 1500 years.'

            elif i == 5:
                fact = 'Shirt is the clothing line that people wear when they want to go in formal occasion. The ' \
                       'shirt for men and women are different. If you look at the men’s shirt, you will see that ' \
                       'it has the button on the right side. The women’s shirt is equipped with the button ' \
                       'on the left side.'

            elif i == 6:
                fact = 'The seventh point of life facts is about Cleopatra. She is considered as the beautiful woman ' \
                       'in the world. The queen of Egypt had married with two of her bothers. Isn’t that ridiculous?'

            elif i == 7:
                fact = 'Ant is one of the tiny animals. This species loves with sugar. When people sleep, they will ' \
                       'close their eyes. I just wonder on how the ants sleep since they cannot shout the eyes.'

            elif i == 8:
                fact = 'Cooking is a nice hobby for some men and women. They will have a chance to explore the skill ' \
                       'by making exclusive food. If you have to slice the onion, I suggest you to eat chewing gum. ' \
                       'It can decrease the tears when you cut the onions.'

            elif i == 9:
                fact = 'You will be lucky if you can eat fortune cookies. This food was initially created by ' \
                       'Charles Jung in America, 1918.'

            else:
                fact = 'The country, which most likely will soon be under water, is Maldives.'

            return fact

        elif nature == 1 or interesting == 10:
            i = int(random.random()) * 21
            if i == 0:
                fact = 'Bald Eagles Build the Largest Tree Nests of Any Bird'

            elif i == 1:
                fact = 'Female Bald Eagles Are 25% Larger than Males'

            elif i == 2:
                fact = 'Bears Have Lived on Earth for 38 Million Years'

            elif i == 3:
                fact = 'There Are over 30 Dolphin Species'

            elif i == 4:
                fact = 'Polar Bears Evolved from Brown to White for Camouflage'

            elif i == 5:
                fact = 'Male Polar Bears Have Longer Hairs on Their Front Legs for Mating'

            elif i == 6:
                fact = 'There Are Only 8 Species of Bear'

            elif i == 7:
                fact = 'Penguins Lost the Ability to Fly 62 Million Years Ago'

            elif i == 8:
                fact = 'Koalas Sleep 20 Hours a Day'

            elif i == 9:
                fact = 'Koalas Only Spend 15 Minutes a Day Hanging Out'

            elif i == 10:
                fact = 'Koalas Have 2 Opposable Thumbs'

            elif i == 11:
                fact = 'Penguins Can Swim Up to 17 Miles Per Hour'

            elif i == 12:
                fact = 'Penguins Can Drink Salt Water and Not Get Sick'

            elif i == 13:
                fact = 'Penguins Can Withstand −40 °F by Working Together in Heat Packs'

            elif i == 14:
                fact = 'The Largest Bear Is 30 Times the Size of Smallest Bear'

            elif i == 15:
                fact = 'Baby Pandas Are Blind, Hairless and 1/900th the Size of the Mother'

            elif i == 16:
                fact = 'More than Meow! Cats Can Make Over 90 Different Sounds'

            elif i == 17:
                fact = 'Is It Time for a Catnap? Cat’s Spend 2/3rds of Their Life Sleeping'

            elif i == 18:
                fact = 'Lions, Tigers, Jaguars, and Leopards Purr Too'

            elif i == 19:
                fact = 'Giraffes Are as Tall as a 2-Story House'

            elif i == 20:
                fact = 'A Giraffe Can Shatter a Lion’s Skull with 1 Kick'

            elif i == 21:
                fact = 'Giraffes Can Run Over 30 Miles Per Hour'

            else:
                fact = 'Giraffes Necks Grew Over Time … Over Millions Of Years'

            return fact

        elif personal == 1 or interesting == 11:
            i = int(random.random()) * 9
            if i == 0:
                fact = 'The brain is more lively at night than during the day. Scientists don’t ' \
                       'recognize yet why this is.'

            elif i == 1:
                fact = 'The most interesting fact about human body is that women’s heart beat quicker than men’s. ' \
                       'Women blink two times as men do. ' \
                       'Women are natural better smellers than men and remain superior smellers over life.'

            elif i == 2:
                fact = 'Babies are forever born with blue eyes. The melanin in their eyes wants time to be fully ' \
                       'deposit or to be dark by ultraviolet light to disclose the baby’s true eye color.'

            elif i == 3:
                fact = 'The single part of your body that has no blood supply is the cornea in the eye. ' \
                       'It gets its oxygen straight from air.'

            elif i == 4:
                fact = 'Our skeleton keeps renewing itself every ten years which means to every ten years you' \
                       ' get a fresh skeleton.'

            elif i == 5:
                fact = 'An adult human being is made of approximately 7,000,000,000,000,000,000,000,000,000 atoms. ' \
                       'Obviously, this varies based on the size of the person and their body composition.'

            elif i == 6:
                fact = 'There are 100,000 miles of blood vessels in an adult human body. The largest blood vessel ' \
                       'is the aorta, which is just over an inch in diameter.'

            elif i == 7:
                fact = 'Researchers estimate that the average human being can distinguish between 1 trillion ' \
                       'different odors. This is much more acute than the human eye, which can ' \
                       'distinguish about 10 million different colors.'

            elif i == 8:
                fact = 'Pound for pound, the strongest muscle in the human body is the masseter (jaw muscle). ' \
                       'It can clamp your chompers shut with 55 pounds of force on the incisors and 200' \
                       ' pounds of force on the molars.'

            elif i == 9:
                fact = 'Your ears and nose will never stop growing until the day you die. In fact, your earlobes ' \
                       'will also elongate from gravity.'

            else:
                fact = 'Similar to fingerprints, everyone also has a unique tongue print. It may be some time before ' \
                       'your local police station starts taking tongue prints, but research on the required 3-D ' \
                       'imaging technology is already being developed and tested.'

            return fact

        elif place == 1 or interesting == 12:
            i = int(random.random()) * 20
            if i == 0:
                fact = '6% of People in Ecuador Speak 1 of 13 Native Dialects'

            elif i == 1:
                fact = 'There Are More Mobile Phones Than People in Ecuador'

            elif i == 2:
                fact = 'The Eiffel Tower Was the World’s Tallest Structure for 41 Years'

            elif i == 3:
                fact = 'Gustave Eiffel Did Not Design the Eiffel Tower – Maurice Koechlin Did'

            elif i == 4:
                fact = 'It Took 3 Years of Lobbying to Approve the Eiffel Tower in 1887'

            elif i == 5:
                fact = 'Over 200,000,000 People Have Visited the Eiffel Tower'

            elif i == 6:
                fact = 'Only One Person Died in the Construction of the Eiffel Tower'

            elif i == 7:
                fact = 'More than 2 Million German Soldiers Died in World War 1'

            elif i == 8:
                fact = 'More than 5 Million German Soldiers Died in World War 2'

            elif i == 9:
                fact = 'X-Rays, The Printing Press, and Einstein all Came from Germany'

            elif i == 10:
                fact = 'People Lived in Argentina More than 10,000 Years Ago'

            elif i == 11:
                fact = 'The Statue of Liberty Was Built Like the Eiffel Tower'

            elif i == 12:
                fact = 'Models of the Statue of Liberty Sold Before the Statue Was Done'

            elif i == 13:
                fact = 'The Statue of Liberty Honors the Union Victory in the Civil War'

            elif i == 14:
                fact = 'The Statue of Liberty’s Nose is Over 4 Feet Long'

            elif i == 15:
                fact = 'The Statue of Liberty Has Had a Few Makeovers in 120 Years'

            elif i == 16:
                fact = 'Africa is the home for largest living land animals, the African elephant, ' \
                       'and the tallest, Giraffe.'

            elif i == 17:
                fact = 'In 1867, the U.S. owned Alaska for just $72 millions from Russia.'

            elif i == 18:
                fact = 'In Antarctica, there is only 1 ATM.'

            elif i == 19:
                fact = 'The most visited place in Europe is Disneyland, Paris.'

            elif i == 20:
                fact = 'There are many hidden walkways that are not explored yet in Giza pyramid.'

            else:
                fact = 'Argentina is Huge – Over 1 Million Square Miles'

            return fact

        elif science == 1 or interesting == 13:
            i = int(random.random()) * 60
            if i == 0:
                fact = 'The Earth Generates $72 Trillion of Goods and Services Each Year'

            elif i == 1:
                fact = 'The Word ‘Earth’ Has Been on Earth for 7,000 Years'

            elif i == 2:
                fact = 'The Earth Isn’t a Perfect Sphere – It Has a 27 Mile Tall Bulge at Its Belly'

            elif i == 3:
                fact = 'The Earth Is 32.1% Iron and 30.1% Oxygen'

            elif i == 4:
                fact = 'The Center of the Earth, at 10,380 °F, Is as Hot as the Sun'

            elif i == 5:
                fact = 'If The Earth Was Smooth, A 1.5 Mile Deep Ocean Would Cover the World'

            elif i == 6:
                fact = 'It’s Hard to Tell Where Earth’s Atmosphere Ends and Space Begins'

            elif i == 7:
                fact = 'Going as Fast as the Earth You Could Reach the Moon in 3.5 Hours'

            elif i == 8:
                fact = 'When the Earth Was Formed, a Day Was Only 5.5 Hours Long'

            elif i == 9:
                fact = '77% of the Earth’s Population Lives in the Northeastern Quadrasphere'

            elif i == 10:
                fact = 'Einstein Created Modern Physics With 4 Papers in 1 Miracle Year, 1905'

            elif i == 11:
                fact = 'Albert Einstein Read Euclid and Kant When He Was 10 Years Old'

            elif i == 12:
                fact = 'Albert Einstein Convinced FDR to Build the Atomic Bomb'

            elif i == 13:
                fact = 'It Took 15 Years for Einstein’s Relativity Theory to Make Him Famous'

            elif i == 14:
                fact = 'Albert Einstein Failed His First Entrance Exam to College in 1895'

            elif i == 15:
                fact = 'Albert Einstein Was an Ordinary Patent Clerk When He Was 21'

            elif i == 16:
                fact = 'Albert Einstein Made His Breakthrough Discoveries in Relative Isolation'

            elif i == 17:
                fact = 'In 3 Years Albert Einstein Went from Obscurity to Celebrity'

            elif i == 18:
                fact = 'Einstein’s Relativity Theory Was Proved in 1919 During a Solar Eclipse'

            elif i == 19:
                fact = 'Albert Einstein Wasn’t a United States Citizen Until 1940'

            elif i == 20:
                fact = '170 Thousand Billion Watts from the Sun Hits Earth Every Moment'

            elif i == 21:
                fact = 'When We Eat Fruits and Vegetables We Get Calories from the Sun'

            elif i == 22:
                fact = 'The First Solar Power Station Was Built in 1912'

            elif i == 23:
                fact = 'A Cool Drink on a Hot Day Is A Passive Solar Technology'

            elif i == 24:
                fact = 'Solar Panels Use Photons to Create Excitons and Electron Hole Pairs'

            elif i == 25:
                fact = 'In 1996 NASA Claimed They Found Life on Mars'

            elif i == 26:
                fact = 'Mankind Has Sent Over 40 Space Missions to Mars'

            elif i == 27:
                fact = 'There Are 3 Robots on Mars Right Now'

            elif i == 28:
                fact = 'Scientists Have Confirmed Liquid Water Once Flowed on Mars'

            elif i == 29:
                fact = 'Mars Is Red Because It’s a Rusty Planet'

            elif i == 30:
                fact = 'Mars Has Seasons like Earth, but with More Extreme Weather'

            elif i == 31:
                fact = 'Galileo Almost Discovered Neptune in the 1600’s'

            elif i == 32:
                fact = 'Neptune Was First Observed in Berlin on September 23rd, 1846'

            elif i == 33:
                fact = 'The Discovery of Neptune was a Big Victory for Science and Math'

            elif i == 34:
                fact = 'Neptune is 17 Times as Massive as Earth'

            elif i == 35:
                fact = 'Neptune Has 14 Moons'

            elif i == 36:
                fact = 'The Winds on Neptune Are Over 1300 Miles Per Hour'

            elif i == 37:
                fact = 'The Rings on Neptune Were Discovered by Voyager 2 in 1989'

            elif i == 38:
                fact = 'A Coat Isn’t Enough … It’s Over 300 Degrees Below Zero on Neptune'

            elif i == 39:
                fact = 'Neptune is the Farthest Planet from the Sun … Again'

            elif i == 40:
                fact = 'In Rome Saturn Was Celebrated with Saturnalia The Biggest Party'

            elif i == 41:
                fact = 'Saturn is 95 Times More Massive Than Earth'

            elif i == 42:
                fact = 'The Center of Saturn is Hot – Over 20,000 Degrees Fahrenheit'

            elif i == 43:
                fact = 'Saturn Is Not the Only Planet with Rings'

            elif i == 44:
                fact = 'Saturn’s Moon Phoebe Orbits In The Opposite Direction'

            elif i == 45:
                fact = 'Saturn Has Over 100 Moons and Moonlets'

            elif i == 46:
                fact = 'Saturn’s Moon Enceladus May Have Life On It'

            elif i == 47:
                fact = 'Winds On Saturn Are Over 1,000 Miles Per Hour'

            elif i == 48:
                fact = 'Jupiter Was Named Over 2,000 Years Ago'

            elif i == 49:
                fact = 'Jupiter is 2.5 Times As Massive As All the Other Planets Combined'

            elif i == 50:
                fact = 'Jupiter Generates As Much Energy As it Gets from the Sun'

            elif i == 51:
                fact = 'Saturn Is Not the Only Planet with Rings, Jupiter Has 4 Rings'

            elif i == 52:
                fact = 'The Wind on Jupiter is Over 200 Miles Per Hour'

            elif i == 53:
                fact = 'Galileo Discovered Jupiter’s Moons in 1610'

            elif i == 54:
                fact = 'The Name Uranus is Over 2,500 Years Old'

            elif i == 55:
                fact = 'Uranus Was One of the Last Planets to Be Found in the 1700’s'

            elif i == 56:
                fact = 'Uranus Receives 1/400th the Energy that Earth Receives from the Sun'

            elif i == 57:
                fact = 'Brrrr … Uranus is over 350 Degrees Below Zero'

            elif i == 58:
                fact = 'Uranus Has 27 Moons and 11 Rings'

            elif i == 59:
                fact = 'Uranus Has Winds Over 500 Miles Per Hour'

            elif i == 60:
                fact = 'William Herschel Discovered Uranus in 1781'

            else:
                fact = 'The human brain can continue to live without oxygen supply for 4 - 6 minutes, after which ' \
                       'it slowly starts dying.'

            return fact

        elif travel == 1 or interesting == 14:
            i = int(random.random()) * 9
            if i == 0:
                fact = 'Travel can help improve your problem-solving skills.'

            elif i == 1:
                fact = 'One out of eight jobs in the U.S. depends on travel and tourism.'

            elif i == 2:
                fact = 'Taking a vacation can lower your risk of heart disease.'

            elif i == 3:
                fact = 'Studies show that money spent on travel makes you happier than money spent on material goods.'

            elif i == 4:
                fact = 'Benefits of travel are almost immediate. After only a day or two, 89% of ' \
                       'people experience significant drops in stress.'

            elif i == 5:
                fact = 'Travel has been shown to help aid those suffering from depression.'

            elif i == 6:
                fact = 'The shortest airline flight available for purchase lasts two minutes and runs from the ' \
                       'Scottish island of Westray to Papa Westray.'

            elif i == 7:
                fact = 'The largest hotel in the world is the Izmailovo Hotel in Russia. It could accommodate ' \
                       'over 7,500 guests.'

            elif i == 8:
                fact = 'The most expensive hotel room in the world costs $83,200 a night at the Royal Penthouse ' \
                       'Suite in Geneva at Hotel President Wilson'

            elif i == 9:
                fact = 'France is the most visited country in the world.'

            else:
                fact = 'Couples who travel together have reported increased feelings of intimacy.'

            return fact

        else:
            fact = 'Travel can also make you smarter.'
            return fact

        return fact

    except:
        pass

def jokes(entities, entity, values):
    try:
        joke = ""
        i = int(random.random() * 88)

        if i == 1:
            joke = "Can a kangaroo jump higher than a house? \n" \
                   "Of course, a house doesn’t jump at all."

        elif i == 2:
            joke = 'Doctor: "Im sorry but you suffer from a terminal illness and have only 10 to live." \n' \
                   'Patient: "What do you mean, 10? 10 what? Months? Weeks?!" \n' \
                   'Doctor: "Nine." '

        elif i == 3:
            joke = 'A man asks a farmer near a field, “Sorry sir, would you mind if ' \
                   'I crossed your field instead of going around it? You see, I have to catch the 4:23 train.” \n' \
                   'The farmer says, “Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.”'

        elif i == 4:
            joke = 'Anton, do you think I’m a bad mother? \n' \
                   'My name is Paul.'

        elif i == 5:
            joke = 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.'

        elif i == 6:
            joke = 'What is the difference between a snowman and a snowwoman?\n' \
                   '-\n' \
                   'Snowballs.'

        elif i == 7:
            joke = 'Mother: "How was school today, Patrick?"\n' \
                   'Patrick: "It was really great mum! Today we made explosives!" \n' \
                   'Mother: "Ooh, they do very fancy stuff with you these days. ' \
                   'And what will you do at school tomorrow?" \n' \
                   'Patrick: "What school?"'

        elif i == 8:
            joke = '"Mom, where do tampons go?"\n' \
                   '"Where the babies come from, darling."\n' \
                   '"In the stork?"'

        elif i == 9:
            joke = 'Man to his priest: “Yesterday I sinned with an 18 year old girl.”\n' \
                   'The priest: “Squeeze 18 lemons and drink the juice all at once.”\n' \
                   'Man: “And that frees me from my sin?”\n' \
                   'Priest: “No, but it frees your face from that dirty grin.”'

        elif i == 10:
            joke = 'Doctor: “I’ve found a great new drug that can help you with your sleeping problem.” \n' \
                   'Patient: “Great, how often do I have to take it?” \n' \
                   'Doctor: “Every two hours.”'

        elif i == 11:
            joke = 'Sleep with an open window tonight! \n' \
                   '1400 mosquitos like that. 420 mosquitos commented on it. 210 mosquitos shared this. \n' \
                   'One mosquito invited for the event. 2800 mosquitos will be attending the event.'

        elif i == 12:
            joke = '“My wife suffers from a drinking problem.” \n' \
                   '-\n' \
                   ' “Oh is she an alcoholic?”\n' \
                   '-\n' \
                   ' “No, I am, but she’s the one who suffers.”'

        elif i == 13:
            joke = 'I managed to lose my rifle when I was in the army. I had to pay $855 to cover the loss.\n' \
                   'I’m starting to understand why a Navy captain always goes down with his ship.'

        elif i == 14:
            joke = 'Coco Chanel once said that you should put perfume on places where you want to be kissed by a man. '\
                   'But hell does that burn!'

        elif i == 15:
            joke = 'A wife goes to consult a psychiatrist about her husband: “My husband is acting so weird. ' \
                   'He drinks his morning coffee and then he goes and eats the mug! He only leaves the handle!”\n' \
                   'Psychiatrist: “Yes, that is weird. The handle is the best part.'

        elif i == 16:
            joke = 'Doctor: “Do you do sports?”\n' \
                   'Patient: “Does sex count?”\n' \
                   'Doctor: “Yes.”\n' \
                   'Patient: “Then no.”'

        elif i == 17:
            joke = 'Oh darling, since you have started dieting, you have become such a passionate kisser…\n' \
                   'What do you mean, passionate? I’m looking for food remains!'

        elif i == 18:
            joke = 'In Spain, there is a tradition after a bullfight to serve the mayor the bull"s testicles.\n' \
                   '-\n' \
                   'One day after a bullfight, the mayor asks the waiter: “Funny, why are they so small today?”\n' \
                   '-\n' \
                   'The waiter: “Today, sir, the bull won.”'

        elif i == 19:
            joke = 'Harry prays to God: Dear Lord, please make me win the lottery. \n' \
                   'The next day Harry begs the Lord again: Please make it so I win the lottery, Lord! \n' \
                   'The next day, Harry again prays: Please, please, dear Lord, make me win the lottery! \n' \
                   'Suddenly he hears a voice from above: Harry, would you kindly go and buy a lottery ticket.'

        elif i == 20:
            joke = '“You know how it is in life. One door closes – that means another door opens…”\n' \
                   '“Yeah, very nice, but you either fix that or I’m expecting a serious discount on that car!”'

        elif i == 21:
            joke = 'A wife complains to her husband: “Just look at that couple down the road, how lovely they are. ' \
                   'He keeps holding her hand, kissing her, holding the door for her, why cant you do the same?”\n' \
                   'The husband: “Are you mad? I barely know that woman!”'

        elif i == 22:
            joke = 'Me and my wife decided that we dont want to have children anymore. ' \
                   'So anybody who wants one can leave us their phone number and address and we will bring you one.'

        elif i == 23:
            joke = 'Police: “Open the door!” \n' \
                   '-\n' \
                   'Man: “I don’t want any balls!” \n' \
                   '-\n' \
                   'Police: “What? We don’t have any balls!”\n' \
                   '-\n' \
                   'Man: “I know.”'

        elif i == 24:
            joke = 'In a boomerang shop: "Id like to buy a new boomerang please. ' \
                   'Also, can you tell me how to throw the old one away?"'

        elif i == 25:
            joke = 'Patient: Oh doctor, Im just so nervous. This is my first operation.\n' \
                   '-\n' \
                   'Doctor: Dont worry. Mine too.'

        elif i == 26:
            joke = 'Mr. Smith: “Doctor, you remember this strengthening solution you prescribed me yesterday?”\n' \
                   'Doctor: “Yes, what’s the matter?”\n' \
                   'Mr. Smith: “I would like to use it but I can’t open the bottle!”'

        elif i == 27:
            joke = 'Doctor: Hello, did you come to see me with an eye problem?\n' \
                   'Patient: Wow, yes, how can you tell?\n' \
                   'Doctor: Because you came in through the window instead of the door.'

        elif i == 28:
            joke = 'Patient: Doctor help me please, every time I drink a cup of coffee ' \
                   'I get this intense stinging in my eye.\n' \
                   '-\n' \
                   'Doctor: I suggest you remove the spoon before drinking.'

        elif i == 29:
            joke = "Men 1845: I just killed a buffalo.\n" \
                   "Men 1952: I just fixed the roof.\n" \
                   "Men 2017: I just shaved my legs."

        elif i == 30:
            joke = 'I was sitting in a bar one day and two really large women came in, ' \
                   'talking in an interesting accent. \n' \
                   'So I said, “Cool accent, are you two ladies from Ireland?” \n' \
                   'One of them snarled at me, “It’s Wales, dumbo!” \n' \
                   'So I corrected myself, “Oh, right, so are you two whales from Ireland?”\n' \
                   'That’s about as far as I remember.'

        elif i == 31:
            joke = 'I can’t believe I forgot to go to the gym today. That’s 7 years in a row now.'

        elif i == 32:
            joke = 'The inventor of AutoCorrect is a stupid mass hole. He can fake right off.'

        elif i == 33:
            joke = 'A naked women robbed a bank. Nobody could remember her face.'

        elif i == 34:
            joke = 'A police officer stops a car.\n' \
                   'Officer: “Your driver’s license please.”\n' \
                   'Driver: “I’m really sorry, I forgot.”\n' \
                   'Officer: “At home?”\n' \
                   'Driver: “No, to do it.”'

        elif i == 35:
            joke = 'Why is women’s soccer so rare?\n' \
                   '-\n' \
                   'It’s quite hard to find enough women willing to wear the same outfit.'

        elif i == 36:
            joke = 'I was making Russian tea. Unfortunately I cannot fish the teabag out of the vodka bottle.'

        elif i == 37:
            joke = 'Guest at a restaurant: “I refuse to eat this roastbeef. Please call the manager! “\n' \
                   'Waiter: “That’s no use. He won’t eat it either.”'

        elif i == 38:
            joke = 'So much has changed since my girlfriend told me we’re having a baby. ' \
                   'For instance my name, address and telephone number!'

        elif i == 39:
            joke = 'I heard a report about a bad outbreak of the tummy bug, ' \
                   'apparently 9 out of 10 people there suffered from diarrhea. ' \
                   'I can’t stop thinking about that tenth person who apparently enjoyed it.'

        elif i == 40:
            joke = '“You are so kind, funny and beautiful.” \n' \
                   '“Oh come on. You just want to get me to bed.” \n' \
                   '“And smart, too!”'

        elif i == 41:
            joke = 'Q: What do politicians and diapers have in common? \n' \
                   '-\n' \
                   'A: Both should be changed regularly, and both for the same reason.'

        elif i == 42:
            joke = 'I’m selling my talking parrot. Why? Because yesterday, the bastard tried to sell me.'

        elif i == 43:
            joke = 'Do you know why women aren’t allowed in space? \n' \
                   '-\n' \
                   'To avoid scenarios like: "Houston, we have a problem!" \n' \
                   '- \n' \
                   '"What is the problem?" \n' \
                   '-\n' \
                   '"Yeah, great, pretend like you don’t know what I’m talking about!"'

        elif i == 44:
            joke = 'A husband and a wife sit at the table, having dinner. ' \
                   'The woman drops a bit of tomato sauce on her white top. "Och, I look like a pig!" \n' \
                   'The man nods, "And you dropped tomato sauce on your top!"'

        elif i == 45:
            joke = 'A woman in a bikini reveals about 90% of her body.... ' \
                   'and yet most men are so polite they only look at the covered parts.'

        elif i == 46:
            joke = 'What goes up and down but never moves? \n' \
                   '-\n' \
                   'The stairs!'

        elif i == 47:
            joke = 'Doctor says to his patient: "You have cancer and Alzheimer."\n' \
                   '-\n' \
                   'Patient: "At least I dont have cancer."'

        elif i == 48:
            joke = 'A wife complains to her husband: “Just look at that couple down the road, how lovely they are. ' \
                   'He keeps holding her hand, kissing her, holding the door for her, why can’t you do the same?”\n' \
                   'The husband: “Are you mad? I barely know the woman!”'

        elif i == 49:
            joke = 'Little Johnny asks his father: \n' \
                   '"Where does the wind come from?"\n' \
                   '-\n' \
                   '"I dont know."\n' \
                   '- \n' \
                   '"Why do dogs bark?"\n' \
                   '-\n' \
                   '"I dont know."\n' \
                   '-\n' \
                   '"Why is the earth round?"\n' \
                   '-\n' \
                   '"I dont know."\n' \
                   '-\n' \
                   '"Does it disturb you that I ask so much?"\n' \
                   '-\n' \
                   '"No son. Please ask. Otherwise you will never learn anything."'

        elif i == 50:
            joke = 'Three guys are stranded in a desert. By a stroke of luck, they find a magic genie lamp.\n' \
                   'The genie grants each of them one wish. \n' \
                   'The first guy wishes to be back home. Wish granted. \n' \
                   'The second guy wishes the same. Wish granted. \n' \
                   'The third guy says, "It feels very lonely here now, I wish my friends were with me…” Wish granted.'

        elif i == 51:
            joke = 'They threw me out of the cinema today for bringing my own food. ' \
                   'But come on – the prices are way too high, plus I haven’t had a barbecue in months.'

        elif i == 52:
            joke = 'Two guys are out hunting in the woods when one of them collapses. ' \
                   'He doesn’t appear to be breathing, his eyes are glazed over. ' \
                   'The other man pulls out his phone with trembling fingers and calls 911. ' \
                   'He gasps, "My friend is dead! What can I do?" \n' \
                   'The operator says "Please stay calm. I will help you. First of all, lets make sure he is dead."\n' \
                   'There’s a silence, then a gun shot. The guy gets back on the phone and says "OK, now what?"'

        elif i == 53:
            joke = 'I‘ve decided to run a marathon for charity. ' \
                   'I didn’t want to do it at first, but apparently it’s for blind and disabled kids so ' \
                   'I think I’ve got a good chance of winning.'

        elif i == 54:
            joke = 'Why haven’t you ever seen any elephants hiding up trees? Because they’re really, really good at it.'

        elif i == 55:
            joke = 'We have a strange custom in our office. The food has names there. ' \
                   'Yesterday for example I got me a sandwich out of the fridge and its name was "Michael".'

        elif i == 56:
            joke = 'What is dangerous?\n' \
                   '-\n' \
                   'Sneezing while having diarrhea!'

        elif i == 57:
            joke = 'Secretary: “Doctor the invisible man has come. He says he has an appointment.”\n' \
                   'Doctor: “Tell him I can"t see him.”'

        elif i == 58:
            joke = 'Two elephants meet a totally naked guy. ' \
                   'After a while one elephant says to the other: ' \
                   '“I really don’t get how he can feed himself with that thing!”'

        elif i == 59:
            joke = '"I really dont know which kid Im supposedly being unfair to, according to my wife, ' \
                   'Thomas, Anton, or the fat, ugly one?"'

        elif i == 60:
            joke = '"Grandpa, why dont you have any life insurance?"\n' \
                   '"So you can all be really sad when I die."'

        elif i == 61:
            joke = 'A wife is like a hand grenade. Take off the ring and say good bye to your house.'

        elif i == 62:
            joke = 'Knock, knock.\n' \
                   'Who’s there?\n' \
                   'The love of your life.\n' \
                   'Liar! Chocolate can’t speak!'

        elif i == 63:
            joke = 'A detective asks a woman, "So, your husband hanged himself?" ' \
                   'Woman replies, "Yes, that is correct." ' \
                   'The suspicious detective continues, "But why does he have all those bruises on his head?" \n' \
                   '"The old fool used an elastic rope!"'

        elif i == 64:
            joke = 'Little Red Riding Hood walks all alone through the deep dark wood. ' \
                   'Suddenly she hears rustling in a thick bush. ' \
                   'Cautiously she moves the branches aside and finds herself facing the big bad wolf.\n' \
                   '"Oh, Big Bad Wolf, why do you have such huge red eyes?" \n' \
                   '-\n' \
                   '"Go away! Im crapping!"'

        elif i == 65:
            joke = 'Why don‘t cannibals eat divorced women?\n' \
                   'Because they’re bitter.'

        elif i == 66:
            joke = 'Q. What’s the worst thing about being lonely?\n' \
                   'A. Playing Frisbee.'

        elif i == 67:
            joke = 'Why did the physics teacher break up with the biology teacher? There was no chemistry.'

        elif i == 68:
            joke = 'I’m certain there are female hormones in beer. ' \
                   'When I drink too much, I talk nonsense and I cannot control my car.'

        elif i == 69:
            joke = 'Patient asks his doctor: “Can I take a bath with diarrhea?”\n' \
                   '-\n' \
                   'Doctor: “Yes, if you are able to fill it up. “'

        elif i == 70:
            joke = 'Man: Hi, do you want to dance?\n' \
                   '-\n' \
                   'Woman: Yeah, sure!\n' \
                   '-\n' \
                   'Man: Great, go and dance, I want to talk to your pretty friend!'

        elif i == 71:
            joke = 'My girlfriend says that I am snoopy. ' \
                   'But OK, maybe she meant it differently when she wrote it in her diary.'

        elif i == 72:
            joke = 'Waiter, I am outraged. There is one hair in my soup.\n' \
                   '-\n' \
                   'And what do you expect for this price? A whole wig?!'

        elif i == 73:
            joke = 'I got another letter from this lawyer today. ' \
                   'It said “Final Notice”. Good that he will not bother me anymore.'

        elif i == 74:
            joke = 'Daddy what is a transvestite? \n' \
                   '-\n' \
                   'Ask Mommy, he knows.'

        elif i == 75:
            joke = 'Q: Is Google a he or a she?\n' \
                   'A: A she, no doubt, because it won‘t let you finish your sentence without suggesting other ideas.'

        elif i == 76:
            joke = 'Today I went to a barber’s shop for a shave. ' \
                   'The barber asked me to put a small wooden ball in my mouth so he ' \
                   'could get a closer shave around my cheeks.\n' \
                   'I asked: “But what if I swallow the ball?”\n' \
                   'He replied: “No problem sir, you just bring it back tomorrow like everybody else.”'

        elif i == 77:
            joke = 'What is see-through and smells of carrots? \n' \
                   '-\n' \
                   'A rabbit fart.'

        elif i == 78:
            joke = 'An optimist sees light at the end of a tunnel and thinks it’s an exit. \n' \
                   'A pessimist sees light at the end of a tunnel and assumes it is an onrushing train. \n' \
                   'The train conductor sees two stupid guys staggering on train tracks.'

        elif i == 79:
            joke = 'Job interview in a psychiatry: \n' \
                   'So you’re interested in working with us. What is your experience with mentally disturbed people?\n'\
                   '-\n' \
                   'I’ve been on Facebook for 5 years now.\n' \
                   '-\n' \
                   'Very good, the job is yours.'

        elif i == 80:
            joke = 'Two men are playing golf. ' \
                   'One of them is about to take a swing when a ' \
                   'funeral procession appears on the road next to the course. ' \
                   'He stops mid-swing, takes off his cap, closes his eyes, and bows his head in contemplation. \n' \
                   'His opponent comments: "That must be the most touching thing I’ve ever seen. ' \
                   'You are a very feeling man." ' \
                   'The man, recovering himself, replies, "Yeah, well we were married 35 years."'

        elif i == 81:
            joke = 'Doctor: Your test results are showing you will easily live to be 80. \n' \
                   'Patient: But, wait, I am 80 just now.\n' \
                   'Doctor: See, I told you to live healthier!'

        elif i == 82:
            joke = 'A woman caught her husband on the weight scale, sucking in his stomach.\n' \
                   '“That won’t help you, Joe, you know?”\n' \
                   '“Oh it helps a lot,” says the man, “it’s the only way I can see the numbers!”'

        elif i == 83:
            joke = 'Today I found my first grey pubic hair. ' \
                   'I got really excited, but not as much as the other people in the lift.'

        elif i == 84:
            joke = 'Dentist: “This will hurt a little.”\n' \
                   'Patient: “OK.”\n' \
                   'Dentist: “I’ve been having an affair with your wife for a while now.”'

        elif i == 85:
            joke = 'Why do you see so few black people on ocean cruises?\n' \
                   '-\n' \
                   'Well, they are not going to fall for that one again.'

        elif i == 86:
            joke = 'Yes, money cannot buy you happiness, ' \
                   'but I’d still feel a lot more comfortable crying in a new BMW than on a bike.'

        elif i == 87:
            joke = 'One state official to the other: ' \
                   '"I dont know what people have against us - We have not done anything."'

        elif i == 88:
            joke = 'Don’t be sad when a bird craps on your head. Be happy that dogs can’t fly.'

        else:
            joke = 'Q: Is Google a he or a she?\n' \
                   'A: A she, no doubt, because it won‘t let you finish your sentence without suggesting other ideas.'

        return joke

    except:
        pass
