import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean the data by filtering out days when the page views were in the top 2.5% or bottom 2.5% of the dataset.
df_cleaned = df[(df['value'] >= df['value'].quantile(0.025)) & 
                (df['value'] <= df['value'].quantile(0.975))]

# 3. Create a draw_line_plot function
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df_cleaned.index, df_cleaned['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

# 4. Create a draw_bar_plot function
def draw_bar_plot():
    df_bar = df_cleaned.groupby([df_cleaned.index.year, df_cleaned.index.month]).mean().unstack()

    fig = df_bar.plot(kind='bar', figsize=(10, 6)).get_figure()
    plt.legend(title='Months', labels=[calendar.month_abbr[i] for i in range(1, 13)])
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Page Views per Year')
    plt.xticks(rotation=90)
    plt.tight_layout()
    fig.savefig('bar_plot.png')
    return fig

# 5. Create a draw_box_plot function
def draw_box_plot():
    fig, ax = plt.subplots(1, 2, figsize=(20, 6))

    df_box_year = df_cleaned.copy()
    df_box_year.reset_index(inplace=True)
    df_box_year['Year'] = [d.year for d in df_box_year['date']]
    df_box_year['Month'] = [d.strftime('%b') for d in df_box_year['date']]
    sns.boxplot(x='Year', y='value', data=df_box_year, ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    df_box_month = df_cleaned.copy()
    df_box_month.reset_index(inplace=True)
    df_box_month['Month'] = [d.strftime('%b') for d in df_box_month['date']]
    sns.boxplot(x='Month', y='value', data=df_box_month, ax=ax[1], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')

    fig.tight_layout()
    fig.savefig('box_plot.png')
    return fig
