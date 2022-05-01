from src.markovchain import MarkovChain
import re


def test_unique_chain():
    input_string = "The quick brown fox jumps over the lazy dog."
    actual_output = []

    expected_states = len(re.findall(r"[\w']+|[.,!?;]", input_string))
    expected_output = [1.0] * expected_states
    
    mc = MarkovChain(input_string)
    seen_words = mc.make_chain()

    for word,state in seen_words.items():
        for _,value in state.dict_prob_to_state.items():
            actual_output.append(value)
    
    assert expected_output == actual_output
        

def test_nonunique_chain():
    input_string = "This test is a test."
    actual_output = []

    expected_output = [1.0,0.5,0.5,1.0,1.0,1.0]
    
    mc = MarkovChain(input_string)
    seen_words = mc.make_chain()

    for word,state in seen_words.items():
        for _,value in state.dict_prob_to_state.items():
            actual_output.append(value)
    assert expected_output == actual_output
