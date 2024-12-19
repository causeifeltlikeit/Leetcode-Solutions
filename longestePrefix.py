strs.sort()
first = strs[0]
last = strs[len(strs)-1]
length = min(len(first), len(last))
i = 0
while i<length and first[i] == last[i]:
    i = i +1
return first[:i]