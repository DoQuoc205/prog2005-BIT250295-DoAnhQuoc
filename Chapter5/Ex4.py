import matplotlib.pyplot as plt
import pandas as pd

data = {
    'city': ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco',
             'Fresno', 'Sacramento', 'Long Beach', 'Oakland',
             'Bakersfield', 'Anaheim', 'Santa Ana'],
    'area_total_km2': [1302, 964, 466, 121, 296, 259, 170, 202, 382, 131, 70]
}
df = pd.DataFrame(data)

top10 = df.sort_values(by='area_total_km2', ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.barh(top10['city'], top10['area_total_km2'], color='skyblue')
plt.xlabel('Diện tích (km²)')
plt.title('Top 10 thành phố lớn nhất California theo diện tích')
plt.gca().invert_yaxis()
plt.show()