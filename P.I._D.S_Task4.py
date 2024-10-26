import pandas as pd
accidents = pd.read_csv('D://1 Intern/archive/AccidentsBig.csv')
casualties = pd.read_csv('D://1 Intern/archive/CasualtiesBig.csv')
vehicle = pd.read_csv('D://1 Intern/archive/VehiclesBig.csv')
print(accidents.head())
print(casualties.head())
print(vehicle.head())
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,6))
sns.countplot(x = 'Weather_Conditions', data=accidents, order=accidents['Weather_Conditions'].value_counts().index)
plt.xticks(rotation=90)
plt.title('road accidents by weateher')
plt.show()
accidents['Time'] = pd.to_datetime(accidents['Time'], errors='coerce')
accidents['Hour'] = accidents['Time'].dt.hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=accidents)
plt.title('Accident Count by Hour of the Day')
plt.show()
import folium

# Create a map centered around India
map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add accident locations (assuming 'Latitude' and 'Longitude' columns exist)
for index, row in accidents.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['Local_Authority(District)']).add_to(map)

# Save the map as an HTML file and display it
map.save("accident_map.html")
sns.countplot(x='Accident_Severity', data=accidents)
plt.title('Accident Severity Distribution')
plt.show()
