s="abcadefga"

# bruteforce
def is_substring_with_no_rep_chars(s):
    return len(s)==len(set(s))


max_length=0
for i in range(len(s)-1,-1,-1):
    for j in range(i,len(s)):
        current_substring=s[i:j+1]
        if len(current_substring)>max_length:
            if is_substring_with_no_rep_chars(current_substring):
                max_length=len(current_substring)

print(max_length)

# using two pointers optimal way
l=0
max_length=0
unique_chars=set()

for r in range(len(s)):
    if s[r] not in unique_chars:
        unique_chars.add(s[r])
        max_length=max(max_length,len(unique_chars))
    else:
        while s[r] in unique_chars:
            unique_chars.remove(s[l])
            l+=1
        unique_chars.add(s[r])

print(max_length)
