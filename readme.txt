The code is written in python.

To run the code on terminal : python luke.py

The code will generate some random values by using previously calculated numbers.
These vaues are stored in startA and startB variables.
A maskValue variable have been used and contains 16 one's.

Any value when made and bitwise & operation with this value will give the same last 16 bitwise.

Example : 245556042 in binary format is below : 

00001110101000101110001101001010

and maskValue is :
1111111111111111

bit-wise and operation : 

00001110101000101110001101001010
00000000000000001111111111111111
--------------------------------
00000000000000001110001101001010 -> which is 58186 and is stored in maskA

The same procedure is applied to maskB and both maskA and maskB are compared to see if they are same;
which means last 16 bits of startA and startB are same.
If they are same, then count is increased by one.
The program is run for 40000000 times to see how many of such pairs have same last 16 bits.