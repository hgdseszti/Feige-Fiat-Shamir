# Fiat-Shamir Protocol
import random
from Crypto.Util.number import *

if __name__ == "__main__":
	p = getPrime(15)                                                    #veszünk 2 db tetszőleges 15 bites prím egészet
	q = getPrime(15)
	n = p*q																#n = 2 prím szorzata

	secret = "The secret ingredient is love"
	S = bytes_to_long(b"The secret ingredient is love")					#Átkonvertáljuk az üzenetet decimális formára.

	v = pow(S, 2, n)													#v a nyilvános kulcs, ami =(S**2)%n

	count = 0
	num_of_iterations = 5
	print('\nMessage 	= ', secret)
	print("Message		= ", S)
	print("Prime 		= ", n,'\n')

	for i in range(num_of_iterations):

		# Alice választ egy random r számot a (1 ,n-1) intervallumból és elküldi x=(r**2)%n Bob-nak.
		r = random.randint(1, n-1)
		x = pow(r, 2, n)

		# Bob véletlenszerűen kiválaszt egy e bitet (0 vagy 1), és elküldi Alice-nek.
		e = random.randint(0, 1)

		# Alice kiszámolja y=(r*(S**e))%n és visszaküldi Bob-nak.
		y = (r*(S**e))%n

		# Bob ellenőrzi y**2 == (x*(v**e))%n egyenlőségét. Ha egyenlő, tovább halad a protokoll
		# következő körébe, ellenkező esetben a bizonyítást nem fogadja el.
		print("=====================================================")
		print("Iteration "+str(i+1),'\n')
		print("r 		    = ", r)
		print("x		    = ", x)
		print("e 		    = ", e)
		print("y 		    = ", y)
		print("y**2 		= ", pow(y,2,n))
		print("(x*(v**e)) 	= ", (x*(v**e))%n)

		print("\nIteration "+str(i+1)+":	", end="")
		if(pow(y,2,n) == (x*(v**e))%n):
			print("Passed")
			count += 1
		else:
			print("Failed")

		print("=====================================================")

	if(count == num_of_iterations):
		print("Alice has proven she knows the secret.")
	else:
		print("The proof is not accepted.")