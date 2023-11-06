## Data Loading

**Result:**

```markdown
|    |   longitude |   latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value |
|---:|------------:|-----------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|
|  0 |     -114.31 |      34.19 |                   15 |          5612 |             1283 |         1015 |          472 |          1.4936 |                66900 |
|  1 |     -114.47 |      34.4  |                   19 |          7650 |             1901 |         1129 |          463 |          1.82   |                80100 |
|  2 |     -114.56 |      33.69 |                   17 |           720 |              174 |          333 |          117 |          1.6509 |                85700 |
|  3 |     -114.57 |      33.64 |                   14 |          1501 |              337 |          515 |          226 |          3.1917 |                73400 |
|  4 |     -114.57 |      33.57 |                   20 |          1454 |              326 |          624 |          262 |          1.925  |                65500 |
|  5 |     -114.58 |      33.63 |                   29 |          1387 |              236 |          671 |          239 |          3.3438 |                74000 |
|  6 |     -114.58 |      33.61 |                   25 |          2907 |              680 |         1841 |          633 |          2.6768 |                82400 |
|  7 |     -114.59 |      34.83 |                   41 |           812 |              168 |          375 |          158 |          1.7083 |                48500 |
|  8 |     -114.59 |      33.61 |                   34 |          4789 |             1175 |         3134 |         1056 |          2.1782 |                58400 |
|  9 |     -114.6  |      34.83 |                   46 |          1497 |              309 |          787 |          271 |          2.1908 |                48100 |
```

## Data Description

**Result:**

```markdown
|    | summary   |   longitude |    latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value |
|---:|:----------|------------:|------------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|
|  0 | count     | 17000       | 17000       |           17000      |      17000    |        17000     |     17000    |    17000     |     17000       |                17000 |
|  1 | mean      |  -119.562   |    35.6252  |              28.5894 |       2643.66 |          539.411 |      1429.57 |      501.222 |         3.88358 |               207301 |
|  2 | stddev    |     2.00517 |     2.13734 |              12.5869 |       2179.95 |          421.499 |      1147.85 |      384.521 |         1.90816 |               115984 |
|  3 | min       |  -124.35    |    32.54    |               1      |          2    |            1     |         3    |        1     |         0.4999  |                14999 |
|  4 | max       |  -114.31    |    41.95    |              52      |      37937    |         6445     |     35682    |     6082     |        15.0001  |               500001 |
```

## Average Total Rooms by Income Category

**SQL Query:**
```sql

SELECT IncomeCategory, AVG(total_rooms) AS AvgTotalRooms
FROM (
    SELECT *, 
    CASE
        WHEN median_income <= 2 THEN 'Low Income'
        WHEN median_income <= 4 THEN 'Moderate Income'
        WHEN median_income <= 6 THEN 'High Income'
        ELSE 'Very High Income'
    END AS IncomeCategory
    FROM housing
)
GROUP BY IncomeCategory
ORDER BY IncomeCategory

```

**Result:**

```markdown
|    | IncomeCategory   |   AvgTotalRooms |
|---:|:-----------------|----------------:|
|  0 | High Income      |         3020.58 |
|  1 | Low Income       |         1748.41 |
|  2 | Moderate Income  |         2469.97 |
|  3 | Very High Income |         3387.98 |
```

## Income Category Transformation

**Result:**

```markdown
|    |   longitude |   latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value | IncomeCategory   |
|---:|------------:|-----------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|:-----------------|
|  0 |     -114.31 |      34.19 |                   15 |          5612 |             1283 |         1015 |          472 |          1.4936 |                66900 | Low Income       |
|  1 |     -114.47 |      34.4  |                   19 |          7650 |             1901 |         1129 |          463 |          1.82   |                80100 | Low Income       |
|  2 |     -114.56 |      33.69 |                   17 |           720 |              174 |          333 |          117 |          1.6509 |                85700 | Low Income       |
|  3 |     -114.57 |      33.64 |                   14 |          1501 |              337 |          515 |          226 |          3.1917 |                73400 | Moderate Income  |
|  4 |     -114.57 |      33.57 |                   20 |          1454 |              326 |          624 |          262 |          1.925  |                65500 | Low Income       |
|  5 |     -114.58 |      33.63 |                   29 |          1387 |              236 |          671 |          239 |          3.3438 |                74000 | Moderate Income  |
|  6 |     -114.58 |      33.61 |                   25 |          2907 |              680 |         1841 |          633 |          2.6768 |                82400 | Moderate Income  |
|  7 |     -114.59 |      34.83 |                   41 |           812 |              168 |          375 |          158 |          1.7083 |                48500 | Low Income       |
|  8 |     -114.59 |      33.61 |                   34 |          4789 |             1175 |         3134 |         1056 |          2.1782 |                58400 | Moderate Income  |
|  9 |     -114.6  |      34.83 |                   46 |          1497 |              309 |          787 |          271 |          2.1908 |                48100 | Moderate Income  |
```

## Data Loading

**Result:**

```markdown
|    |   longitude |   latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value |
|---:|------------:|-----------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|
|  0 |     -114.31 |      34.19 |                   15 |          5612 |             1283 |         1015 |          472 |          1.4936 |                66900 |
|  1 |     -114.47 |      34.4  |                   19 |          7650 |             1901 |         1129 |          463 |          1.82   |                80100 |
|  2 |     -114.56 |      33.69 |                   17 |           720 |              174 |          333 |          117 |          1.6509 |                85700 |
|  3 |     -114.57 |      33.64 |                   14 |          1501 |              337 |          515 |          226 |          3.1917 |                73400 |
|  4 |     -114.57 |      33.57 |                   20 |          1454 |              326 |          624 |          262 |          1.925  |                65500 |
|  5 |     -114.58 |      33.63 |                   29 |          1387 |              236 |          671 |          239 |          3.3438 |                74000 |
|  6 |     -114.58 |      33.61 |                   25 |          2907 |              680 |         1841 |          633 |          2.6768 |                82400 |
|  7 |     -114.59 |      34.83 |                   41 |           812 |              168 |          375 |          158 |          1.7083 |                48500 |
|  8 |     -114.59 |      33.61 |                   34 |          4789 |             1175 |         3134 |         1056 |          2.1782 |                58400 |
|  9 |     -114.6  |      34.83 |                   46 |          1497 |              309 |          787 |          271 |          2.1908 |                48100 |
```

## Data Loading

**Result:**

```markdown
|    |   longitude |   latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value |
|---:|------------:|-----------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|
|  0 |     -114.31 |      34.19 |                   15 |          5612 |             1283 |         1015 |          472 |          1.4936 |                66900 |
|  1 |     -114.47 |      34.4  |                   19 |          7650 |             1901 |         1129 |          463 |          1.82   |                80100 |
|  2 |     -114.56 |      33.69 |                   17 |           720 |              174 |          333 |          117 |          1.6509 |                85700 |
|  3 |     -114.57 |      33.64 |                   14 |          1501 |              337 |          515 |          226 |          3.1917 |                73400 |
|  4 |     -114.57 |      33.57 |                   20 |          1454 |              326 |          624 |          262 |          1.925  |                65500 |
|  5 |     -114.58 |      33.63 |                   29 |          1387 |              236 |          671 |          239 |          3.3438 |                74000 |
|  6 |     -114.58 |      33.61 |                   25 |          2907 |              680 |         1841 |          633 |          2.6768 |                82400 |
|  7 |     -114.59 |      34.83 |                   41 |           812 |              168 |          375 |          158 |          1.7083 |                48500 |
|  8 |     -114.59 |      33.61 |                   34 |          4789 |             1175 |         3134 |         1056 |          2.1782 |                58400 |
|  9 |     -114.6  |      34.83 |                   46 |          1497 |              309 |          787 |          271 |          2.1908 |                48100 |
```

## Data Description

**Result:**

```markdown
|    | summary   |   longitude |    latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value |
|---:|:----------|------------:|------------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|
|  0 | count     | 17000       | 17000       |           17000      |      17000    |        17000     |     17000    |    17000     |     17000       |                17000 |
|  1 | mean      |  -119.562   |    35.6252  |              28.5894 |       2643.66 |          539.411 |      1429.57 |      501.222 |         3.88358 |               207301 |
|  2 | stddev    |     2.00517 |     2.13734 |              12.5869 |       2179.95 |          421.499 |      1147.85 |      384.521 |         1.90816 |               115984 |
|  3 | min       |  -124.35    |    32.54    |               1      |          2    |            1     |         3    |        1     |         0.4999  |                14999 |
|  4 | max       |  -114.31    |    41.95    |              52      |      37937    |         6445     |     35682    |     6082     |        15.0001  |               500001 |
```

## Data Loading

**Result:**

```markdown
|    |   longitude |   latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value |
|---:|------------:|-----------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|
|  0 |     -114.31 |      34.19 |                   15 |          5612 |             1283 |         1015 |          472 |          1.4936 |                66900 |
|  1 |     -114.47 |      34.4  |                   19 |          7650 |             1901 |         1129 |          463 |          1.82   |                80100 |
|  2 |     -114.56 |      33.69 |                   17 |           720 |              174 |          333 |          117 |          1.6509 |                85700 |
|  3 |     -114.57 |      33.64 |                   14 |          1501 |              337 |          515 |          226 |          3.1917 |                73400 |
|  4 |     -114.57 |      33.57 |                   20 |          1454 |              326 |          624 |          262 |          1.925  |                65500 |
|  5 |     -114.58 |      33.63 |                   29 |          1387 |              236 |          671 |          239 |          3.3438 |                74000 |
|  6 |     -114.58 |      33.61 |                   25 |          2907 |              680 |         1841 |          633 |          2.6768 |                82400 |
|  7 |     -114.59 |      34.83 |                   41 |           812 |              168 |          375 |          158 |          1.7083 |                48500 |
|  8 |     -114.59 |      33.61 |                   34 |          4789 |             1175 |         3134 |         1056 |          2.1782 |                58400 |
|  9 |     -114.6  |      34.83 |                   46 |          1497 |              309 |          787 |          271 |          2.1908 |                48100 |
```

## Income Category Transformation

**Result:**

```markdown
|    |   longitude |   latitude |   housing_median_age |   total_rooms |   total_bedrooms |   population |   households |   median_income |   median_house_value | IncomeCategory   |
|---:|------------:|-----------:|---------------------:|--------------:|-----------------:|-------------:|-------------:|----------------:|---------------------:|:-----------------|
|  0 |     -114.31 |      34.19 |                   15 |          5612 |             1283 |         1015 |          472 |          1.4936 |                66900 | Low Income       |
|  1 |     -114.47 |      34.4  |                   19 |          7650 |             1901 |         1129 |          463 |          1.82   |                80100 | Low Income       |
|  2 |     -114.56 |      33.69 |                   17 |           720 |              174 |          333 |          117 |          1.6509 |                85700 | Low Income       |
|  3 |     -114.57 |      33.64 |                   14 |          1501 |              337 |          515 |          226 |          3.1917 |                73400 | Moderate Income  |
|  4 |     -114.57 |      33.57 |                   20 |          1454 |              326 |          624 |          262 |          1.925  |                65500 | Low Income       |
|  5 |     -114.58 |      33.63 |                   29 |          1387 |              236 |          671 |          239 |          3.3438 |                74000 | Moderate Income  |
|  6 |     -114.58 |      33.61 |                   25 |          2907 |              680 |         1841 |          633 |          2.6768 |                82400 | Moderate Income  |
|  7 |     -114.59 |      34.83 |                   41 |           812 |              168 |          375 |          158 |          1.7083 |                48500 | Low Income       |
|  8 |     -114.59 |      33.61 |                   34 |          4789 |             1175 |         3134 |         1056 |          2.1782 |                58400 | Moderate Income  |
|  9 |     -114.6  |      34.83 |                   46 |          1497 |              309 |          787 |          271 |          2.1908 |                48100 | Moderate Income  |
```
