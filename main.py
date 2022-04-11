from tqdm import trange, tqdm
import random
class state:
    def __init__(self, state_value):
        self.value = state_value
        self.state_to_add = None
        self.next_states_raw = {}
        self.dict_prob_to_state = {}

        self.next_states, self.probability_to_state = [],[]
    
    def add_state(self,state_to_add):
        """ This function adds a state to the dictionary of next states, or \\
            increments its count """ 
        if state_to_add.value in self.next_states_raw:
            self.next_states_raw[state_to_add.value] += 1
        else:
            self.next_states_raw[state_to_add.value] = 1
    
    def compute_probabilites(self):
        """this function computes the probability of going into one of the \\
            next states"""

        possible_non_unique_states = 0

        for key in self.next_states_raw.keys(): #find total sum 
            possible_non_unique_states += self.next_states_raw[key]

        for key in self.next_states_raw.keys(): #compute the probabilities
            self.dict_prob_to_state[key] = \
                self.next_states_raw[key] / possible_non_unique_states
            
            self.next_states.append(key)
            self.probability_to_state.append(self.dict_prob_to_state[key])

        return self.dict_prob_to_state

    def pick_next_state(self):
        """ this function will randomly choose the value of the next state in \\
            the chain during execution"""
        return random.choices(self.next_states, self.probability_to_state)[0]
        


def print_raw_chain(object_dict):
    """Test function"""
    
    for word in object_dict:
        print(seen_words[word].value, seen_words[word].dict_prob_to_state)

if __name__ == "__main__":
    
    #some test input
    input_file = \
        open(r"C:\Users\Sid Murthy\Documents\projects\markov-text-chain\input.txt")
    test_input = input_file.read()
    word_list = test_input.split()


    #initialise dictionaries and lists
    seen_words = {}
    starting_words = []
    current_state,previous_state = None, None

    #making the chain     
    for i,word in enumerate(tqdm(word_list)): #loop over all words and make \\
                                              #the chain 
        
        current_state = state(word)

        if i == 0:
            #seen_words[word] = current_state
            pass
        
        else:
            
            if previous_state.value not in seen_words:
                previous_state.add_state(current_state)
                seen_words[previous_state.value] = previous_state

                if previous_state.value[0].isupper(): #is first letter is capital
                    starting_words.append(previous_state.value)
    
            else:
                seen_words[previous_state.value].add_state(current_state)
        
            #print(previous_state.value, current_state.value)
        previous_state = current_state

    for word in seen_words:
        seen_words[word].compute_probabilites()

    #execute the chain 

    input_word = random.choice(starting_words) #choose random starting word
    sentence_length = 20
    print(input_word)
    
    for _ in range(sentence_length):
        current_state = seen_words[input_word]
        input_word = current_state.pick_next_state()
        print(input_word)



    # print_raw_chain(seen_words)

        
        
        