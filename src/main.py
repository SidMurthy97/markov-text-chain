from tqdm import trange, tqdm
import random
import re
from markovchain import MarkovChain

if __name__ == "__main__":
    
    #some test input
    input_file = \
        open(r"C:\Users\Sid Murthy\Documents\projects\markov-text-chain\datasets\harry_potter.txt", encoding="utf8")
    test_input = input_file.read()
    # word_list =  re.findall(r"[\w']+|[.,!?;]", test_input) #split all word and \
    #                                                        # punctuation 

    mc = MarkovChain(test_input)
    mc.make_chain()
    mc.generate_output()
