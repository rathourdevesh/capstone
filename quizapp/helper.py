
def typing_test_logic(original_text, typed_text, time_taken) -> tuple:
    """
    Candidate A - typed total 390 words out of which 388 are correct and 2 are incorrect in a duration of
    10 minutes. Hence,
    Total Typed Words = 390
    Correct Words = 388
    Incorrect Words = 2
    Gross words per Minute (GWPM) = 390/10 = 39 words per minute
    Net words per Minute (NWPM) = 388/10 = 38.8 words per minute
    Accuracy = 38.8*100/39 = 99.49 %
    Hence, actual typing speed of the candidate is 38.8 words per minute.

    returns 
        total_words,
        correct_words,
        incorrect_words,
        gross_word_per_min,
        net_word_per_min,
        accuracy
    """
    if time_taken == 0:
        time_taken = 0.1
    original_words = original_text.split(' ')
    typed_words = typed_text.split(' ')
    correct_count = 0
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct_count+=1
    gwpm = len(original_words)/time_taken
    nwpm = correct_count/time_taken
    return \
        len(original_words), \
        correct_count, \
        len(typed_text) - correct_count, \
        gwpm, nwpm, (nwpm*100)/gwpm
