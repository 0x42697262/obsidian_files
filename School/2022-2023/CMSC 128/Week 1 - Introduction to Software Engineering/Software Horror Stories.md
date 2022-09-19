# unorganized notes
- Poor software engineering practice is the culprit (software design errors and software specifications)
- Ariane 5 Flight 501 a continuation of a costly incomplete testing procedure
- Computer Based Systems (CBS)
	- Computing System (CS)

**SpECS (System Engineering for Computer Systems)**
- Phases
	1. Capture of initial requirements
	2. System design
	3. System dimensioning

**Some major benefits**
- SpECS benefit in application is design reusability
- Getting rid of these 3 issues:
	- specifications of some modules are missing, or are ambiguous, or are incomplete
	- verification is done via testing, within some limited time budget, which means that verification is almost incomplete
	- verfication that the set of concatenated modules "behaves correctly" is a combinatorial problem

- On-Board Computer input data transmitted by the Inertial Reference System (SRI) did not contain proper flight data. Although it showed diagnostic bit pattern that got interpreted as regular flight data by the OBC. 
	- Caused an exception from converting a 64-bit floating point number `F` to 16-bit signed integer.
		- F has greater value than the 16-bit signed integer thus causing an `Operand Error`
		- The cause was from the high value of an aligment function result called `Horizontal Bias`
	- Since Ariane 5 differs from Ariane 4 trajectory, this caused higher horizontal velocity values
- `Horizontal Velocity` is an external variable used to compute an integer variable `Horizontal Bias`

## Capture of initial requirements
- **3 Faults** (Causes?)
	- **External Variable**  (RC<sub>1</sub>)
		- The need to split the initial application requirements into two subsets has not been identified.
		- A `fortiori`, the need to transform description, has not been identified.
		- This fault has resulted into system dimensioning fault (DIM<sub>1</sub>).
		- The alignment program was running after lift-off.
			- The *"exception condition"* (Horizontal Bias overflow) was raised while running this program.
	- **Application Task Attribute**  (RC<sub>2</sub>)
		- Had the problem been listed, the alignment task would have been listed, along with its attributes.
			- "alignment task should not be running after lift-off"
		- This fault has resulted into system design fault  (DES<sub>5</sub>).
	- **Dependability Property and Assumptions**  (RC<sub>3</sub>)
		- Assumed that 1 SRI module at most would fail.
			- This has resulted into system design faults  (DES<sub>1,2,3,4</sub>) and system dimensioning fault (DIM<sub>2</sub>).

## System Design
- **5 Faults** (Effects?)
	- DES<sub>1</sub> (SRIs)
		- No SpECS methods was used
			- Non diversified redunancy is an incorrect solution
	- DES<sub>2</sub> (SRIs)
		- The implicit "*crash-only*" assumption has not been specified which could be violated, which happened
		- `Detection-and-recovery`, the type of fault-tolerance algorithm used, cannot be proven to be a correct solution unless failure models are specified
	- DES<sub>3</sub> (SRIs & OBCs)
		- The implicit "*crash-only*" assumption has not been specified which instead of "killing themselves", SRI modules issued diagnostic/error messages
	- DES<sub>4</sub> (OBCs)
		- No proof has been established showing that a correct OBC module delivers correct inputs to the OBC task in charge of commanding the nozzle deflections, in the presence of some faulty values issued by the SRI modules.
	- DES<sub>5</sub> (SRIs)
		- Conditions under which tasks can be run, suspended, or aborted are to be stated explicitly
			- Assuming a correct a task scheduler has been designed for the SRI modules, the alignment tasks would have been deactivated (by the scheduler)  as specified (right after lift-off).

## System Dimensioning
- **2 Faults** (Effects?)
		- DIM<sub>1</sub> - Operand Error was due to an unexpected high value of Horizontal Bias
		- Fault RC<sub>1</sub> would have been avoided if SpECS method was used.
	- DIM<sub>2</sub> - Both SRI modules failed and the f-out-of-n (1-out-of-2) implicit assumptions was violated
		- It was implicitly assumed that f's value would be 1 and that simple redundancy (n=2) would suffice.

# Exercise?
- **What were the software issues experienced? When were these issues experienced?** 
```
An Operand Error that caused an exception from converting a 64-bit floating point number F to 16-bit signed integer.
```
```
39 seconds after lift-off that the launcher started to disintegrate because of the angle of attack more than 20 degrees caused by full nozzle deflections of the solid boosters and the Vulcain main engine
```

- **What was the cause of these issues?**  
```
The On-Board Computer input data transmitted by the Inertial Reference System did not contain proper flight data. Although it showed diagnostic bit pattern that got interpreted as regular flight data by the OBC. Thus, resulting an exception.
```

- **Where do you think these errors were introduced?**  
```
It occured at the Inertial Reference System 2 (SRI2) however, the cause was from the On-Board Computer (OBC) that provided improper flight data.
```

- **What could have been done to eliminate the errors mentioned?**  
```
If the engineers had done System Engineering for Computer Systems (SpECS) implementation, they could've prevent the design and system errors.
```

- **What is the role of software engineering practice in this case?**
```

```

----
# References
- https://www.researchgate.net/publication/220882405_An_analysis_of_the_Ariane_5_flight_501_failure-a_system_engineering_perspective