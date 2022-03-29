from tqdm import trange, tqdm

class state:
    def __init__(self, state_value):
        self.value = state_value
        self.next_state = None
        self.next_states = {}
    
    def __update_state__(self):
        pass

    def add_state(self,next_state):
        self.next_state = next_state
        self.__update_state__()
    
    def compute_probabilites():
        pass


if __name__ == "__main__":
    
    #some test input
    test_input = "the quick brown fox"
    word_list = test_input.split()


    #initialise dictionaries and lists
    words2index = {}
    states = []
    
    
    for i,word in enumerate(tqdm(word_list)): #loop over all words and make the chain 
        
        if i == 0: #skip the first iteration
        
            current_word = state(word)
            
        else: #assign the next state to each word and update the count
            
            next_word = state(word)
            current_word.add_state(next_word)
            
            current_word = next_word
        

        states.append(current_word)
            

            
        
        
        