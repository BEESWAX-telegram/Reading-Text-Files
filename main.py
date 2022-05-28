# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



import string


def read_file_content(filename):
  with open('story.txt', 'r') as f:
    filename = f.read()
    return filename

   
      
      
         


def count_words():
    text = read_file_content("story.txt")
    word_in_text = text.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in word_in_text]

     #[assignment] Add your code here
    count = dict()
    for word in stripped:
        if word in count:
          count[word] += 1
        else: 
          count[word] = 1
    return(count)


print (count_words())
    

        #return {"as": 10, "would": 20}
