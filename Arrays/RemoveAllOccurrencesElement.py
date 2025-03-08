'''
Remove All Occurrences of an Element in an Array
Given an integer array arr[] and an integer ele the task is to the remove all occurrences of ele from arr[] in-place and 
return the number of elements which are not equal to ele. If there are k number of elements which are not equal to ele then 
the input array arr[] should be modified such that the first k elements should contain the elements which are not equal to ele
and then the remaining elements.

Input: arr[] = [3, 2, 2, 3], ele = 3
Output: 2
Explanation: The answer is 2 because there are 2 elements which are not equal to 3 and arr[] will be modified such that the 
first 2 elements contain the elements which are not equal to 3 and remaining elements can contain any element. So, modified 
arr[] = [2, 2, _, _]

Input: arr[] = [0, 1, 3, 0, 2, 2, 4, 2], ele = 2
Output: 5
Explanation: The answer is 5 because there are 5 elements which are not equal to 2 and arr[] will be modified such that 
the first 5 elements contain the elements which are not equal to 2 and remaining elements can contain any element. So, 
modified arr[] = [0, 1, 3, 0, 4, _, _, _]

'''

class Solution(object):
    def removeElement(self, nums, val):
        #inicializa uma variavel que serve de apoio pra rastrear onde o prox elemento sera colocado
        k = 0
        
        #percorre todos os indices [i] da lista nums
        for i in range(len(nums)):
        # se nums[i] for diferenet do valor de val
            if nums[i] != val:
                #vApós mover o elemento para a posição k, incrementando k para que o próximo 
                # elemento que não é val seja colocado na próxima posição.
                nums[k] = nums[i]
                #itera K para um novo tamanho do array
                k += 1
        return k


'''
O valor de K significa o valor que vai ser alterado.
Se o valor de k é igual o de val, entao k nao sera alterado, desse jeito o k continua sendo o indice do valor que é igual val
quando ele vai pra um valor diferente de val, o indice de K é o do val anterior, entao é sobrescrito na posição que é pra sair


exemplo: num [5, 7, 6, 10] val = 7
k = 0 
num[0] = 5 // 5 é != de 7
entao k+1
----------
k = 1
num[1] = 7 // que é == 7
nao faz nada com k entao ele continua sendo 1
----------
k = 1
num[2] = 6 // que é != de 7
entao num[k] == num[i] /// num[1] == num[2] entao o indice 1 é trocado pelo indice 2
'''