import matplotlib.pyplot as plt                                                               
                                                                                              
X1= [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,51,52,53,54,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,78,79,80,84,85,87,88,90,91,92,94,96,98,101,102,103,105,106,110,115,116,118,119,121,122,123,125,126,129,130,132,133,137,138,139,140,141,146,150,154,156,159,162,167,169,184,187,192,207,213,225,236,254,290,358]                                                
Y1 = [4948,1045,1010,364,321,195,139,97,89,59,56,59,26,25,22,26,16,18,26,17,12,10,8,12,11,10,10,6,6,3,8,3,7,6,3,8,6,3,4,5,7,3,4,2,4,3,7,2,1,2,4,1,8,6,2,2,5,3,1,2,2,3,1,1,1,3,2,3,1,2,4,4,4,1,3,2,1,2,1,2,1,2,1,2,3,1,3,1,2,2,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,2,1,1,2,1,2,1,1,1,2,1,1,1,1,1,1,1,1,1,1]

X = X1[0:15]
Y = Y1[0:15]
                                                                                              
plt.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[4948,1045,1010,364,321,195,139,97,89,59,56,59,26,25,22])                                                                        
plt.ylabel('number of components')                                                          
plt.xlabel('component size')                                                                    
plt.show()                       

