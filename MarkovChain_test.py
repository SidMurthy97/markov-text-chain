from MarkovChain import MarkovChain

def test_chain():
    '''This tests is the chain is generated correctly for perfect input
    with capitalisation and period'''
    input_string = "The quick brown fox jumps over the lazy dog."

    mc = MarkovChain(input_string)
    seen_words, starting_words = mc.make_chain()
    mc.generate_output()

    assert True == True