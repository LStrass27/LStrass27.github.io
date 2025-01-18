## Analyzing Gasoline Price Impact on National Park Attendance

**Correlation_Visits.html:** Main output of the analysis. Mapped visualization of all the US national parks showing total attendance and impact of gasoline on each park's attendance.

**gas_aggregation.ipynb:** SQL testing of Gas price dataset and determining proper aggregation to be used for analysis.

**GAS_PRICES(1995-2021).csv:** CSV from Kaggle containing weekly US standardized gasoline prices for a variety of gasoline types from 1995 to 2021.

**National_park_population.csv:** Contains surrounding population data within a 75 mile radius of each of the national parks. Used to determine if there is a correlation between the surrounding population and what correlation value is given between gas prices and attendance.

**national_park_project.HTML:** HTML output of national_parks.ipynb

**national_parks.ipynb:** Jupyter notebook containing all the code and analysis of the project.

**US-National-Parks_RecreationVisits_1979-2023.csv:** Dataset of National Park attendance tracked annually from 1979-2023.

# Sources

National Park Data: https://www.responsible-datasets-in-context.com/posts/np-data/ \
Gasoline Price Data: https://www.kaggle.com/datasets/mruanova/us-gasoline-and-diesel-retail-prices-19952021 \
Population Data: https://www.statsamerica.org/radius/big.aspx \
Coordinates: https://www.geographyrealm.com/map-and-geography-trivia-u-s-national-parks/ \
Spearman: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html \
Pearson: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html \
Folium: https://python-visualization.github.io/folium/latest/