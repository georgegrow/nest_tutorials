#import packages and start nest
from sklearn.svm import LinearSVC
from scipy.special import erf
import nest

#CREATING PARAMETERISED POPULATIONS OF NODES
ndict = {"I_e": 200.0, "tau_m": 20.0} #creating a varible to define all parameters for the neuron. Neuron parameters can be deterined from electrical testing on the MEA with a single neuron.
nest.SetDefaults("iaf_psc_alpha", ndict) #this sets the parameter ndict as all defaults so there is no need to add it to the parameter
neuronpop1 = nest.Create("iaf_psc_alpha", 100)
neuronpop2 = nest.Create("iaf_psc_alpha", 100)
neuronpop3 = nest.Create("iaf_psc_alpha", 100)

edict = {"I_e": 200.0, "tau_m": 20.0} #creating new variable parameter
nest.CopyModel("iaf_psc_alpha", "exc_iaf_psc_alpha") #copying parameter
nest.SetDefaults("exc_iaf_psc_alpha", edict)

#you can also copy and set parameters in one step
idict = {"I_e": 300.0}
nest.CopyModel("iaf_psc_alpha", "inh_iaf_psc_alpha", params=idict)

epop1 = nest.Create("exc_iaf_psc_alpha", 100)
epop2 = nest.Create("exc_iaf_psc_alpha", 100)
ipop1 = nest.Create("inh_iaf_psc_alpha", 30)
ipop2 = nest.Create("inh_iaf_psc_alpha", 30)

parameter_list = [{"I_e":200.0, "tau_m":20.0}, {"I_e": 150.0, "tau_m": 30.0}]
epop3 = nest.Create("exc_iaf_psc_alpha", 2, parameter_list) #creating a heterogenous population of neurons; don't understand how many of each parameter exists in a given population

#SETTING PARAMETERS FOR POPULATIONS OF NEURONS
Vth = -55
Vrest = -70
#for neuron in epop1:
 #   nest-SetStatus([neuron]), {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()}])
#could do it this way ^ but below is a better way to do it

dVms = [{"V_m": Vrest+(Vth-Vrest)\*numpy.random.ran())} for x in epop1]
nest.SetStatus(epop1, dVms)

# CREATING POPULATIONS OF NEURONS WITH DETERMINISTIC CONDITIONS
pop1 = nest.Create("iaf_psc_alpha", 10) #creating population of 10 neurons
nest.SetStatus(pop1, {"I_e": 376.0}) #pretty sure this Set.Status creates spike neurons
pop2 = nest.Create("iaf_psc_alpha", 10)
multimeter = nest.Create("multimeter", 10)
nest.SetStatus(multimeter, {"withtime":True, "record_from":["V_m"]})
nest.Connect(pop1, pop2, syn_spec={"weight":20.0})
#can use all_to_all or one_to_one
nest.Connect(multimeter, pop2)

#CONNECTING POPULATIONS WITH RANDOM CONNECTIONS
#fixed_indegree : n random connections for each neuron in the target population#fixed_outdegree : n random connections for each neuron in the source population
#fixed_total_number : specified n connections are created by randomly picking neurons from source and target populations
#pairwise_bernoulli : iterates through all possible source-target pairs and creates connections with a specified probability
#make sure neurons don't connect to each other multiple times!!!

#SPECIFYING THE BEHAVIOUR OF DEVICES

