from pHcalc import Acid,Inert,System
import matplotlib.pyplot as plt
import numpy as np

def generate_sillen(acids, names):
        
    #initialize pH for plotting
    pHs = np.linspace(0,14,1000)
    conc_H = -pHs
    conc_OH = -(14-pHs)

    #calculate concentration from speciation
   


    #initialize plotting
    fig, ax = plt.subplots()

    #Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 14, 2)
    minor_ticks = np.arange(0, 14, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(-major_ticks)
    ax.set_yticks(-minor_ticks, minor=True)

    ax.set_xlim((0,14))
    ax.set_xlabel('pH')

    ax.set_ylim((-14,0))
    ax.set_ylabel('log(conc/M)')
    
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    #plot pH and pOH
    ax.plot(pHs,conc_H, color="blue", alpha = 0.1)
    ax.plot(pHs,conc_OH, color ='blue', alpha =0.1)


    for i,acid in enumerate(acids):
        conc_acid = np.log10(acid.alpha(pHs)*acid.conc)
        regions = np.shape(conc_acid)[1]
        #separate different regions
        #for region in conc_acid[:]
        for ri in range(regions):
            ax.plot(
                pHs,
                conc_acid[:,ri],
                color="C%s"%(i+1),
                alpha = 0.2+0.8*(ri/regions),
                label = names[i] + "_" +str(ri)
                )

        #ax.plot(pHs, conc_acid, color="C%s"%i)
    ax.legend()
