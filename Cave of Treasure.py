#question
image A normal day for a common man, woke up late, rushed to work still ended up an hour lte becuse of trafic. It was a horrible start for the day for Victor. Just when he thought the day couldnt be any worse, the day got even worse. He got sacked. He wanted to submerge his depresion a bit so he started walking along the highway and into the forest. He kept walking for 8 hours stretch witout a stop through the bushes and trees. It was getting darker and darker, the visibility kept reducing. The floor was slippery, he was tkaing cautious steps, but still he slipped and fell inside a cave. His head hit rock when he fell down and became unconsious.
After 2 hours....
He slowly gained consiousness, he tried oepning his eyes slowly, he could feel the pain but it wasnt that much severe. It was pitch dark all around him, but at a distance inside the cave he could see something glowing. He started walking towards it slowly. The day he thought as the most worst day of life, suddenly turned into a best day of life as he saw few glowing blue diamonds before him, they were so big that he need not work for lifetime. There was a note along with a bag. The note said take as much as you can in this bag, the paper even had a list about the weight of each blue diamond and its proit in million dollars. Which diamonds should he take and which he can leave behind so that he will be able to get the maximum profit.
Input Format
The first line of input has one integer input N, where N is the number of different blue diamonds available , and it is followed by two lines of N spaced inputs. The secnod line of input is the weights of those blue diamonds and the third line of input has the profits which can be got from each diamond. And the last line of input is C, where C is the capacity of the bag.
Constraints
1<=N<=10^9 1<=C<=10000 All other values will be less than 10^3
Output Format
Print the maximum profit he can get
Sample Input 0
3
10 20 30
60 100 120
50
Sample Output 0
220
************************************************************************************************************************************
#answer
def knapSack(W, wt, val, n): 
    if n == 0 or W == 0 : 
        return 0
    if (wt[n-1] > W): 
        return knapSack(W, wt, val, n-1)
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), 
                   knapSack(W, wt, val, n-1)) 
n=int(input())
wt =list(map(int,input().split())) 
val = list(map(int,input().split()))
W = int(input())
c=knapSack(W, wt, val, n) 
print(c)

