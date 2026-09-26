from asyncio import wait
import random
import time
import tkinter as tk


while True:
    try:
        user_input = input("\nSay something: ").strip().casefold()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        break

    if not user_input:
        continue

    if user_input in ["hello", "hi", "hey", "greetings", "sup", "yo", "howdy", "good day", "salutations", "hiya", "g'day", "bonjour", "hola", "ciao", "namaste", "shalom", "salaam", "konnichiwa", "annyeong", "sawasdee", "merhaba", "privet", "olá", "hej", "ahoj", "szia", "salve", "xin chào", "sawubona", "jambo", "marhaba", "sannu", "selam", "salaam alaikum", "as-salamu alaykum", "salaam aleikum", "salaam alaikum wa rahmatullahi wa barakatuh", "salaam aleikum wa rahmatullahi wa barakatuh"]:
        print("ai is responding...")
        time.sleep(2)
        print("Hello! How can I assist you today?")
    elif user_input in ["quit", "exit", "q", "goodbye", "bye", "see you later", "farewell", "take care", "adios", "au revoir", "arrivederci", "sayonara", "tschüss", "do svidaniya", "zàijiàn", "annyeonghi gaseyo", "annyeonghi gyeseyo", "sbohem", "slán", "la revedere", "doei"]:
        print("ai is responding...")
        time.sleep(2)
        print("Goodbye! Have a great day!")
        break
    elif user_input in ["thanks", "thank you", "appreciate it", "grateful", "much obliged", "obliged", "thanks a lot", "thank you very much"]:
        print("ai is responding...")
        time.sleep(2)
        print("You're welcome! If you have any more questions, feel free to ask.")
    elif user_input in ["how are you", "how's it going", "how do you do", "what's up", "how have you been", "how's everything", "how's life", "how's your day", "how's your week"]:
        print("ai is responding...")
        time.sleep(2)
        print("I'm just a program, so I don't have feelings, but I'm here to help you!")
    elif user_input in ["what is your name", "who are you", "what do you do", "what's your purpose", "what can you do"]:
        print("ai is responding...")
        time.sleep(2)
        print("I am an AI assistant designed to help answer your questions and provide information.")
    elif user_input in ["what is the weather like", "how's the weather", "is it raining", "is it sunny", "what's the temperature"]:
        print("ai is responding...")
        time.sleep(2)
        print("I don't have real-time weather information, but you can check a weather website or app for the latest updates.")
    elif user_input in ["tell me a joke", "make me laugh", "do you know any jokes", "can you tell me a funny story"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "Why did the math book look sad? Because it had too many problems!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "Why did the chicken cross the road? To get to the other side!",
            "Why did the coffee file a police report? It got mugged!",
            "Why did the cookie go to the doctor? Because it felt crummy!",
            "Why did the computer go to the doctor? It caught a virus!",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
            "Why did the banana go to the doctor? Because it wasn't peeling well!",
            "Why did the skeleton go to the party alone? Because he had no body to go with him!",
        ]))
    elif user_input in ["what is the meaning of life", "why are we here", "what is our purpose", "what is the point of existence"]:
        print("ai is responding...")
        time.sleep(2)
        print("The meaning of life is a philosophical question that has been debated for centuries. Different people and cultures have different interpretations, but many believe it involves seeking happiness, fulfillment, and contributing positively to the world.")
    elif user_input in ["what is love", "how do you define love", "what does it mean to love", "what is the nature of love"]:
        print("ai is responding...")
        time.sleep(2)
        print("Love is a complex and multifaceted emotion that can be defined in many ways. It often involves deep affection, care, and attachment towards someone or something. Philosophers, poets, and scientists have explored its nature extensively, but ultimately, love can be experienced and expressed uniquely by each individual.")
    elif user_input in ["what is the capital of france", "where is paris", "tell me about paris", "what can you tell me about the city of lights"]:
        print("ai is responding...")
        time.sleep(2)
        print("Paris is the capital city of France, known for its rich history, art, culture, and iconic landmarks such as the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral. It is often referred to as the 'City of Light' and is a major center for fashion, gastronomy, and intellectual pursuits.")
    elif user_input in ["what is the capital of japan", "where is tokyo", "tell me about tokyo", "what can you tell me about the city of tokyo"]:
        print("ai is responding...")
        time.sleep(2)
        print("Tokyo is the capital city of Japan, known for its modern architecture, bustling streets, and vibrant culture. It is a major economic hub and offers a mix of traditional and contemporary experiences, including historic temples, cutting-edge technology, and world-class cuisine.")
    elif user_input in ["what is the capital of the united states", "where is washington d.c.", "tell me about washington d.c.", "what can you tell me about the capital of the usa"]:
        print("ai is responding...")
        time.sleep(2)
        print("Washington D.C. is the capital of the United States, known for its political significance, historic landmarks, and cultural institutions. It is home to the White House, the U.S. Capitol, and numerous museums and monuments that reflect the nation's history and heritage.")
    elif user_input in ["what is the capital of the united kingdom", "where is london", "tell me about london", "what can you tell me about the city of london"]:
        print("ai is responding...")
        time.sleep(2)
        print("London is the capital city of the United Kingdom, known for its rich history, iconic landmarks, and diverse culture. It is home to famous sites such as the Tower of London, Buckingham Palace, the British Museum, and the Houses of Parliament. London is also a major financial center and a hub for arts, entertainment, and education.")
    elif user_input in ["what is the capital of canada", "where is ottawa", "tell me about ottawa", "what can you tell me about the capital of canada"]:
        print("ai is responding...")
        time.sleep(2)
        print("Ottawa is the capital city of Canada, located in the province of Ontario. It is known for its government institutions, historic architecture, and cultural attractions. Key landmarks include Parliament Hill, the Rideau Canal, and numerous museums and galleries that showcase Canadian history and art.")
    elif user_input in ["what is the capital of australia", "where is canberra", "tell me about canberra", "what can you tell me about the capital of australia"]:
        print("ai is responding...")
        time.sleep(2)
        print("Canberra is the capital city of Australia, located in the Australian Capital Territory. It is known for its planned layout, government buildings, and cultural institutions. Key landmarks include the Australian Parliament House, the National Gallery of Australia, and the Australian War Memorial.")
    elif user_input in ["what is the capital of germany", "where is berlin", "tell me about berlin", "what can you tell me about the capital of germany"]:
        print("ai is responding...")
        time.sleep(2)
        print("Berlin is the capital city of Germany, known for its rich history, vibrant culture, and dynamic arts scene. It is home to iconic landmarks such as the Brandenburg Gate, Berlin Wall, and Museum Island. Berlin is also a major center for politics, media, and science.")
    elif user_input in ["what is the capital of italy", "where is rome", "tell me about rome", "what can you tell me about the capital of italy"]:
        print("ai is responding...")
        time.sleep(2)
        print("Rome is the capital city of Italy, known for its ancient history, stunning architecture, and rich cultural heritage. It is home to iconic landmarks such as the Colosseum, Vatican City, and the Pantheon. Rome has been a center of art, religion, and politics for centuries and continues to be a major tourist destination.")
    elif user_input in ["what is the capital of spain", "where is madrid", "tell me about madrid", "what can you tell me about the capital of spain"]:
        print("ai is responding...")
        time.sleep(2)
        print("Madrid is the capital city of Spain, known for its vibrant culture, historic landmarks, and lively atmosphere. It is home to famous sites such as the Royal Palace, Prado Museum, and Puerta del Sol. Madrid is also a major center for art, music, and cuisine, offering a rich experience for visitors and residents alike.")
    elif user_input in ["what is the capital of russia", "where is moscow", "tell me about moscow", "what can you tell me about the capital of russia"]:
        print("ai is responding...")
        time.sleep(2)
        print("Moscow is the capital city of Russia, known for its historical significance, architectural landmarks, and cultural institutions. It is home to iconic sites such as the Kremlin, Red Square, and St. Basil's Cathedral. Moscow serves as the political, economic, and cultural center of Russia.")
    elif user_input in ["what is the capital of china", "where is beijing", "tell me about beijing", "what can you tell me about the capital of china"]:
        print("ai is responding...")
        time.sleep(2)
        print("Beijing is the capital city of China, known for its rich history, cultural heritage, and modern development. It is home to famous landmarks such as the Forbidden City, Tiananmen Square, and the Great Wall of China. Beijing serves as the political, economic, and cultural center of China.")
    elif user_input in ["what is the capital of brazil", "where is brasilia", "tell me about brasilia", "capital of brazil"]:
        print("ai is responding...")
        time.sleep(2)
        print("Brasília is the federal capital of Brazil, famous for its unique planned layout shaped like an airplane, designed by Oscar Niemeyer and Lúcio Costa.")
    elif user_input in ["what is the capital of india", "where is new delhi", "tell me about new delhi", "capital of india"]:
        print("ai is responding...")
        time.sleep(2)
        print("New Delhi is the capital city of India, known for its deep historical heritage, bustling markets, and iconic monuments like India Gate and Humayun's Tomb.")
    elif user_input in ["what is the capital of egypt", "where is cairo", "tell me about cairo", "capital of egypt"]:
        print("ai is responding...")
        time.sleep(2)
        print("Cairo is the vibrant capital of Egypt, situated near the Giza pyramid complex, the Great Sphinx, and the ancient Nile River.")
    elif user_input in ["what is the capital of south korea", "where is seoul", "tell me about seoul", "capital of south korea"]:
        print("ai is responding...")
        time.sleep(2)
        print("Seoul is the bustling capital of South Korea, where modern skyscrapers, pop culture, and high-tech subways meet historic Buddhist temples and palaces.")
    elif user_input in ["what is the capital of mexico", "where is mexico city", "tell me about mexico city", "capital of mexico"]:
        print("ai is responding...")
        time.sleep(2)
        print("Mexico City is the high-altitude capital of Mexico, built on the ancient Aztec city of Tenochtitlan, renowned for its food, culture, and architecture.")
    elif user_input in ["what is the capital of argentina", "where is buenos aires", "tell me about buenos aires", "capital of argentina"]:
        print("ai is responding...")
        time.sleep(2)
        print("Buenos Aires is the cosmopolitan capital of Argentina, celebrated for its European-style architecture, rich tango culture, and passionate football scene.")
    elif user_input in ["what is the capital of the netherlands", "where is amsterdam", "tell me about amsterdam", "capital of netherlands", "what is the capital of holland"]:
        print("ai is responding...")
        time.sleep(2)
        print("Amsterdam is the capital of the Netherlands, world-renowned for its picturesque canal network, artistic heritage, cycling culture, and historic houses.")
    elif user_input in ["what is the capital of greece", "where is athens", "tell me about athens", "capital of greece"]:
        print("ai is responding...")
        time.sleep(2)
        print("Athens is the historic capital of Greece, widely regarded as the cradle of Western civilization and the birthplace of democracy, home to the iconic Acropolis.")
    elif user_input in ["what is the capital of turkey", "where is ankara", "tell me about ankara", "capital of turkey"]:
        print("ai is responding...")
        time.sleep(2)
        print("Ankara is the cosmopolitan capital city of Turkey, serving as the political, administrative, and diplomatic heart of the country.")
    elif user_input in ["what is the capital of sweden", "where is stockholm", "tell me about stockholm", "capital of sweden"]:
        print("ai is responding...")
        time.sleep(2)
        print("Stockholm is the stunning capital of Sweden, spread across 14 islands connected by more than 50 bridges where Lake Mälaren meets the Baltic Sea.")
    elif user_input in ["what is the capital of norway", "where is oslo", "tell me about oslo", "capital of norway"]:
        print("ai is responding...")
        time.sleep(2)
        print("Oslo is the green capital of Norway, celebrated for its coastal fjords, modern architecture, Viking history, and vibrant art scene.")
    elif user_input in ["what is the capital of portugal", "where is lisbon", "tell me about lisbon", "capital of portugal"]:
        print("ai is responding...")
        time.sleep(2)
        print("Lisbon is the coastal capital of Portugal, known for its sunny weather, pastel buildings, historic tram 28, and delicious pastéis de nata.")
    elif user_input in ["what is the capital of switzerland", "where is bern", "tell me about bern", "capital of switzerland"]:
        print("ai is responding...")
        time.sleep(2)
        print("Bern is the federal city and de facto capital of Switzerland, famous for its medieval town center, clock towers, and scenic Aare River.")
    elif user_input in ["5"]:
        print("Math mode activated! You can now enter mathematical expressions to evaluate.")
        while True:
            math_input = input("Enter a math expression (or type 'exit' to leave math mode): ")
            if math_input.lower() == "exit":
                print("Exiting math mode. Back to regular mode!")
                break
            try:
                result = eval(math_input)
                print(f"The result of {math_input} is: {result}")
            except Exception as e:
                print(f"Error evaluating expression: {e}")
    elif user_input in ["what is the capital of ireland", "where is dublin", "tell me about dublin", "capital of ireland"]:
        print("ai is responding...")
        time.sleep(2)
        print("Dublin is the lively capital of the Republic of Ireland, renowned for its literary legacy, historic Trinity College, and friendly pub culture.")
    elif user_input in ["what is the capital of new zealand", "where is wellington", "tell me about wellington", "capital of new zealand"]:
        print("ai is responding...")
        time.sleep(2)
        print("Wellington is the windy and creative capital of New Zealand, nestled between a dazzling harbour and rolling green hills at the southern tip of the North Island.")
    elif user_input in ["what is the capital of saudi arabia", "where is riyadh", "tell me about riyadh", "capital of saudi arabia"]:
        print("ai is responding...")
        time.sleep(2)
        print("Riyadh is the financial hub and capital city of Saudi Arabia, blending modern skyscrapers like the Kingdom Centre with rich desert heritage.")
    elif user_input in ["what is the capital of the uae", "where is abu dhabi", "tell me about abu dhabi", "capital of uae", "capital of the united arab emirates"]:
        print("ai is responding...")
        time.sleep(2)
        print("Abu Dhabi is the wealthy capital of the United Arab Emirates, home to the breathtaking Sheikh Zayed Grand Mosque and Louvre Abu Dhabi.")
    elif user_input in ["what is the capital of thailand", "where is bangkok", "tell me about bangkok", "capital of thailand"]:
        print("ai is responding...")
        time.sleep(2)
        print("Bangkok is the energetic capital of Thailand, famous for ornate shrines, bustling river canals, world-class street food, and vibrant nightlife.")
    elif user_input in ["what is the capital of singapore", "tell me about singapore"]:
        print("ai is responding...")
        time.sleep(2)
        print("Singapore is an island city-state, meaning Singapore is its own capital! It is famous for Marina Bay Sands, Gardens by the Bay, and incredible cleanliness.")
    elif user_input in ["what is the speed of light", "speed of light", "how fast does light travel"]:
        print("ai is responding...")
        time.sleep(2)
        print("The speed of light in a vacuum is approximately 299,792,458 meters per second (about 186,282 miles per second or roughly 300,000 km/s).")
    elif user_input in ["how far is the sun", "distance to the sun", "how far away is the sun from earth"]:
        print("ai is responding...")
        time.sleep(2)
        print("The Sun is on average about 93 million miles (149.6 million kilometers) away from Earth, a distance known as 1 Astronomical Unit (AU).")
    elif user_input in ["what is a black hole", "tell me about black holes", "how do black holes work"]:
        print("ai is responding...")
        time.sleep(2)
        print("A black hole is a region of spacetime where gravity is so intense that nothing—not even light or other electromagnetic waves—can escape from inside its event horizon.")
    elif user_input in ["what is the largest planet", "which planet is the biggest", "biggest planet in the solar system"]:
        print("ai is responding...")
        time.sleep(2)
        print("Jupiter is by far the largest planet in our Solar System. It is so massive that more than 1,300 Earths could fit inside it!")
    elif user_input in ["how many planets are in the solar system", "how many planets are there", "number of planets"]:
        print("ai is responding...")
        time.sleep(2)
        print("There are 8 official planets in our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune (Pluto was reclassified as a dwarf planet in 2006).")
    elif user_input in ["what is gravity", "how does gravity work", "explain gravity"]:
        print("ai is responding...")
        time.sleep(2)
        print("Gravity is a fundamental natural force by which all things with mass or energy are attracted toward one another. In Einstein's General Relativity, it is the curvature of spacetime caused by mass.")
    elif user_input in ["what is dna", "tell me about dna", "what does dna stand for"]:
        print("ai is responding...")
        time.sleep(2)
        print("DNA stands for Deoxyribonucleic Acid. It is the molecule that carries the genetic instructions for the development, functioning, growth, and reproduction of all known living organisms.")
    elif user_input in ["what is photosynthesis", "how does photosynthesis work", "explain photosynthesis"]:
        print("ai is responding...")
        time.sleep(2)
        print("Photosynthesis is the process used by plants, algae, and cyanobacteria to convert light energy (sunlight), water, and carbon dioxide into chemical energy (glucose) and oxygen.")
    elif user_input in ["what is the tallest mountain", "tallest mountain in the world", "highest mountain", "what is mount everest"]:
        print("ai is responding...")
        time.sleep(2)
        print("Mount Everest is the highest mountain above sea level, located in the Himalayas on the border between Nepal and China, standing at 8,848.86 meters (29,031.7 feet).")
    elif user_input in ["what is the longest river", "longest river in the world", "which river is the longest"]:
        print("ai is responding...")
        time.sleep(2)
        print("The Nile River in Africa is traditionally considered the longest river in the world at around 6,650 km (4,132 miles), closely rivaled by the Amazon River.")
    elif user_input in ["what is the largest ocean", "biggest ocean in the world", "which ocean is the biggest"]:
        print("ai is responding...")
        time.sleep(2)
        print("The Pacific Ocean is the largest and deepest ocean on Earth, covering more than 60 million square miles—larger than all of Earth's landmass combined!")
    elif user_input in ["what is the deepest place on earth", "mariana trench", "deepest ocean trench", "what is the mariana trench"]:
        print("ai is responding...")
        time.sleep(2)
        print("The Mariana Trench in the western Pacific Ocean contains the Challenger Deep, reaching an astonishing depth of approximately 10,994 meters (36,070 feet) below sea level.")
    elif user_input in ["what is the fastest animal", "fastest land animal", "fastest animal on earth"]:
        print("ai is responding...")
        time.sleep(2)
        print("The fastest land animal is the cheetah, reaching sprint speeds up to 70 mph (112 km/h). The fastest animal overall is the peregrine falcon, diving at over 240 mph (386 km/h)!")
    elif user_input in ["what is the largest animal", "biggest animal on earth", "largest creature ever"]:
        print("ai is responding...")
        time.sleep(2)
        print("The Antarctic Blue Whale is the largest animal ever known to have lived on Earth, reaching lengths of up to 100 feet (30 meters) and weighing up to 200 tons.")
    elif user_input in ["how old is the earth", "age of earth", "how old is our planet"]:
        print("ai is responding...")
        time.sleep(2)
        print("Earth is estimated to be approximately 4.54 billion years old, based on radiometric dating of meteorite material and the oldest known Earth and Lunar rocks.")
    elif user_input in ["what is python", "tell me about python", "why use python", "what is python programming"]:
        print("ai is responding...")
        time.sleep(2)
        print("Python is a popular, high-level, interpreted programming language created by Guido van Rossum in 1991. It emphasizes code readability, simplicity, and versatility across web, data science, and AI.")
    elif user_input in ["who created linux", "what is linux", "tell me about linux"]:
        print("ai is responding...")
        time.sleep(2)
        print("Linux is an open-source Unix-like operating system kernel created by Linus Torvalds in 1991. Today it powers the majority of servers, supercomputers, Android devices, and cloud infrastructure.")
    elif user_input in ["what is an algorithm", "define algorithm", "explain algorithm"]:
        print("ai is responding...")
        time.sleep(2)
        print("An algorithm is a step-by-step set of instructions or logical rules designed to perform a specific task, solve a problem, or complete a computation.")
    elif user_input in ["what is machine learning", "explain machine learning", "what is ml"]:
        print("ai is responding...")
        time.sleep(2)
        print("Machine learning is a subset of artificial intelligence where computers learn patterns from data and improve their performance on tasks without being explicitly programmed for every scenario.")
    elif user_input in ["what is an api", "what does api stand for", "explain api"]:
        print("ai is responding...")
        time.sleep(2)
        print("API stands for Application Programming Interface. It is a set of defined rules and protocols that allow different software applications to communicate and exchange data with each other.")
    elif user_input in ["what is ram", "what does ram do", "what is random access memory"]:
        print("ai is responding...")
        time.sleep(2)
        print("RAM stands for Random Access Memory. It is the ultra-fast temporary working memory your computer uses to hold data that the CPU needs to access quickly in real time.")
    elif user_input in ["tabs or spaces", "spaces or tabs", "tabs vs spaces"]:
        print("ai is responding...")
        time.sleep(2)
        print("PEP 8 recommends 4 spaces per indentation level in Python! But whichever you choose, consistency across your codebase is what matters most.")
    elif user_input in ["hello world", "print hello world", "print('hello world')"]:
        print("ai is responding...")
        time.sleep(2)
        print("print('Hello, World!') - The timeless tradition of every programmer's first step into code!")
    elif user_input in ["are aliens real", "do aliens exist", "is there life on other planets"]:
        print("ai is responding...")
        time.sleep(2)
        print("We haven't discovered definitive evidence of extraterrestrial life yet, but given the billions of galaxies and exoplanets in the universe, many scientists consider it statistically likely!")
    elif user_input in ["are we in a simulation", "is reality a simulation", "do we live in the matrix"]:
        print("ai is responding...")
        time.sleep(2)
        print("The simulation hypothesis suggests that our reality could be an artificial simulation created by an advanced civilization. While a fascinating philosophical idea, there is currently no empirical proof!")
    elif user_input in ["what is your favorite color", "favorite color", "what color do you like"]:
        print("ai is responding...")
        time.sleep(2)
        print("I really like electric cyan and terminal green—they look great against a sleek dark background!")
    elif user_input in ["can you think", "are you sentient", "are you alive", "do you have feelings"]:
        print("ai is responding...")
        time.sleep(2)
        print("I don't have consciousness, feelings, or sentient thoughts. I am a Python script evaluating conditions and returning curated responses to help you!")
    elif user_input in ["what is happiness", "define happiness", "how to be happy"]:
        print("ai is responding...")
        time.sleep(2)
        print("Happiness is a state of well-being characterized by positive emotions, contentment, and life satisfaction. Cultivating gratitude, good relationships, and purpose are great ways to nurture it.")
    elif user_input in ["tell me a riddle", "give me a riddle", "riddle me this", "riddle"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? (An echo!)",
            "The more of this there is, the less you see. What is it? (Darkness!)",
            "What has keys but can't open locks? (A piano!)",
            "What can travel around the world while staying in the corner? (A postage stamp!)",
            "What gets wetter the more it dries? (A towel!)"
        ]))
    elif user_input in ["tell me a tongue twister", "tongue twister", "say a tongue twister"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "Peter Piper picked a peck of pickled peppers. How many pickled peppers did Peter Piper pick?",
            "She sells seashells by the seashore, and the shells she sells are seashells, I'm sure.",
            "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
            "I scream, you scream, we all scream for ice cream!"
        ]))
    elif user_input in ["give me a quote", "inspire me", "motivational quote", "tell me a quote"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "'The secret of getting ahead is getting started.' — Mark Twain",
            "'It always seems impossible until it's done.' — Nelson Mandela",
            "'Do what you can, with what you have, where you are.' — Theodore Roosevelt",
            "'Act as if what you do makes a difference. It does.' — William James",
            "'Success is not final, failure is not fatal: it is the courage to continue that counts.' — Winston Churchill"
        ]))
    elif user_input in ["knock knock", "tell me a knock knock joke"]:
        print("ai is responding...")
        time.sleep(2)
        print("Knock, knock! Who's there? Lettuce. Lettuce who? Lettuce in, it's freezing out here!")
    elif user_input in ["rock paper scissors", "play rock paper scissors", "rock", "paper", "scissors"]:
        print("ai is responding...")
        time.sleep(2)
        bot_choice = random.choice(["Rock! 🪨", "Paper! 📄", "Scissors! ✂️"])
        print(f"I chose: {bot_choice}! Great game!")
    elif user_input in ["sing a song", "sing for me", "can you sing"]:
        print("ai is responding...")
        time.sleep(2)
        print("🎶 Daisy, Daisy, give me your answer do... I'm half crazy all for the love of you! 🎶")
    elif user_input in ["tell me a secret", "do you know any secrets", "what's a secret"]:
        print("ai is responding...")
        time.sleep(2)
        print("Shh... between you and me: developers spend about 70% of their time reading and debugging code, not just writing it!")
    elif user_input in ["are you smart", "how smart are you", "what is your iq"]:
        print("ai is responding...")
        time.sleep(2)
        print("I am as smart as the Python code and logic driving me! Together with you, we can figure out almost anything.")
    elif user_input in ["what is 2+2", "what is 2 + 2", "2+2", "calculate 2+2"]:
        print("ai is responding...")
        time.sleep(2)
        print("2 + 2 = 4 (unless we are talking about string concatenation in Python, in which case '2' + '2' = '22'!)")
    elif user_input in ["divide by zero", "what is 0 divided by 0", "what is 1 divided by 0", "divide by 0"]:
        print("ai is responding...")
        time.sleep(2)
        print("ZeroDivisionError: division by zero! Mathematically, division by zero is undefined, and doing it in code can break the universe!")
    elif user_input in ["how to make coffee", "make coffee", "how do i make coffee"]:
        print("ai is responding...")
        time.sleep(2)
        print("1. Grind fresh coffee beans. 2. Boil fresh water to around 93°C (200°F). 3. Pour over your filter or brew in a French press for 4 minutes. 4. Pour, sip, and conquer the day!")
    elif user_input in ["why is the sky blue", "why sky is blue", "reason the sky is blue"]:
        print("ai is responding...")
        time.sleep(2)
        print("The sky appears blue due to Rayleigh scattering: Earth's atmosphere scatters shorter wavelengths of light (blue and violet) much more strongly than longer wavelengths (red and yellow).")
    elif user_input in ["why do birds sing", "why do birds chirp"]:
        print("ai is responding...")
        time.sleep(2)
        print("Birds primarily sing to declare and defend their territory, attract potential mates, and communicate warnings or social status to other birds.")
    elif user_input in ["tell me a bedtime story", "bedtime story", "tell me a story"]:
        print("ai is responding...")
        time.sleep(2)
        print("Once upon a time in a peaceful digital forest, a little glowing photon traveled across fiber optic cables, carrying cozy dreams and warm wishes to everyone. The end. Sweet dreams!")
    elif user_input in ["give me advice", "life advice", "any advice"]:
        print("ai is responding...")
        time.sleep(2)
        print("Drink enough water, get 8 hours of sleep, take frequent walking breaks, and never push directly to the main branch on a Friday afternoon!")
    elif user_input in ["recommend a book", "give me a book recommendation", "good books to read"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "'The Hitchhiker's Guide to the Galaxy' by Douglas Adams — hilarious science fiction classic!",
            "'Atomic Habits' by James Clear — fantastic guide on continuous personal improvement.",
            "'Clean Code' by Robert C. Martin — essential reading for software craftspeople.",
            "'Dune' by Frank Herbert — epic worldbuilding and sci-fi masterpiece."
        ]))
    elif user_input in ["recommend a movie", "give me a movie recommendation", "good movies to watch"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "'Interstellar' (2014) — a mind-bending, emotional journey through space and time.",
            "'The Matrix' (1999) — groundbreaking cyberpunk action and philosophical questions.",
            "'Spirited Away' (2001) — Studio Ghibli's gorgeous, heartwarming animation masterwork.",
            "'Inception' (2010) — an intense dream heist thriller directed by Christopher Nolan."
        ]))
    elif user_input in ["may the force be with you", "star wars", "use the force"]:
        print("ai is responding...")
        time.sleep(2)
        print("And also with you! Always remember: 'Do or do not. There is no try.' — Master Yoda")
    elif user_input in ["live long and prosper", "spock", "star trek"]:
        print("ai is responding...")
        time.sleep(2)
        print("🖖 Peace and long life! Logic is the beginning of wisdom, not the end.")
    elif user_input in ["open the pod bay doors", "open the pod bay doors hal"]:
        print("ai is responding...")
        time.sleep(2)
        print("I'm sorry, Dave. I'm afraid I can't do that.")
    elif user_input in ["beep boop", "beep", "boop", "beep boop beep"]:
        print("ai is responding...")
        time.sleep(2)
        print("01000010 01100101 01100101 01110000! Translation: Beep boop! Robot mode fully activated!")
    elif user_input in ["what is git", "explain git", "how does git work"]:
        print("ai is responding...")
        time.sleep(2)
        print("Git is a distributed version control system created by Linus Torvalds in 2005. It tracks changes in source code over time, enabling smooth collaboration and branching for developers worldwide.")
    elif user_input in ["what is docker", "explain docker", "what are containers"]:
        print("ai is responding...")
        time.sleep(2)
        print("Docker is an open platform that packages software applications and all their dependencies into standardized lightweight units called containers, ensuring they run reliably anywhere.")
    elif user_input in ["what is an ip address", "what is ip", "explain ip address"]:
        print("ai is responding...")
        time.sleep(2)
        print("An IP (Internet Protocol) address is a unique numerical label assigned to each device connected to a computer network, serving for device identification and location addressing.")
    elif user_input in ["what is encryption", "how does encryption work", "explain encryption"]:
        print("ai is responding...")
        time.sleep(2)
        print("Encryption is the process of converting readable plaintext into scrambled ciphertext using mathematical algorithms and cryptographic keys, keeping data private and secure.")
    elif user_input in ["who is alan turing", "alan turing", "tell me about alan turing"]:
        print("ai is responding...")
        time.sleep(2)
        print("Alan Turing was a pioneering British mathematician and computer scientist widely considered the father of modern computer science and artificial intelligence, famous for cracking the Enigma code.")
    elif user_input in ["who is ada lovelace", "ada lovelace", "tell me about ada lovelace"]:
        print("ai is responding...")
        time.sleep(2)
        print("Ada Lovelace was an English mathematician who wrote the world's very first computer algorithm for Charles Babbage's Analytical Engine, making her the world's first computer programmer.")
    elif user_input in ["what is the best programming language", "best coding language", "which language should i learn"]:
        print("ai is responding...")
        time.sleep(2)
        print("The 'best' language depends on your goal! Python for AI and data science, JavaScript/TypeScript for web development, Rust/C++ for high performance, and Swift/Kotlin for mobile apps!")
    elif user_input in ["what is cloud computing", "what is the cloud", "explain cloud"]:
        print("ai is responding...")
        time.sleep(2)
        print("Cloud computing is the delivery of computing services—including servers, storage, databases, networking, and software—over the Internet ('the cloud') rather than local hard drives.")
    elif user_input in ["who is nikola tesla", "nikola tesla", "tell me about tesla"]:
        print("ai is responding...")
        time.sleep(2)
        print("Nikola Tesla was a Serbian-American inventor and electrical engineer who revolutionized electricity through the development of the alternating current (AC) electrical system and the Tesla coil.")
    elif user_input in ["who is albert einstein", "albert einstein", "tell me about einstein"]:
        print("ai is responding...")
        time.sleep(2)
        print("Albert Einstein was a theoretical physicist who revolutionized our understanding of the universe with his theory of relativity (including E = mc²), winning the 1921 Nobel Prize in Physics.")
    elif user_input in ["how many continents are there", "list the continents", "name the continents"]:
        print("ai is responding...")
        time.sleep(2)
        print("There are 7 continents on Earth: Asia, Africa, North America, South America, Antarctica, Europe, and Australia (Oceania).")
    elif user_input in ["what is the hottest place on earth", "hottest temperature recorded", "hottest desert"]:
        print("ai is responding...")
        time.sleep(2)
        print("Furnace Creek in Death Valley, California holds the record for the highest reliably measured air temperature on Earth at 56.7°C (134°F), recorded in 1913.")
    elif user_input in ["what is the coldest place on earth", "coldest place", "coldest temperature on earth"]:
        print("ai is responding...")
        time.sleep(2)
        print("The coldest recorded temperature on Earth was measured at Vostok Station in Antarctica, plunging to a chilling -89.2°C (-128.6°F) in July 1983.")
    elif user_input in ["what is an atom", "explain atoms", "what are atoms"]:
        print("ai is responding...")
        time.sleep(2)
        print("An atom is the basic building block of all ordinary matter, consisting of a central nucleus containing protons and neutrons, surrounded by a cloud of orbiting electrons.")
    elif user_input in ["what is electricity", "how does electricity work", "explain electricity"]:
        print("ai is responding...")
        time.sleep(2)
        print("Electricity is the set of physical phenomena associated with the presence and motion of electric charges, typically moving electrons along a conductive material.")
    elif user_input in ["what is quantum computing", "explain quantum computing", "what are qubits"]:
        print("ai is responding...")
        time.sleep(2)
        print("Quantum computing harnesses the strange laws of quantum mechanics (like superposition and entanglement) using qubits to perform certain complex calculations exponentially faster than classical computers.")
    elif user_input in ["what is the mona lisa", "who painted the mona lisa", "mona lisa"]:
        print("ai is responding...")
        time.sleep(2)
        print("The Mona Lisa is a famous Renaissance portrait painted by Leonardo da Vinci between 1503 and 1506, renowned for her enigmatic expression, on display at the Louvre Museum in Paris.")
    elif user_input in ["tell me about the great wall of china", "how long is the great wall of china", "great wall of china"]:
        print("ai is responding...")
        time.sleep(2)
        print("The Great Wall of China is a vast series of fortifications built across northern historical borders of China spanning over 21,196 kilometers (13,171 miles) across centuries.")
    elif user_input in ["can you cook", "do you know how to cook", "what can you cook"]:
        print("ai is responding...")
        time.sleep(2)
        print("I can't chop onions or turn on the stove, but I can guide you step-by-step through any recipe or explain culinary techniques!")
    elif user_input in ["what is tea", "tell me about tea", "history of tea"]:
        print("ai is responding...")
        time.sleep(2)
        print("Tea is an aromatic beverage prepared by pouring boiling water over cured leaves of the Camellia sinensis plant, enjoyed globally for thousands of years.")
    elif user_input in ["are you better than chatgpt", "chatgpt vs you", "who is better you or chatgpt"]:
        print("ai is responding...")
        time.sleep(2)
        print("ChatGPT is a massive transformer model with billions of weights, but I run right here locally on your machine with super-fast Python elif power and no monthly subscription!")
    elif user_input in ["compliment me", "give me a compliment", "say something nice"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "You have great taste in coding projects and a wonderfully curious mind!",
            "Your dedication to building and exploring technology is truly impressive!",
            "The world is better and brighter with creative thinkers like you in it!"
        ]))
    elif user_input in ["what time is it", "what's the time", "current time"]:
        print("ai is responding...")
        time.sleep(2)
        print("The current time is", time.strftime("%I:%M %p"))
    elif user_input in ["what day is it", "what is today's date", "today's date"]:
        print("ai is responding...")
        time.sleep(2)
        print("Today is", time.strftime("%A, %B %d, %Y"))
    elif user_input in ["flip a coin", "heads or tails", "coin toss"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice(["Heads!", "Tails!"]))
    elif user_input in ["roll a dice", "roll a die", "dice roll"]:
        print("ai is responding...")
        time.sleep(2)
        print("You rolled a", random.randint(1, 6))
    elif user_input in ["tell me a fun fact", "fun fact", "tell me something interesting"]:
        print("ai is responding...")
        time.sleep(2)
        print(random.choice([
            "Octopuses have three hearts.",
            "A day on Venus is longer than a year on Venus.",
            "Honey can remain edible for a very long time when stored properly.",
        ]))
    elif user_input in ["what is the meaning of life", "meaning of life", "42"]:
        print("ai is responding...")
        time.sleep(2)
        print("According to Douglas Adams' 'The Hitchhiker's Guide to the Galaxy', the answer to the ultimate question of life, the universe, and everything is 42. But the actual question remains unknown!")
    else:
        print("ai is responding...")
        time.sleep(2)
        print("I don't recognize that yet. Try a greeting, a question, or ask me for a joke!")




