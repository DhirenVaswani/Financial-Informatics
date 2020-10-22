

# #### Binomial model Assignment
# ##### Write a Class called Option
# * To hold option attributes (Exercise Style, Option type, Strike, time to expiry)
# * Method to price the option using binomial model formula
# * The method should take an object of type Option as a parameter and additional parameters to take market details
# * Market details are (Stock price, Interest Rate, Volatility) 
# * Write a script to price European Call, Put and American Call and Put 
# * on Apple Stock strike of 275 and time to expiry 1 year,
# * market details are Stock price of 275, Interest rate of 2% and volatility of 30%
# ###DHIREN VASWANI

# In[53]:



import numpy

#T = time in years
#N = Number of iterations

#S0=275
#K=275
#T = 1
#N= 1000
#sigma= 0.3
#r= 0.02
            
class Option:
    def price(S0, K, T, N, sigma, r ,optiontype, callorput):
            dt= (T/N)
            u = numpy.exp(sigma*numpy.sqrt(dt))
            d = 1/u
            p = (numpy.exp(r*dt)-d)/(u-d)

            price_tree = numpy.zeros([N+1,N+1])

            for i in range(N+1):
                for j in range(i+1):
                    price_tree[j,i] = S0*(d**j)*(u**(i-j))

            option = numpy.zeros([N+1, N+1])


            if optiontype == "A" and callorput == "C":
                option[:,N] = numpy.maximum(numpy.zeros(N+1),price_tree[:,N]-K)
                for i in numpy.arange(N-1, -1, -1):
                    for j in numpy.arange(0, i+1):
                        option[j,i] = numpy.maximum(numpy.maximum(price_tree[j,i]-K,0),numpy.exp(-r*dt)*(p*option[j,i+1]+(1-p)*option[j+1, i+1]))

            elif optiontype == "A" and callorput == "P":
                option[:,N] = numpy.maximum(numpy.zeros(N+1),K-price_tree[:,N])
                for i in numpy.arange(N-1, -1, -1):
                    for j in numpy.arange(0, i+1):
                        option[j,i] = numpy.maximum(numpy.maximum(K-price_tree[j,i],0),numpy.exp(-r*dt)*(p*option[j,i+1]+(1-p)*option[j+1, i+1]))            

            elif optiontype =="E" and callorput == "C":  
                option[:,N] = numpy.maximum(numpy.zeros(N+1),price_tree[:,N]-K)
                for i in numpy.arange(N-1, -1, -1):
                    for j in numpy.arange(0, i+1):
                        option[j,i] = numpy.exp(-r*dt)*(p*option[j,i+1]+(1-p)*option[j+1, i+1])                                 

            else:
                option[:,N] = numpy.maximum(numpy.zeros(N+1),K-price_tree[:,N])
                for i in numpy.arange(N-1, -1, -1):
                    for j in numpy.arange(0, i+1):
                        option[j,i] = numpy.exp(-r*dt)*(p*option[j,i+1]+(1-p)*option[j+1, i+1])

            return option[0,0]


print("European call:",Option.price(275,275,1,1000,0.30, 0.02,"E","C"))
print("European put:",Option.price(275,275,1,1000,0.30, 0.02,"E","P"))
print("American call:",Option.price(275,275,1,1000,0.30, 0.02,"A","C"))
print("American put:",Option.price(275,275,1,1000,0.30, 0.02,"A","P"))



