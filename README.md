Task list for project

## Base Roadmap
1. Finish desigining the core parameters for simulation purposes
2. Finish implementing state handlers for each main state type
3. Implement infection exposure and fatality mechanics
4. Test SimIndividual for general functionality
5. Begin implementing a connection graph between nodes
6. Stress-test and optimize structures
7. Test diseases and tweak as needed

## More Specific Tasks
* (X) Review and finish clarifying documentation for simulation parameters.
* (X) Review and finish describing the base mathematical models for the SimIndividual.
* (X) Implement the rest of the CONTAGIOUS state's core logic.
* (X) Implement the BEDRIDDEN state's core logic.
* (X) Implement any additional unique logic for RECOVERED or DECEASED individuals.
* (X) Complete the 'sub-day' update logic function, including scheduling of state changes.
* (X) Implement infection exposure methods.
* (X) Test one SimIndividual's course of infection.
* (X) Test a few SimIndividuals on a small scale.


#### What I Yammered On About
Evan: Designed template structure for the simulation, designed the first draft of the Simulation Individual class (screenshot provided), and setup the GitHub for the project.

Shira: Worked through additional biological parameter specifications and worked to plan the mathematics of the project.

Val: Worked on some parameter specifications and mathematical documentation; encountered Jupyter Lab difficulties during this.

Tyler: Worked on code organization and on designing visualization frameworks for Simulation Individuals.
