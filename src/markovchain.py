from tqdm import trange, tqdm
import random
import re

'''TODO: The last word is left out in the current architecture. Also true for 
the computed probabily dictionary.'''
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
        
class MarkovChain:

    def __init__(self, input):
        '''initialise the class with an input string'''
        self.seen_words = {}
        self.starting_words = []
        self.current_state,self.previous_state = None, None
        self.input_dataset =  re.findall(r"[\w']+|[.,!?;]", input)
        self.input_dataset.append(" ") #append blank space so the whole list is iterated
        self.sentence_end = False
    def check_if_start_of_sentence(self):
        '''This function sets a flag is an ending punctiation is encountered
        and records the next word in the starting words list'''
        word = self.previous_state.value
        
        if self.sentence_end: #first check if sentence has ended
            self.starting_words.append(word) #add word if it has
            self.sentence_end = False #reset the flag
        
        if word == "." or word == "!" or word == "?": #set flag if ended            
            self.sentence_end = True

        

    def make_chain(self):
        
        for i,word in enumerate(tqdm(self.input_dataset)): #loop over all words and make \\
                                                #the chain             
            self.current_state = state(word)

            if i == 0:
                #Register first word as starting word
                self.starting_words.append(self.current_state.value)
            
            else:
                
                if self.previous_state.value not in self.seen_words:
                    self.previous_state.add_state(self.current_state)
                    self.seen_words[self.previous_state.value] = self.previous_state

                    # if self.previous_state.value[0].isupper(): #is first letter is capital
                    #     self.starting_words.append(self.previous_state.value)
        
                else:
                    self.seen_words[self.previous_state.value].add_state(self.current_state)
                self.check_if_start_of_sentence()
                #print(self.previous_state.value, self.current_state.value)
            self.previous_state = self.current_state

        for word in self.seen_words:
            self.seen_words[word].compute_probabilites()
        
        return self.seen_words 

    def generate_output(self):
        input_word = random.choice(self.starting_words) #choose random starting word
        output_str = ""
        while input_word != ".":
            output_str += " " + input_word
            current_state = self.seen_words[input_word]
            input_word = current_state.pick_next_state()
        
        output_str += "."

        print(output_str)
