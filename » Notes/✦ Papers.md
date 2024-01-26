
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

# Special Problem

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
	WHERE subject = "CMSC198"
```

# Something I've just read


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
	WHERE randomly_read = "true"
```

%% Begin Waypoint %%
- **__documents**

- [[C. Vennila, K. Chandraprabha, M. Vijayaraj, S. Kavitha, S. Vimalnath, K. Kalaichelvi (2021). Traffic controlling and monitoring using IoT. Journal of physics, 2027(1), 012017]]
- [[D. Buckley, K. Chen and J. Knowles, "Predicting skill from gameplay input to a first-person shooter," 2013 IEEE Conference on Computational Inteligence in Games (CIG), Niagara Falls, ON, Canada, 2013]]
- [[Hagiwara, G., Akiyama, D., Furukado, R. & Takeshita, S. (2020). A study on psychological training of eSports using digital games׃ Focusing on rhythm game. Journal of Human Sport and Exercise, 15(3proc), S495-S503]]
- [[Kadena, Esmeralda & Gupi, Marsidi. Human factors in cybersecurity׃ risks and impacts. 2021.]]
- [[Zhang, X., & LeCun, Y. (2015). Text Understanding from Scratch]]
- [[Zhao, Y., Jiali, T., Huang, H., Wang, Z., Chen, T., Chiang, C., & Chiang, P. (2020). Development of IoT technologiesfor air pollution prevention and improvement. Aerosol and Air Quality Research, 20(12), 2874–2888]]

%% End Waypoint %%
