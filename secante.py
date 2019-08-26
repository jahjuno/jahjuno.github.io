# -*- coding:utf-8 -*
print("""
                =================================================================================================    
            |                                                                                                       |
        |                               METHODE DE LA SECANTE BY AINA JUNO                                              |        
            |                                                                                                       |
                =================================================================================================
""")
print("_____________________________ Pour f(x) ___________________________________")

a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))

print("_____________________________ Condition ___________________________________")
r = int(input("Borne inférieure= "))
s = int(input("Borne supérieure= "))
j=int(input('Itération maximum j= '))


print("_____________________________  SUJET   ____________________________________")
print(f"""
Soit la fonction f(x) = {a}x² + {b}x + {c} continue et derivable sur l'intervalle I=[{r},{s}].
Nous allons calculer f(x)=0 avec l'itération maximum  j={j}
""")
def f(x):
    f = a*(x**2) + b*x + c 
   
    return f
print(f"""
alors >>> f(x) = {a}x² + {b}x + {c}

f({r})= {f(r)}
f({s})= {f(s)}
""")    

for i in range (j):
    rn = (r-((f(r)*(s-r)) / (f(s)-f(r))))
    print(f"r{i+1}: {rn}")
    r = rn
