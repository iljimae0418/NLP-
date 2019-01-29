from __future__ import division
s = "I had a good day today, even though the weather was not great"
t = "I am good at getting stuck in bad weather"
s = s.split(" ")
t = t.split(" ")
'''
Positive Word Weights: 
Word 	Score
good	0.35
today	0.11
weather	0.23
great	0.63

Negative Word Weights: 
Word	Score
though	0.14
not	0.35
bad	0.44
stuck	0.21
'''
p = {
	"good":0.35,
	"today":0.11, 
	"weather":0.23, 
	"great":0.63
}
n = {
	"though":0.14,
	"not":0.35,
	"bad":0.44,
	"stuck":0.21
}
eval_s_fpos = 0.0 
eval_s_fneg = 0.0 
for i in p.keys(): 
	cnt = 0 
	for j in s: 
		if i == j: 
			eval_s_fpos += p[i] 
for i in n.keys(): 
	cnt = 0
	for j in s: 
		if i == j: 
			cnt += 1 
	eval_s_fneg += n[i]*cnt 
print(eval_s_fneg/eval_s_fpos) 
print(eval_s_fpos/eval_s_fneg)  
# do something similar for t 
