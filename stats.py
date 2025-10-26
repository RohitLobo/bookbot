def get_book_word_count(contents):
    total_wc = 0
    for line in contents.split('\n'):
        for word in line.split(' ') : 
            if len(word ) > 0:
                total_wc += 1
    return total_wc


def sort_results (count_dict):
    sorted_results = sorted(count_dict.items() ,reverse=True,key = lambda item:item[1])
    return(sorted_results)
    

def get_char_count(contents):
    char_count = {}
    for line in contents.split('\n'):
        for word in line.split(' ') :
            if len(word) > 0:
                for char in word:
                    if char.lower() in char_count:
                        char_count[char.lower()]+=1    
                        continue
                    elif char.lower().isalpha():
                        char_count[char.lower()]=1     
    return char_count                             
    # return dict(sorted(char_count.items(),key = lambda item :item[0]))