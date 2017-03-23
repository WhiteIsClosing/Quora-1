from data_helper import get_words_and_states

if __name__ == '__main__':
    words1, states1, words2, states2 = get_words_and_states('How does the Surface Pro himself 4 compare with iPad Pro?','Why did Microsoft choose core m3 and not core i3 home Surface Pro 4?')
    print words1
    print states1
    print words2
    print states2