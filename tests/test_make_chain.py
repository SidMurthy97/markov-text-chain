from src.markovchain import MarkovChain
import re

'''TODO: Write tests:
- what happens when input is empty?
- Check probabilities are correct assigned 
- test cases on the actual chain, do the words link correctly?'''

def test_make_chain_with_perfect_input():
    '''This tests if the chain is generated correctly for perfect input
    with capitalisation and period'''
    input_string = "The quick brown fox jumps over the lazy dog."
    expected_output = re.findall(r"[\w']+|[.,!?;]", input_string)
    mc = MarkovChain(input_string)
    seen_words = mc.make_chain()

    assert list(seen_words.keys()) == expected_output

def test_make_chain_with_duplicate_words():
    pass

def test_starting_words():
    pass

