import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Data with detailed complaints
data = [
    {
        "name": "Amanda Ward",
        "location": "29 River Heights Blvd, Cochrane - Riversong Phase 5",
        "tags": ["Pedestrian Safety", "Crosswalk Issues", "Visibility", "Traffic Behavior", "Infrastructure Improvement"],
        "details": "Vehicles do NOT stop for children waiting at the crosswalks. Vehicles park too close to the crosswalk, obstructing driver's vision. Request for a pedestrian light to prevent future tragedy."
    },
    {
        "name": "Chris Bednarski",
        "location": "Fireside Pkwy & Fireside Burrow, Cochrane - Fireside",
        "tags": ["School Zone Safety", "Pedestrian Safety", "Traffic Congestion", "Infrastructure Improvement"],
        "details": "Area at school corner and Fireside burrow very congested with traffic and pedestrians at peak hours. Kids often don't look before crossing. Request for flashing lights to alert drivers when pedestrians intend to cross."
    },
    {
        "name": "Clarence Guenter",
        "location": "320 50 Grande Ave, Cochrane AB Canada T4C2P6 - Downtown",
        "tags": ["Pedestrian Safety", "Infrastructure Improvement", "Community Engagement"],
        "details": "Suggestions to improve pedestrian safety and increase pedestrian activity in the highest density housing and commercial area of Cochrane. Concerns discussed with many friends and neighbors."
    },
    {
        "name": "Marc Lahaie",
        "location": "Heritage Blvd & Heritage Dr, Cochrane - Heritage Hills",
        "tags": ["Intersection Safety", "Traffic Behavior", "Infrastructure Improvement"],
        "details": "Precarious 2-way stop intersection with near misses becoming more frequent. New drivers to the area treat it as a 4-way stop. Request to change to a 4-way stop."
    },
    {
        "name": "Daniel Petitclerc",
        "location": "272 Sundown Rd, Cochrane - Sunset Ridge",
        "tags": ["Speeding", "Intersection Safety", "Traffic Calming", "Infrastructure Improvement"],
        "details": "Excessive speeds of vehicles travelling on Sundown Road through this area and by the playground. Request to make the intersection of Sundown Road and Sundown View a 4-Way Stop to slow traffic down."
    },
    {
        "name": "Haley Ellenbroek",
        "location": "41 Sunrise Heath, Cochrane - Sunset Ridge",
        "tags": ["Pedestrian Safety", "Crosswalk Issues", "Infrastructure Improvement"],
        "details": "Near misses crossing the road (north/south) at intersection of Sunrise Heath and Sunrise Way. Curb is depressed for crossing but no painted crosswalk or signage. Request for crosswalk signage."
    },
    {
        "name": "Sheena Cates",
        "location": "Sunset Dr & Circle Crosswalk, Cochrane - Sunset Ridge",
        "tags": ["Pedestrian Safety", "Crosswalk Issues", "Traffic Behavior", "Infrastructure Improvement"],
        "details": "Vehicles do not yield to pedestrians at the intersection of Sunset Circle and Sunset Drive. Increased traffic due to terminated access from highway 22. Request for an automated crosswalk."
    },
    {
        "name": "Chris Morrison",
        "location": "Sunset Manor entrance, Cochrane - Sunset Ridge",
        "tags": ["Intersection Safety", "Visibility", "Traffic Behavior"],
        "details": "Multiple collisions on the same turn at corner lot of small residential street. Cars parking into the turn on the corner reduces visibility for drivers approaching the corner."
    },
    {
        "name": "Rebecca Carroll",
        "location": "20 Sunset Rd, Cochrane - Sunset Ridge",
        "tags": ["Pedestrian Safety", "Crosswalk Issues", "Speeding", "Visibility", "Infrastructure Improvement", "School Zone Safety"],
        "details": "Close calls and witnessed incidents at intersection of Sunset Road/Sunrise View/Sunrise Heath. Blind crossing when driving southbound and when crossing Sunset Road east to west due to curve in the road. Many drivers going above speed limit. Request for a lit crosswalk."
    },
    {
        "name": "Casey Piercey",
        "location": "Sunset Blvd & Sunvalley Rd, Cochrane - Sunset Ridge",
        "tags": ["Pedestrian Safety", "Crosswalk Issues", "Traffic Behavior", "Infrastructure Improvement", "School Zone Safety"],
        "details": "Extremely dangerous crosswalk at Sunset Boulevard and Sunset Road/Sun Valley Road by the pond park. Many people not stopping or driving through when pedestrians are in the crosswalk. Busiest intersection, especially during school pickup and drop off. Request for pedestrian lights."
    },
    {
        "name": "Hilary Humphrey",
        "location": "West Rock Rd & West Side Dr, Cochrane - West Valley",
        "tags": ["Pedestrian Safety", "Crosswalk Issues", "Speeding", "Visibility", "Infrastructure Improvement"],
        "details": "4-year old daughter nearly struck on the crosswalk by a speeding vehicle exiting the Mitford Ponds parking lot. Heavily used crossing for children going to Zero Gravity Skate Park and for pathway access. Large semi-trucks often park along the road, reducing visibility. Request for a flashing crosswalk light."
    }
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Streamlit app
st.title('Transportation Concerns in Cochrane')

# Filter by theme
all_themes = sorted(set([theme for item in data for theme in item['tags']]))
selected_themes = st.multiselect('Filter by themes:', all_themes)

# Filter data based on selected themes
if selected_themes:
    filtered_df = df[df['tags'].apply(lambda x: any(theme in x for theme in selected_themes))].copy()
    filtered_df['Relevant Themes'] = filtered_df['tags'].apply(lambda x: ', '.join(set(x) & set(selected_themes)))
else:
    filtered_df = df.copy()
    filtered_df['Relevant Themes'] = filtered_df['tags'].apply(lambda x: ', '.join(x))

# Display filtered data
st.dataframe(filtered_df[['name', 'location', 'Relevant Themes', 'details']])

# Display statistics
st.subheader('Statistics')
st.write(f"Total number of concerns: {len(df)}")
st.write(f"Number of unique locations: {df['location'].nunique()}")

# Most common themes
theme_counts = pd.Series([theme for themes in df['tags'] for theme in themes]).value_counts()
st.write("Most common themes:")
st.bar_chart(theme_counts)