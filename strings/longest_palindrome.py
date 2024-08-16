
def find_longest_palindrome(s):
    memoization = [[0]*len(s) for _ in range(len(s))]
    for i in range(len(s)):
        memoization[i][i]=1
        palindrome=s[i]
    for i in range(len(s)-1,-1,-1):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                if (j-i)>1: 
                    if memoization[i+1][j-1]==1:
                        memoization[i][j]=1
                        current_palindrome=s[i:j+1]
                        if len(current_palindrome)>len(palindrome):
                            palindrome=current_palindrome
                        # max_length=max(max_length,(j-i+1))
                else:
                    memoization[i][j]=1
                    if len(current_palindrome)>len(palindrome):
                        palindrome=current_palindrome
    return palindrome

s="abcacbj"
print(find_longest_palindrome(s)) #bcacb
