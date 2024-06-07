# 1. Import the data from medical_examination.csv and assign it to the df variable
import pandas as pd

df = pd.read_csv('medical_examination.csv')

# 2. Create the overweight column in the df variable
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot
def draw_cat_plot():
    # 5. Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat the data in df_cat to split it by cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Convert the data into long format and create a chart using seaborn's catplot()
    import seaborn as sns
    import matplotlib.pyplot as plt

    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig

    # 8. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 9. Draw the Heat Map
def draw_heat_map():
    # 10. Clean the data in the df_heat variable
    df_heat = df[(df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975)) &
                 (df['ap_lo'] <= df['ap_hi'])]

    # 11. Calculate the correlation matrix
    corr = df_heat.corr()

    # 12. Generate a mask for the upper triangle
    mask = (corr.abs() < 0.1)

    # 13. Plot the correlation matrix
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, annot=True, fmt='.1f', cmap='coolwarm', mask=mask, square=True, linewidths=0.5, ax=ax)

    # 14. Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
