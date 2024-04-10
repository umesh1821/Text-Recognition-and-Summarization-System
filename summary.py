import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

class summary:

    def summary(text):
        stopwords = list(STOP_WORDS)
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        #print(doc)
        tokens = [token.text for token in doc]
        #print(tokens)

        word_freq={}
        for word in doc:
            if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                if word.text not in word_freq.keys():
                    word_freq[word.text] = 1
                else:
                    word_freq[word.text]+=1

        #print(word_freq)

        max_freq = max(word_freq.values())

        #print(max_freq)

        for word in word_freq.keys():
            word_freq[word] /= max_freq

        # print(word_freq)

        sent_tokens = [sent for sent in doc.sents]

        #print(sent_tokens)

        sent_scores = {}

        for sent in sent_tokens:
            for word in sent:
                if word.text in word_freq.keys():
                    if sent not in sent_scores.keys():
                        sent_scores[sent] = word_freq[word.text]
                    else:
                        sent_scores[sent]+= word_freq[word.text]

        # print(sent_scores)

        length = int(len(sent_tokens)*0.3)
        #print(length)

        summary = nlargest(length , sent_scores , key=sent_scores.get)

        #print(summary)

        final_summary = [word.text for word in summary]
        summary = " ".join(final_summary)

        print(summary)



 text="""Elon Reeve Musk (/ˈiːlɒn/; EE-lon; born June 28, 1971) is a businessman and investor. He is the founder, chairman, CEO, and CTO of SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the wealthiest people in the world, with an estimated net worth of US$190 billion as of March 2024, according to the Bloomberg Billionaires Index, and $195 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.[5][6]

A member of the wealthy South African Musk family, Elon was born in Pretoria and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania, and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999, and that same year Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal.

In October 2002, eBay acquired PayPal for $1.5 billion, and that same year, with $100 million of the money he made, Musk founded SpaceX, a spaceflight services company. In 2004, he became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and the Boring Company, a tunnel construction company. In 2022, he acquired Twitter for $44 billion. He subsequently merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, he founded xAI, an artificial intelligence company.

Musk has expressed views that have made him a polarizing figure.[7] He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation and antisemitic conspiracy theories.[7][8][9][10] His ownership of Twitter has been similarly controversial, being marked by the laying off of a large number of employees, an increase in hate speech and misinformation and disinformation on the website, as well as changes to Twitter Blue verification. In 2018, the U.S. Securities and Exchange Commission (SEC) sued him, alleging that he had falsely announced that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a $20 million fine.

Early life and education
Childhood and family
Further information: Musk family
Elon Reeve Musk was born on June 28, 1971, in Pretoria, South Africa's administrative capital.[11][12] He is of British and Pennsylvania Dutch ancestry.[13][14] His mother, Maye Musk (née Haldeman), is a model and dietitian born in Saskatchewan, Canada, and raised in South Africa.[15][16][17] His father, Errol Musk, is a South African electromechanical engineer, pilot, sailor, consultant, emerald dealer, and property developer, who partly owned a rental lodge at the Timbavati Private Nature Reserve.[18][19][20][21] Elon has a younger brother, Kimbal, and a younger sister, Tosca.[17][22]

The family was wealthy during Elon's youth.[21] Despite both Musk and Errol previously stating that Errol was a part owner of a Zambian emerald mine,[21] in 2023, Errol recounted that the deal he made was to receive "a portion of the emeralds produced at three small mines."[23][24] Errol was elected to the Pretoria City Council as a representative of the anti-apartheid Progressive Party and has said that his children shared their father's dislike of apartheid.[11]

Elon's maternal grandfather, Joshua N. Haldeman, was an American-born Canadian who took his family on record-breaking journeys to Africa and Australia in a single-engine Bellanca airplane.[25][26][27][28]

After his parents divorced in 1980, Elon chose to live primarily with his father.[13][18] Elon later regretted his decision and became estranged from his father.[29] In one incident, after having called a boy whose father had committed suicide "stupid", Elon was thrown down concrete steps.[30][31] Elon has four paternal half-siblings.[32][25][33]

Elon was an enthusiastic reader of books, later attributing his success in part to having read The Lord of the Rings, the Foundation series, and The Hitchhiker's Guide to the Galaxy.[20][34] At age ten, he developed an interest in computing and video games, teaching himself how to program from the VIC-20 user manual.[35] At age twelve, Elon sold his BASIC-based game Blastar to PC and Office Technology magazine for approximately $500.[36][37]

Education
An ornate school building
Musk graduated from Pretoria Boys High School in South Africa
Musk attended Waterkloof House Preparatory School, Bryanston High School, and then Pretoria Boys High School, where he graduated.[38] Musk was a good but not exceptional student, earning a 61 in Afrikaans and a B on his senior math certification.[39] Musk applied for a Canadian passport through his Canadian-born mother,[40][41] knowing that it would be easier to immigrate to the United States this way.[42] While waiting for his application to be processed, he attended the University of Pretoria for five months.[43]

Musk arrived in Canada in June 1989, connected with a second cousin in Saskatchewan,[44] and worked odd jobs including at a farm and a lumber mill.[45] In 1990, he entered Queen's University in Kingston, Ontario.[46][47]

Two years later, he transferred to the University of Pennsylvania, an Ivy League university in Philadelphia, where he earned two degrees, a Bachelor of Arts in physics, and a Bachelor of Science degree in economics from the university's Wharton School.[48][49][50][51] Although Musk has said that he earned the degrees in 1995, the University of Pennsylvania did not award them until 1997.[52][49][53] He reportedly hosted large, ticketed house parties to help pay for tuition, and wrote a business plan for an electronic book-scanning service similar to Google Books.[54]

In 1994, Musk held two internships in Silicon Valley: one at energy storage startup Pinnacle Research Institute, which investigated electrolytic ultracapacitors for energy storage, and another at Palo Alto–based startup Rocket Science Games.[55][56] In 1995, he was accepted to a PhD program in materials science at Stanford University.[49][53][57] However, Musk decided to join the Internet boom, dropping out two days after being accepted and applied for a job at Netscape, to which he reportedly never received a response.[58][40]

Business career
Zip2
Main article: Zip2
External videos
video icon Musk speaks of his early business experience during a 2014 commencement speech at USC on YouTube
In 1995, Musk, his brother Kimbal, and Greg Kouri founded Global Link Information Network, later renamed to Zip2.[59][60] The company was financed mainly through a financing round of $200,000, of which 10% was contributed by his father Errol Musk.[61] The company developed an Internet city guide with maps, directions, and yellow pages, and marketed it to newspapers.[62] They worked at a small rented office in Palo Alto,[63] with Musk coding the website every night.[63] Eventually, Zip2 obtained contracts with The New York Times and the Chicago Tribune.[54] The brothers persuaded the board of directors to abandon a merger with CitySearch;[64] however, Musk's attempts to become CEO were thwarted.[65] Compaq acquired Zip2 for $307 million in cash in February 1999,[66][67] and Musk received $22 million for his 7-percent share.[68]"""
s=summary()
s.minimize(text)


