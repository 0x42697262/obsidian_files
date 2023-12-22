
# Internet of Things

```dataview
	TABLE WITHOUT ID
		Title,
		Year,
		Month,
		Author,
		Journal,
		Publisher,
		bibliography AS Bibliography,
		join(map(tags, (x) => "#" + x)) as tags
		
	FROM "» Notes/✦ Papers"
	WHERE subject = "CMSC176"
```


%% Begin Waypoint %%
- **__documents**

- [[C. Vennila, K. Chandraprabha, M. Vijayaraj, S. Kavitha, S. Vimalnath, K. Kalaichelvi (2021). Traffic controlling and monitoring using IoT. Journal of physics, 2027(1), 012017]]
- [[Zhao, Y., Jiali, T., Huang, H., Wang, Z., Chen, T., Chiang, C., & Chiang, P. (2020). Development of IoT technologiesfor air pollution prevention and improvement. Aerosol and Air Quality Research, 20(12), 2874–2888]]

%% End Waypoint %%
