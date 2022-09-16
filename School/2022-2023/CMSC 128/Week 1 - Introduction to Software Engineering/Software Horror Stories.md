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

- On-Board Computer input data transmitted by the Inertial Reference System did not contain proper flight data. Although it showed diagnostic bit pattern that got interpreted as regular flight data by the OBC. 
	- Caused an exception from converting a 64-bit floating point number `F` to 16-bit signed integer.
		- F has greater value than the 16-bit signed integer thus causing an `Operand Error`
		- The cause was from the high value of an aligment function result called `Horizontal Bias`
	- Since Ariane 5 differs from Ariane 4 trajectory, this caused higher horizontal velocity values
- `Horizontal Velocity` is an external variable used to compute an integer variable `Horizontal Bias`
- **3 Faults**
	- External Variable
		- 
# Exercise?
- **What were the software issues experienced? When were these issues experienced?** 
```

```
``
```
39 seconds after lift-off that the launcher started to disintegrate because of the angle of attack more than 20 degrees caused by full nozzle deflections of the solid boosters and the Vulcain main engine
```
`3. Autopsy of the 501 Failure, 3.1 The failure scenario, p. 342`

- **What was the cause of these issues?**  
- **Where do you think these errors were introduced?**  
- **What could have been done to eliminate the errors mentioned?**  
- **What is the role of software engineering practice in this case?**

----
# References
- https://www.researchgate.net/publication/220882405_An_analysis_of_the_Ariane_5_flight_501_failure-a_system_engineering_perspective