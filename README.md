# QuGlassyIsing
Repository for `Glassy dynamics using Quantum Computers` Team in Qiskit Hackathon Europe


<img width="550" alt="image" src="https://user-images.githubusercontent.com/38852529/120808929-2c45b000-c567-11eb-8343-d8f36f9014cc.png">

## Glassy Dynamics using Quantum Computing

![GitHub release](https://img.shields.io/github/v/release/arnavdas88/QuGlassyIsing?include_prereleases)
![GitHub repo size](https://img.shields.io/github/repo-size/arnavdas88/QuGlassyIsing)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Disordered Phase in Ising and Metastability in Cellular Potts Models Simulated on a Quantum Computer Hint at Glassy Dynamics

<details><summary><b>1.) Aim</b></summary>

<hr>
Understanding the <b>nature of glass</b> is one of the longstanding fundamental problems of Natural Sciences. Simulating quantum properties on a quantum device inherently comes with a faster and more accurate description of the system. Hence we propose to study the dynamics of glass using quantum computers. 

This problem statement falls in the category of “Application of Quantum Computing” in “Computational Natural Sciences”
<hr>
  
</details>


<details><summary><b>2.) Glassy Dynamics</b></summary>

<hr>
Any kind of arrested liquid system falls under glassy systems. But simulating a glassy system is a still an unsolved problem. Although many theories have been put forward over the years, a one-size-fits-all theory still remains an open problem in the field of natural sciences. 
<hr>
  
</details>


<details><summary><b>3.) Objectives</b></summary>
  
<hr>

-  If glassy systems arise in two different toy models from two different fields: 
   - Transverse Ising Model in Longitudinal Field
   - Cellular Potts Model
- Pushing the boundaries of NISQ era computing applications by simulating the dynamics of glass on hardware suitable for NISQ Devices
- Kickstart a new area of research for the quantum computing in natural sciences community
- Proposed Qiskit Module and Tutorial

<hr>
  
</details>

<details><summary><b>4.) Project Log</b></summary>
  
<hr>

- 1st week: Read Deepmind's Glassy Dynamics Paper. Can it be replicated using NISQ era QC? The answer turned out to be a resounding 'NO'. Decided to implement 2D faciliated Kinetic Ising Model. Read the Hubbard Model implementation using VQE. Do we need creation/annihilation operator for our project as it was used there? No. Just Ising formulations of our model is necessary. Read about probable use of QML in our work. No appropriate use found that can be implementated in the hackathon's time frame. But looked like an interesting research problem to pursue afterwards. 
- 2nd week: The penalty function formulations required to impose the local constraints in the 2D facilitated Kinetic Model requires more extensive study. This is not doable in the project timeline. Made a report and presentation on it and we discussed and decided to do it post hackathon. The report has been uploaded. We decided on implentating a Transverse Ising Model in a longitudinal field, which shows disordered phases according to the few papers that we read. This could show hint at glassiness: a temporal state between two magentic phases observed during Transition. 
- 3rd week: Started Cellular Potts Model implementation. Made helper functions in python to generate the equations for CPM to define the correct interactions among the cells. Learnt that varying the interactions will show us the metastablities during minimization that is a characteristics of a glassy system. It would be awesome if the relaxation could be shown, but that seems to be impossible as we can not exactly track the center of mass of the cells when converted to the ising formulation. The Ising formulations of the equations were made as well. Looking good so far! Maybe, we finally found two models that we can finish within the deadline?!?
-  4th week: TOTAL CHAOS! Doable within time, but so much work! Started building the proposed Qiskit Module as we have our formulations ready. Pushed our personal computers to the limit. The run of the results came in and looking good so far! There are good evidence of the disordered phases and flucations that we wanted to show in our model. Time to write the report and make the video! It has been a fun journey. First two weeks, we tried a lot of stuff that did not work as of now, but we got a lot of ideas that we would love to pursue in the future!

<hr>
  
</details>



### The Transverse Ising Model In a Longitudinal Field


**1 Dimensional:** The Longitudinal fields contribute more to the lowest energy than Transverse field. The transverse field account for the quantum fluctuations in the system. 

**2 Dimensional:** The best 3 spin configurations for each case are similar to each other. This means that the fields and interactions are pushing the system to reach a preferable configuration successfully. Our results are hence, coherent. 

Region of disordered phase between paramagnetic phase and anti-ferromagnetic phase. Different disordered phase region from 1D as shown in the reference paper [PhysRevE.99.012122](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.99.012122), due to the varying number of interactions for spins in center and edges.

If there is no longitudinal field, there is near perfect antiferromagnetic ordering. So no glass. But as we increase the longitudinal fields, we see disorder i.e combination of anti ferromagentic and ferromangentic. The ferromagenetism is seen in local moments. But if you increase the longitudinal field too much, it starts to show paramagnetism. Same goes for the transverse field. So, for a some particular combinations of both the fields, we can see disorder and we have found that the disordered phase lies in a region between paramagnetic and anti-ferromagnetic phase.



#### Cellular Potts Model

The Cellular Potts Model (CPM) for tightly packed cells in biological tissue can exhibit glass-like behaviour as the cells change their configurations, thereby changing the total energy possessed by the system. 

In our model, instead of using Markov Chain Monte Carlo (which is generally used in CPM models), we have used a Variational Quantum Eigensolver to reduce the energy to its ground state. 

This won’t tell us the configurations of the cells but it will tell us the exact energy for which the tissue reaches its ground state energy configuration.

`Docplex` : converting the quadratic equation to an ising hamiltonian

##### Completed Work
- Implementation of Transverse Field Ising Model in a Longitudinal Field and Cellular-Potts Model to simulate glassy dynamics 
- Open source library to simulate glassy dynamics that can ‘plug and play’ with the existing Qiskit framework

##### Future Work
- Bigger Lattice size for Transverse ising in longitudinal field and Cellular Potts Model. For ising, 50 by 50. For CPM, 80 by 80. Matrix product state simulator to the rescue.

- Investigating the effects of varying the interaction term in the Ising Model. J=0.25, J=4 etc

- Kinetic Ising Model: Investigating the relaxation from the spin flip dynamics of the 2D facilitated Kinetic Ising Model. The challenge is to implement the strong local kinetic constraints.

- Ising formulation of the Kob Anderson Binary Mixture with Lennard Jones Potential for studying molecular glass


## Provided Qiskit Helper Package

Our provided qiskit helper package provides the helper functions for the all the heavy lifting tasks. It eases the task of creating the hamiltonian by a lot.

### Project Structure
```bash
├── FUTURE_WORK.pdf
├── LICENSE
├── MANIFEST.in
├── README.md
├── pyproject.toml
├── qiskit_glassydynamics
│   ├── VERSION.txt
│   ├── __init__.py
│   └── helpers
│       ├── __init__.py
│       ├── decoretors.py
│       └── ising.py
├── requirements.txt
├── research
│   ├── cpm-vqe
│   ├── glassy grid
│   ├── notebooks
│   ├── pickle-files
│   └── rough-work-misc
├── samples
│   ├── 1Dising.py
│   ├── 2Dising.py
│   └── test.py
└── setup.py
```

##### Install :

```shell
$ pip3 install https://github.com/arnavdas88/QuGlassyIsing/releases/download/v0.0.1-alpha/QuGlassyIsing-0.0.1a0-py3-none-any.whl
```

##### Usage :

```python
from qiskit_glassydynamics.helpers import ising
```

Creating a hamiltonian for the 1D Ising is easier with `qiskit_glassydynamics`.

```python
# For 1D

J_hamiltonian = ising.Ising1DHamiltonian(5)
Bz_hamiltonian = ising.FieldHamiltonian( 5 , 'Z')
Bx_hamiltonian = ising.FieldHamiltonian( 5 , 'X')

H = - .75 * J_hamiltonian + .116 * Bz_hamiltonian - .431 * Bx_hamiltonian
```

For 2D Ising, we can use `Ising2DHamiltonian`

```python
# For 2D

J_hamiltonian = ising.Ising2DHamiltonian( (5, 5) )
Bz_hamiltonian = ising.FieldHamiltonian( (5, 5) , 'Z')
Bx_hamiltonian = ising.FieldHamiltonian( (5, 5) , 'X')

H = - .75 * J_hamiltonian + .116 * Bz_hamiltonian - .431 * Bx_hamiltonian
```

For complete sample, look at [2D Ising.py](https://github.com/arnavdas88/QuGlassyIsing/blob/main/samples/2Dising.py) and [1D Ising.py](https://github.com/arnavdas88/QuGlassyIsing/blob/main/samples/1Dising.py)


## Reference

<sup><a href="https://doi.org/10.1063/1.461768">[1]</a></sup> Scott Butler and Peter Harrowell, [The origin of glassy dynamics in the 2D facilitated kinetic Ising model](https://doi.org/10.1063/1.461768), 1991

<sup><a href="https://www.nature.com/articles/s41567-020-0842-8">[2]</a></sup> Bapst et. al., [Unveiling the predictive power of static structure in glassy systems](https://www.nature.com/articles/s41567-020-0842-8), 2020

<sup><a href="https://iopscience.iop.org/article/10.1209/0295-5075/116/28009/meta#:~:text=We%20map%20out%20the%20phase,that%20this%20phase%20is%20glassy.">[3]</a></sup> M. Chiang and D. Marenduzzo, [Glass transitions in the cellular Potts model](https://iopscience.iop.org/article/10.1209/0295-5075/116/28009/meta#:~:text=We%20map%20out%20the%20phase,that%20this%20phase%20is%20glassy.), 2016

<sup><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.35.1792">[4]</a></sup> David Sherrington and Scott Kirkpatrick, [Solvable Model of a Spin-Glass](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.35.1792), 1975

<sup><a href="https://www.frontiersin.org/article/10.3389/fphy.2014.00005">[5]</a></sup> Andrew Lucas, [Ising formulations of many NP problems](https://www.frontiersin.org/article/10.3389/fphy.2014.00005), 2014

<sup><a href="https://doi.org/10.1038/nature09994">[6]</a></sup> Simon, J., Bakr, W., Ma, R. et al. [Quantum simulation of antiferromagnetic spin chains in an optical lattice](https://doi.org/10.1038/nature09994), 2011



## About Us

| Ishmam Shah | Turbasu Chatterjee | Arnav Das | Sumit Suresh Kale | Rishabh Gupta | 
| :---: | :---: | :---: | :---: | :---: |
| Senior Year Chemistry Undergraduate, Dhaka University | Senior Year CS Undergraduate, MAKAUT | Senior Year CS Undergraduate, KNU | PhD Student, Purdue University, Sabre-Kais Group | PhD Student, Purdue University, Sabre-Kais Group |
