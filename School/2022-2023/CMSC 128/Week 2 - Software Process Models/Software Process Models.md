# Process Models
Check generic process framework [here](../Week%201%20-%20Introduction%20to%20Software%20Engineering/Software%20Engineering%20and%20Processes.md#The%20Process%20Framework)


## Waterfall Model
![[Pasted image 20220927084503.png]]
- a linear process flow
- sequential
- plan-driven process
- must plan and schedule all activies before starting
- each activities are represented as a separate phase arranged in linear order
- classic life cycle
	- illustrates the phases of software development
	- oldest process model being followed by industries even to this day


## Phases
1. Requirements / Requirements Analysis / Communication
2. System Design / Planning
3. Implementation / Modelling
4. Testing / Construction
5. Deployment
6. Maintenance

```diff
+ simple
+ easy to understand, use, and manage
+ activities are completed one at a time
+ rigid structure, very well understood requirements and unlikely to radical change
+ clearly defined stages
- no working software is produced until the last phase
- inflexible, cannot adapt to changes
- high risk
- poor model for large and ongoing project
- not designed for object-oriented programming
```


# V-Model
![[Pasted image 20220927091832.png]]
- **Verification** and **Validation** model
- variation/extension of [waterfall model](#Waterfall%20Model)
- all requirements are gathered from the start and cannot be changed
- for every phase in development cycle, there is an **associated testing phase**
- depicts the relationship of quality asssurance actions
`The corresponding testing phase of the development phase is planned in parallel, as you can see above.`


## Phases
1. Requirement Analysis  --> System/Acceptance Testing
2. High Level Design       --> Integration Testing
3. Low Level Design        --> Unit Testing
4. Coding

```diff
+ highly disciplined, easy to understand, and makes project management easier
+ good choice for software where downtimes and failures are unacceptable
- not good for complex project or projects that have unclear or changing requirements
```

# Incremental Process Model
![[Pasted image 20220927095214.png]]


# Prototyping

# Spiral Model
![[Pasted image 20220927105124.png]]



----
Check references [here](../../REFERENCES.md#Software%20Process%20Models).