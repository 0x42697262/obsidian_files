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
		
	FROM "» Notes/✦ Papers/Resource"
```
