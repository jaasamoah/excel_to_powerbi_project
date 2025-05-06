# Analytics Workflow: From Spreadsheets to Dynamic Dashboards  

# Data Showcase: Excel to Power BI 

![excel-to-powerbi-animated-diagram](assets/images/kaggle_to_powerbi.gif)

# Table of contents 

- [Aim](#objective)  
- [Data Origin](#data-source)  
- [Phases](#stages)  
- [Layout](#design)  
  - [Prototype](#mockup)  
  - [Technologies](#tools)  
- [Implementation](#development)  
  - [Algorithm Outline](#pseudocode)  
  - [Initial Inspection](#data-exploration)  
  - [Data Refinement](#data-cleaning)  
  - [Data Shaping](#transform-the-data)  
  - [Building the SQL View](#create-the-sql-view)  
- [Validation](#testing)  
  - [Quality Assurance](#data-quality-tests)  
- [Presentation](#visualization)  
  - [Dashboard Preview](#results)  
  - [Key DAX Calculations](#dax-measures)  
- [Insights](#analysis)  
  - [Key Takeaways](#findings)  
  - [Verification](#validation)  
  - [Exploration](#discovery)  
- [Suggestions](#recommendations)  
  - [Estimated ROI](#potential-roi)  
  - [Next Steps](#potential-courses-of-actions)  
- [Wrap-Up](#conclusion)  

# Aim {#objective}

- **Primary challenge?**

  The Marketing Director needs to pinpoint the leading UK YouTube creators in 2024 to decide which influencers to approach for upcoming campaigns.

- **Desired outcome?**

  Build an interactive dashboard showcasing the top UK channels in 2024, detailing:
  - subscriber totals  
  - cumulative views  
  - video counts  
  - engagement indicators  

  This will empower the marketing team to select the most impactful partnerships.

## User Narrative

As the Marketing Director, I want an interactive dashboard that evaluates UK YouTube channel performance so I can easily spot channels with strong subscriber numbers and viewership. With that intelligence, I can choose the best influencers to work with and boost our campaign effectiveness.

# Data Origin {#data-source}

- **Required inputs?**  

  We need a dataset of the leading UK YouTube channels in 2024 with:
  - channel identifiers  
  - subscriber counts  
  - total view counts  
  - number of videos  

- **Source location**  
  This data comes from a Kaggle Excel export: [Top 100 Social Media Influencers 2024 (Country-wise)](https://www.kaggle.com/datasets/bhavyadhingra00020/top-100-social-media-influencers-2024-countrywise?resource=download).

# Phases {#stages}

- Layout  
- Implementation  
- Validation  
- Insights  

# Layout {#design}

## Prototype {#mockup}

To satisfy our objectives, the dashboard should answer:

1. Which 10 channels have the highest subscriber counts?  
2. Which 3 channels have uploaded the most content?  
3. Which 3 channels boast the largest view totals?  
4. Which 3 channels lead in average views per video?  
5. Which 3 channels have the best views-per-subscriber ratio?  
6. Which 3 channels deliver the greatest engagement per upload?

The requirements may evolve as analysis progresses.

- **Suggested visuals:**  
  - Data table  
  - Treemap  
  - KPI cards  
  - Horizontal bar charts  

![Dashboard-Mockup](assets/images/dashboard_mockup.png)

## Technologies {#tools}

| Tool         | Role                                                    |
| ------------ | ------------------------------------------------------- |
| Excel        | Data familiarization                                    |
| SQL Server   | Data cleaning, validation, and analysis                 |
| Power BI     | Crafting interactive visualizations                     |
| GitHub       | Version control and documentation repository            |
| Mokkup AI    | Producing wireframes and mockups                        |

# Implementation {#development}

## Algorithm Outline {#pseudocode}

1. Acquire the dataset  
2. Review data in Excel  
3. Import into SQL Server  
4. Cleanse and transform via SQL  
5. Perform data integrity checks  
6. Build Power BI visualizations  
7. Derive actionable insights  
8. Document process and commentary  
9. Publish to GitHub Pages  

## Initial Inspection {#data-exploration}

- What jumps out at first glance?  

  1. Four columns match our needs, so no extra sourcing required.  
  2. The first column combines channel IDs and names (separated by “@”); we’ll parse out the names.  
  3. Some headers or entries appear in another language—determine if they’re necessary.  
  4. There are extra fields beyond what’s needed, so we’ll drop the extras.

## Data Refinement {#data-cleaning}

- **Goals for the cleaned table:**  
  - Include only relevant fields  
  - Ensure correct data types  
  - No NULL values in key columns  

| Property         | Specification |
| ---------------- | ------------- |
| Rows             | 100           |
| Columns          | 4             |

| Column Name        | Data Type | Nullable |
| ------------------ | --------- | -------- |
| channel_name       | VARCHAR   | NO       |
| total_subscribers  | INTEGER   | NO       |
| total_views        | INTEGER   | NO       |
| total_videos       | INTEGER   | NO       |

- **Refinement steps:**  
  1. Select only necessary columns  
  2. Extract channel names from the combined ID field  
  3. Apply clear aliases  

### Data Shaping {#transform-the-data}

```sql
/*
1. Pick columns we need
2. Parse channel_name from 'NOMBRE'
*/
SELECT
    SUBSTRING(NOMBRE, 1, CHARINDEX('@', NOMBRE) - 1) AS channel_name,
    total_subscribers,
    total_views,
    total_videos
FROM
    top_uk_youtubers_2024;
```
### Building the SQL View {#create-the-sql-view}
```sql
/*
1. Define a view for the cleaned data
2. Cast channel_name to VARCHAR(100)
3. Select fields from original table
*/
CREATE VIEW view_uk_youtubers_2024 AS
SELECT
    CAST(SUBSTRING(NOMBRE, 1, CHARINDEX('@', NOMBRE) - 1) AS VARCHAR(100)) AS channel_name,
    total_subscribers,
    total_views,
    total_videos
FROM
    top_uk_youtubers_2024;
```



