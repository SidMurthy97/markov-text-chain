from tqdm import trange, tqdm

class state:
    def __init__(self, state_value):
        self.value = state_value
        self.next_state = None
        self.next_states = {}
    
    def __update_state__(self):
        pass

    def add_state(self,next_state):
        if next_state.value in self.next_states:
            self.next_states[next_state.value] += 1
        else:
            self.next_states[next_state.value] = 1
    
    def compute_probabilites():
        pass


if __name__ == "__main__":
    
    #some test input
    test_input = "the quick brown the change the quick end"
    word_list = test_input.split()


    #initialise dictionaries and lists
    seen_words = {}
    current_state,previous_state = None, None
    
    for i,word in enumerate(tqdm(word_list)): #loop over all words and make the chain 
        
        current_state = state(word)

        if i == 0:
            #seen_words[word] = current_state
            pass
        
        else:
            
            if previous_state.value not in seen_words:
                previous_state.add_state(current_state)
                seen_words[previous_state.value] = previous_state
            else:
                seen_words[previous_state.value].add_state(current_state)
        
            #print(previous_state.value, current_state.value)
        previous_state = current_state
    
    assert seen_words[0].next_states[quick] == 2

            
        
        
        