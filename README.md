# PyProj1 purpose explained
1st Project in python at devops-experts -> which summarizes python fundamentals.
* In this project we will receive an encrypted txt message.
* We will need to decrypt the message that is written in the txt file and represent the results.
* In addition to the decryption of the file, we will be required to make some additional actions on the decrypted message.

Part 1:
In the first part, we will receive a text string and will replace alphabetical characters in the text with other alphabetical characters, 
there will be a specific logic that will connect between each character that we will implement for full success. 
Example:
We assume that this is the text that appears in your text file:
AB DMF GR YGI
We found the next logic that connects between alphabetical characters to other alphabetical characters:
M=A, Y=B, C=D, A=M, T=F, I=G, S=R, B=Y and G=I
Pay attention that the logic is two directions, this means that if you found that M = A this automatically says that A = M.
According to this logic our decrypted text will be:
MY CAT IS BIG
Our actual decrypted text file will contain the next text:

'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'

J.U.U.U Kmltin.

mmps iks nmk eio; ---> hkmu

The logic for decrypting the text will come from finding the most common letters in the text file, 
and replacing them with the most common letters in the English language.
Our assumption for the project will be that the most common letters in English language are ‘e’,’t’,’o’,’r’.
For example, let’s assume that the most common letter in the text file is ‘a’ and the second most common letter is ‘b’.
Then we will receive the next logic for these two letters:
‘a’ = ‘e’, ‘e’=’a’, ’b’ =‘t’, ‘t’ = ‘b’.
So if the most common letters, for example, are ‘a’ , ‘b’, ‘c’, ‘d’ 
we will receive the following logic:
a b c d
^ ^ ^ ^
e t o r
In the first part we would like to run over the text string and save our described connection between the letters into a dictionary.
For the above example we will receive the following dictionary:
{'a': 'e', 'c': 'o', 'b': 't', 'e': 'a', 'd': 'r', 'o': 'c', 'r': 'd', 't': 'b'}
The function will return the dictionary with the logic. 
Notes:
* The dictionary will include just our four most common letters and the letters that there are connected to.
  For example, if ‘x’ is the fifth most common letter it will not appear in the dictionary.
* Some characters are not alphabetical letters, like ‘>’ for example.
  Please specify your code to use just alphabetical letters for dictionary creation.
* The code must be case insensitive but in the dictionary please present just the lower case of each character.
Check steps:
In order to check that your results, are right you can print your dictionary that you created in the function.
Then you can count manually the four most common letters in the string and check if it corresponds to your dictionary.
