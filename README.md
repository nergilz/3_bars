## Wich bar is closer

This script processes the json-file with the data and finds the largest bar, 
the smallest and the nearest bar, from the received coordinates
---

### How to use

The list of Moscow bars can be downloaded in JSON format:
1. register on the site and get the API key
2. Download file: 
```bash
https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}
```

### How to run

+ Requrements: Python 3.5

+ Run on Linux:

```bash

$ python bars.py <path to json-file>  # possibly requires call of python3 executive instead of just python

```
#### Example input data:
```bash

Input GPS coordinates longitube: 37.635709999610895
Input GPS coordinates latitube: 55.805575000158511

```

#### Scripts response example:
```bash

Biggest bar name : Спорт бар «Красная машина»
Biggest bar adress : Автозаводская улица, дом 23, строение 1
Biggest bar phone : (905) 795-15-84


Smallest bar name : БАР. СОКИ
Smallest bar adress : Дубравная улица, дом 34/29
Smallest bar phone : (495) 258-94-19


Closest bar name : Бар «Джонни Грин Паб»
Closest bar adress : проспект Мира, дом 91, корпус 1
Closest bar phone : (495) 602-45-85

```

+ Runing in Windows is similar

---
### Project objectives

The code was created for educational purposes.
In the framework of the training course on web development - [DEVMAN.org](https://devman.org)
