import numpy
import scipy.optimize as opt

filename = 'data.csv'

data = numpy.loadtxt(open(filename,"r"),delimiter=",")

stress = data[:,0]
strain = data[:,1]
err_stress = data[:,2]


smax = stress.max()
stress = stress/smax
#I am assuming the errors err_stress are in the same units of stress.
err_stress = err_stress/smax

def chisqfunc((a, b)):
    model = a + b*strain
    chisq = numpy.sum(((stress - model)/err_stress)**2)
    return chisq

x0 = numpy.array([0,0])

result =  opt.minimize(chisqfunc, x0)
print result
#assert result.success==True
#a,b=result.x*smax
#plot(strain,stress*smax)
#plot(strain,a+b*strain)
