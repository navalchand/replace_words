from edit_distance import SequenceMatcher
import re
def sqr(x):
    return list(x)
def join_list(word_chunks):  
        ref_words =[]
        hyp_words =[]
        for i in range(len(word_chunks)):
            ans = []        
            ref_words1 = []
            hyp_words1 =[]
            for j in range(len(word_chunks[i])):
                ref_words1.append((word_chunks[i][j][1]))
                hyp_words1.append((word_chunks[i][j][2]))
            ref_words.append("".join(ref_words1))
            hyp_words.append("".join(hyp_words1))
            #z =(ref_words , hyp_words)
        ans =(ref_words , hyp_words)
        ans =  list(zip(*list(ans)))
        i = 0    
    	#remove the duplicates from the resulted list 
        while i < len(ans)-1:
            if ans[i] == ans[i+1]:
                del ans[i]
            else:
                i = i+1 
        #print (ans)
        
        ans = list(map(sqr, ans))
        return ans

def delete_check(delete_list):
    new_delete_list = []
    for w in delete_list:
        temp_list1 = w[0].split(" ")
        temp_list2 = w[1].split(" ")
        w[0] = " ".join([w for w in temp_list1 if w not in temp_list2])
        w[1] = " ".join([w for w in temp_list2 if w not in temp_list1])
        if w[1] == "":
            new_delete_list.append(w)
    return new_delete_list
def insert_check(insert_list):
    new_insert_list = []
    for w in insert_list:
        temp_list1 = w[0].split(" ")
        temp_list2 = w[1].split(" ")
        w[0] = " ".join([w for w in temp_list1 if w not in temp_list2])
        w[1] = " ".join([w for w in temp_list2 if w not in temp_list1])
        if w[0] == "":
            new_insert_list.append(w)
    return new_insert_list

def replace_words(string_a,string_b):
    tag1 = []
    ref = []
    hyp = []
    questionchunks = []
    qlist = []
    replaced_word_list = []
    inserted_word_list = []
    deleted_word_list = []
    string_b = string_b.lower()
    string_a = string_a.lower()
    string_a= re.sub("[!#$%&\'()*+,./:;<=>?@[\\]^_`{|}~]","",string_a)    
    string_b = re.sub("[!#$%&\'()*+,./:;<=>?@[\\]^_`{|}~]","",string_b)    
    string_a = string_a.replace('-'," ")
    string_b = string_b.replace('-'," ")
    #print a
    #print b
    s = SequenceMatcher(string_a, string_b)
    opcodes = s.get_opcodes()
    for tag, i1, i2, j1, j2 in opcodes:    
       #p.append(b[j1:j2])
       tag1.append(tag)
       ref.append(string_a[i1:i2])
       hyp.append(string_b[j1:j2])
    hyp_result = (tag1,ref,hyp)
    edit_distance_op =  list(zip(*list(hyp_result)))        
    for line in edit_distance_op:    
        if (line[1] == " " and line[2] == " "):
            questionchunks.append(qlist)
            qlist = []
        else: 
            qlist.append(line) 
    #get replaced words list in another list
    for i in range(len(questionchunks)):
        for j in range(len(questionchunks[i])):
            if questionchunks[i][j][0] == 'replace':
                replaced_word_list.append(questionchunks[i])                             
    
    for i in range(len(qlist)):
        if qlist[i][0] == 'replace':
                replaced_word_list.append(qlist)       
    #get inserted words list in another list
    for i in range(len(questionchunks)):
        for j in range(len(questionchunks[i])):
            if questionchunks[i][j][0] == 'insert':
                inserted_word_list.append(questionchunks[i])                             
                
    for i in range(len(qlist)):
        if qlist[i][0] == 'insert':
                inserted_word_list.append(qlist)       
    #get deleted words list in another list
    for i in range(len(questionchunks)):
        for j in range(len(questionchunks[i])):
            if questionchunks[i][j][0] == 'delete':
                deleted_word_list.append(questionchunks[i])                             
    
    for i in range(len(qlist)):
        if qlist[i][0] == 'delete':
                deleted_word_list.append(qlist)       
            #joining the resulted list
    print(replaced_word_list[0])
    #replaced_word_list1 = replaced_word_list[0]
    replaced_words = join_list(replaced_word_list)
    deleted_words = delete_check(join_list(deleted_word_list))
    inserted_words = insert_check(join_list(inserted_word_list))
    return (replaced_words,inserted_words,deleted_words)
