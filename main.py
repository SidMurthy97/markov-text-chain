from tqdm import trange, tqdm

class state:
    def __init__(self, state_value):
        self.value = state_value
        self.next_state = None
        self.next_states = {}
    
    def update_state(self):
        if self.next_state in self.next_states: #if state already exists
            self.next_states[self.next_state] += 1
        else:
            self.next_states[self.next_state] = 1

test_input = "The cat and the dog are animals on Earth"

if __name__ == "__main__":
    states = []
    word_list = test_input.split()
    
    for i,word in enumerate(tqdm(word_list)):
        
        if i == 0:
        
            current = state(word)
        
        else:
            current.next_state = word
            current.update_state()
            
            current = state(word)

        states.append(current)
        
        