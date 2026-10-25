# Notes

1. Sabse pehle problem kya hai?
Maan lo tumhare paas 3 words hain:
strs = ["flower", "flow", "flight"]



Humein pata karna hai ki teeno words ke starting mein kitne letters same hain.

Dekho:
- flower → f, l, o, w, e, r
- flow → f, l, o, w
- flight → f, l, i, g, h, t
Teeno mein starting ke f aur l same hain. Lekin teesre letter par o, o, i aata hai, jo same nahi hai.

Isliye answer "fl" hoga.
2. Complete code
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        left = 0

        while left < len(strs[0]):
            for word in strs[1:]:
                if left >= len(word) or strs[0][left] != word[left]:
                    return strs[0][:left]

            left += 1

        return strs[0]



3. Ab har line ko samjho
Line 1: left = 0
left ek pointer hai jo batata hai ki hum word ke kis index par hain.

Python mein indexing 0 se shuru hoti hai.
Index	0	1	2	3	4	5
Character	f	l	o	w	e	r

Toh left = 0 ka matlab hum sabse pehle f check karenge.
Line 2: while left < len(strs[0]):
Iska matlab:

Jab tak left first word ki length se chhota hai, tab tak checking karte raho.

Yahan:
strs[0]        # "flower"
len(strs[0])   # 6



Toh condition banegi:
while left < 6:



Hum first word ko reference bana rahe hain, yaani baaki saare words ko isi se compare karenge.
Line 3: for word in strs[1:]:
Yeh sabse important line hai.

strs[1:] ka matlab hai first word ko chhodkar baaki saare words.
strs[1:]  # ["flow", "flight"]



Ab for loop ek-ek karke words uthayega.

Pehle word = "flow" hoga, phir word = "flight" hoga.

Dhyan dena: Jab for loop chal raha hai, tab left same rahega. Hum ek hi index ko sabhi words mein compare karenge.
Line 4: Comparison condition
if left >= len(word) or strs[0][left] != word[left]:



Is line mein do conditions hain.

Pehli condition:
left >= len(word)



Agar koi word khatam ho gaya hai, toh hum aage compare nahi kar sakte.

Example:
strs = ["flower", "fl"]



Jab left = 2 hoga, "fl" mein index 2 exist hi nahi karta. Isliye humein wahi stop karna hoga.

Dusri condition:
strs[0][left] != word[left]



Iska matlab hai:

First word ke current index ka character aur doosre word ke same index ka character alag hain kya?

Agar alag hain, toh mismatch mil gaya.

or ka matlab hai ki dono mein se koi bhi condition true ho, toh hum return kar denge.
4. Ab actual dry run karte hain
Code dry run

Step 1 of 3





Current indexleft = 0

Match

f
flower

f
flow

f
flight


Kya hua?

Teeno mein f same hai. Ab left ko 1 karenge.

Prefix ab tak: "{steps[step].prefix}"
Next 


Is dry run se samjho ki hum pehle sabhi words ke same index ko check karte hain, phir index aage badhate hain.
5. return strs[0][:left] ka matlab
Maan lo mismatch left = 2 par mila.
return strs[0][:left]



Yeh ban jayega:
return "flower"[:2]



Python slicing mein ending index include nahi hota.

Isliye index 0 aur 1 ke letters milenge:
"fl"



Aur function wahi khatam ho jayega.
6. left += 1 kahan aur kyun likha hai?
for word in strs[1:]:
    if left >= len(word) or strs[0][left] != word[left]:
        return strs[0][:left]

left += 1



Yeh indentation bahut important hai.

left += 1 for loop ke bahar hai, lekin while loop ke andar hai.

Iska reason:

Agar hum left ko for loop ke andar badha denge, toh ek word ka index 0 check hoga aur doosre ka index 1. Yeh galat hoga.

Humein har word ke liye same index check karna hai. Jab saare match kar jaayein, tabhi left badhana hai.
7. Last mein return strs[0] kyun?
Agar koi mismatch mila hi nahi aur poora first word check ho gaya, toh iska matlab first word hi common prefix hai.

Example:
strs = ["cat", "catfish", "catalog"]



Teeno words "cat" se start hote hain.

First word "cat" poora match ho jaayega. while loop end hoga aur:
return strs[0]



Answer "cat" return karega.
