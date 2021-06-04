# QuGlassyIsing
Repository for `Glassy dynamics using Quantum Computers` Team in Qiskit Hackathon Europe

<img width="1146" alt="image" src="https://user-images.githubusercontent.com/38852529/118729352-5ef76500-b853-11eb-9c6b-8471ecc55dc0.png">

## Glassy Dynamics using Quantum Computing
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Answering some of the toughest questions in the field like:
- Can we simulate the dramatic arrest of particles that leads to a system to act like a glass? 
- Can we understand the nature of the interaction of the particles in glassy systems?
- How do glassy systems “age” with time?
- Can we model our glassy systems beyond the realm of physics in order to be applicable for the simulation of complex systems?






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


<details><summary><b>3.) Problem Statement</b></summary>
  
<hr>
In our project, we will be trying to address the  following :

-  Studying the representation and correlation of various components of “glassy dynamics” like:
   -  Initialization of the glassy phase
   -  Evolution of the glassy system
   -  Long-term dynamics and aging
   -  Clustering of disordered particles
<hr>
  
</details>


We will be starting out with **2D Kinetic Ising model** and studying the phase diagram for glass transition. After that, we would be looking at more comprehensive models for a more realistic simulation. There are a lot of theories like “Kob-Anderson Binary Mixture with Lennard-Jones Potential”, “Random First Order Transition Theory” and “Cellular Potts model” but we will be trying to apply **“Ising Models for Spin-Glasses”** for our simulation. 

### The aim of this project is to find a suitable theory of glassy dynamics that can be realistically simulated on a quantum computer.

Glasses are fascinating to humans and a quantum simulation of glasses may lead to several breakthroughs in the field of natural sciences and practical industrial advances in the future!

This could mean that quantum computing might be able to eventually assist researchers in deriving fundamental physical theories, ultimately helping to augment, rather than replace, human understanding.

#### Novelty of the idea

The problem of understanding glass remains an open problem to this day and we are trying to be the first ones to be able to simulate existing quantum models of glassy dynamics using quantum computers

##### Near-Term Goal
- Implementation of 2D-Kinetic Ising model and Cellular-Potts Model to simulate glassy dynamics 
- Open source library to simulate glassy dynamics that can ‘plug and play’ with the existing Qiskit framework

##### Long Term Goals
> - Probably Implementing a 3D-Kinetic Ising model to simulate the glassy dynamics 
> - Probable use of quantum-classical hybrid Deep Learning model to KABLJ data to predict the long term dynamics of glasses

## Provided Qiskit Helper Package

Our provided qiskit helper package provides the helper functions for the all the heavy lifting tasks. It eases the task of creating the hamiltonian by a lot.

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


## Reference

<sup><a href="https://doi.org/10.1063/1.461768">[1]</a></sup> Scott Butler and Peter Harrowell, [The origin of glassy dynamics in the 2D facilitated kinetic Ising model](https://doi.org/10.1063/1.461768), 1991

<sup><a href="https://www.nature.com/articles/s41567-020-0842-8">[2]</a></sup> Bapst et. al., [Unveiling the predictive power of static structure in glassy systems](https://www.nature.com/articles/s41567-020-0842-8), 2020

<sup><a href="https://iopscience.iop.org/article/10.1209/0295-5075/116/28009/meta#:~:text=We%20map%20out%20the%20phase,that%20this%20phase%20is%20glassy.">[3]</a></sup> M. Chiang and D. Marenduzzo, [Glass transitions in the cellular Potts model](https://iopscience.iop.org/article/10.1209/0295-5075/116/28009/meta#:~:text=We%20map%20out%20the%20phase,that%20this%20phase%20is%20glassy.), 2016

<sup><a href="https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.35.1792">[4]</a></sup> David Sherrington and Scott Kirkpatrick, [Solvable Model of a Spin-Glass](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.35.1792), 1975


## About Us

| Sumit Suresh Kale | Rishabh Gupta | Ishmam Shah | Turbasu Chatterjee | Arnav Das |
| :---: | :---: | :---: | :---: | :---: |
| PhD Student, Purdue University, Sabre-Kais Group | PhD Student, Purdue University, Sabre-Kais Group | Senior Year Chemistry Undergraduate, Dhaka University | Senior Year CS Undergraduate, MAKAUT | Senior Year CS Undergraduate, KNU |
