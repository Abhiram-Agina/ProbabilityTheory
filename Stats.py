# Learn Statistics using Python
import streamlit as st #Create Apps of Python Programs + Hosting
import math

nav = st.sidebar.radio("Navigation",["Basic Stats","Organizing Data","Averages & Variation", "Probability Theory", "Binomial Distribution"], index=3)
st.image('images\stats_banner.PNG', width=400)

if nav == "Probability Theory":
    st.header("Probability Theory")
    
    st.image('images\SampleSpace_Deck.PNG', width=400)
    st.subheader("Sample Space")
    import itertools, random

    # make a deck of cards
    deck = list(itertools.product(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
                                  ['Spade','Heart','Diamond','Club']))
    
    st.write(deck)
    st.write(type(deck))
    st.write("sample size =", len(deck))
    
    cols = st.columns(2)
    card = cols[0].selectbox("pick a card:", ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
    house = cols[1].selectbox("pick a house:", ['Spade','Heart','Diamond','Club'])
    
    picked = [d[0] for d in deck[0:51]].count(card)
    
    st.write("number of {}:".format(card), picked)
    
    st.write("probability of picking {} from a deck".format(card), str(round((picked/len(deck))*100, 2))+'%')
    
    st.image('images\pocket-aces.jpg', width=400)
    st.subheader('Permutations & Combinations')
    
    st.write("Pocket Cards: First 2 Cards dealt to each player in Poker")
    cols = st.columns(2)
    oper = cols[0].selectbox("pick an operation:", ['Permutation', 'Combination'])
    set = cols[1].selectbox("pick a set:", ['Aces','Total'])
    
    if oper == "Permutation":
        if set == "Aces":
            st.write('Permutations: nPk = n! / (n−k)!')
            # 12 Permutations Code for Pocket Aces

            """
            Permutations of Pocket Aces: Getting 2 Aces from a total of 12 different Aces
            - Ace Hearts / Ace Diamonds\n
            - Ace Diamonds / Ace Hearts\n
            - Ace Hearts / Ace Clubs\n
            - Ace Clubs / Ace Hearts\n
            - Ace Hearts / Ace Spades\n
            - Ace Spades / Ace Hearts\n 
            - Ace Diamonds / Ace Clubs\n
            - Ace Clubs / Ace Diamonds\n 
            - Ace Diamonds / Ace Spades\n
            - Ace Spades / Ace Diamonds\n 
            - Ace Clubs / Ace Spades\n
            - Ace Spades / Ace Clubs\n 
            """

            n = 4
            st.write("total number of aces in a deck: n =", n)
            k = 2
            st.write("total number of cards selected from a deck: k =", k)

            # Determine permutations and print result
            Permutations = math.factorial(n) / math.factorial(n-k)
            st.write("#Permutations of Pocket Aces:", int(Permutations))
            
        if set == "Total":
            n = 52
            st.write("total number of cards in a deck: n =", n)
            k = 2
            st.write("total number of cards selected from a deck: k =", k)

            # Determine permutations and print result
            Permutations = math.factorial(n) / math.factorial(n-k)
            st.write("#Total Permutations of Pocket Cards:", int(Permutations))
    
    if oper == "Combination":
        st.write('Combinations: nCk = nPk / k!')
        if set == "Aces":
            # 6 Combinations of Pocket Aces

            """
            Pocket Cards: First 2 Cards dealt to each player in Poker\n
            Combinations of Pocket Aces: Getting 2 Aces from a total of 6 different Aces, where Order doesn't matter
            - Ace Hearts / Ace Diamonds\n
            - Ace Hearts / Ace Clubs\n
            - Ace Hearts / Ace Spades\n
            - Ace Diamonds / Ace Clubs\n
            - Ace Diamonds / Ace Spades\n
            - Ace Clubs / Ace Spades\n

            """
            n = 4
            st.write("total number of Aces in a deck: n =", n)
            k = 2
            st.write("total number of cards selected from a deck: k =", k)

            # Determine permutations and print result
            Permutations = math.factorial(n) / math.factorial(n-k)
            Combinations = Permutations / math.factorial(k)
            st.write(int(Combinations))
        if set == "Total":
            n = 52
            st.write("total number of cards in a deck: n =", n)
            k = 2
            st.write("total number of cards selected from a deck: k =", k)

            # Determine permutations and print result
            Permutations = math.factorial(n) / math.factorial(n-k)
            Combinations = Permutations / math.factorial(k)
            st.write("#Total Combinations of Pocket Cards: ", int(Combinations))
       
    st.header("Independent and Dependent Events")
    st.write("Calculate the Probability of picking these Cards")
    cols = st.columns(3)
    card11 = cols[0].selectbox("First Card:", deck)
    card22 = cols[1].selectbox("Second Card:", deck)
    rpl = cols[2].selectbox("approach", ["with replacement", "without replacement"])
    
    picked1 = [d[0] for d in deck[0:51]].count(card11)
    picked2 = [d[0] for d in deck[0:51]].count(card22)
            
    if st.button("Submit"):
        if rpl == "with replacement":
            st.subheader('Independent Events')
            """
            Events A and B (which have nonzero probability) are independent if and only if all of the following equivalent statements holds:\n
            P(A∩B)=P(A)*P(B)\n
            P(A|B)=P(A)\n
            P(B|A)=P(B)\n
            """
            
            # Probability of drawing an Ace from a deck of cards, replacing it, reshuffling the deck, and drawing another Ace

            st.write("first card:", card11)
            st.write("seond card:", card22)
            #st.write("probability of drawing first card is", picked1)
            #st.write("probability of drawing second card is", picked2)
            #st.write(str(round((picked1/len(deck))*100, 2)))
            #st.write(str(round((picked2/len(deck))*100, 2)))

            # Probability of two consecutive independant aces 
            #two_aces_probability = ace_probability * ace_probability
            # st.write("probability of picking {0} and {1} from a deck:".format(card11, card22), str(round(round((picked1/len(deck))*100, 2)*round((picked2/len(deck))*100, 2), 2))+'%')
            # st.write("As cards are replaced, these are Independent Events")
            # st.write(round((picked1/len(deck))*100, 2))
        
        if rpl == "without replacement":
            st.subheader('Dependent Events')
            """
            Events A and B (which have nonzero probability) are dependent if and only if all of the following equivalent statements holds:
            P(A∩B)=P(A)*P(B)
            P(A|B)=P(A)
            P(B|A) <> P(B)
            """
            st.write("deck size:", len(deck))
            picked1 = [d[0] for d in deck[0:51]].count(card11)
            st.write("picked1", picked1)
            st.write(type(deck))
            st.write(type(card11))
            st.write(card11)
            deck = deck.remove(card11)
            # st.write("deck size:", len(deck))
            # picked2 = [d[0] for d in deck[0:50]].count(card22)
            # st.write("picked2", picked2)
            # st.write("probability of picking {0} and {1} from a deck:".format(card11, card22), str(round(round((picked1/len(deck))*100, 2)*round((picked2/len(deck))*100, 2), 2))+'%')
            # st.write("As cards are NOT replaced, these are Dependent Events")        
