# Analytics Workflow: From Data Sheets to Dynamic Insights  

![excel-powerbi-workflow](assets/images/kaggle_to_powerbi.gif)  

---

## Navigation Guide  
- [Objective Statement](#objective-statement)  
- [Data Source Overview](#data-source-overview)  
- [Process Stages](#process-stages)  
- [Dashboard Framework](#dashboard-framework)  
  - [Layout Design](#layout-design)  
  - [Technology Components](#technology-components)  
- [Execution Strategy](#execution-strategy)  
  - [Workflow Logic](#workflow-logic)  
  - [Preliminary Data Assessment](#preliminary-data-assessment)  
  - [Data Optimization](#data-optimization)  
  - [Query Execution](#query-execution)  
- [Quality Validation](#quality-validation)  
  - [Data Integrity Tests](#data-integrity-tests)  
- [Dynamic Reporting](#dynamic-reporting)  
  - [Visualization Results](#visualization-results)  
  - [Core Measurements](#core-measurements)  
- [Strategic Analysis](#strategic-analysis)  
  - [Critical Findings](#critical-findings)  
  - [Impact Validation](#impact-validation)  
  - [Trend Identification](#trend-identification)  
- [Actionable Recommendations](#actionable-recommendations)  
  - [Projected Outcomes](#projected-outcomes)  
  - [Implementation Plan](#implementation-plan)  

---

## Objective Statement  
**Primary Challenge**  
The Marketing Team requires data-driven identification of top UK YouTube creators for 2024 campaign collaborations through measurable analytics.  

**Strategic Approach**  
Create an interactive reporting system monitoring:  
- Follower growth metrics  
- Content production frequency  
- Audience interaction rates  

**User Requirement**  
> *As partnership coordinator, I require rapid channel evaluation based on performance analytics to enhance influencer selection efficiency.*  

---

## Data Source Overview  
**Essential Data Points**  
- Creator identifiers  
- Follower counts  
- Video view metrics  
- Upload frequency data  

**Origin**: [Kaggle dataset](https://www.kaggle.com/datasets/bhavyadhingra00020/top-100-social-media-influencers-2024-countrywise?resource=download) (Excel format)  

---

## Process Stages  
1. System Architecture  
2. Solution Development  
3. Result Verification  
4. Insight Development  

---

## Dashboard Framework  
**Central Analytical Objectives**  
1. Leading channels by follower base  
2. Most prolific content producers  
3. Top performing video content  
4. Optimal content engagement ratio  
5. Peak audience interaction levels  

**Visual Elements**  
- Information grids  
- Comparative visualizations  
- Metric snapshots  

![dashboard-prototype](assets/images/dashboard_mockup.png)  

### Technology Components  
| Tool | Purpose |  
|------|---------|  
| Excel | Initial data evaluation |  
| SQL Server | Data processing |  
| Power BI | Interactive visualization |  

---

## Execution Strategy  
### Workflow Logic  
1. Data acquisition  
2. Exploratory analysis  
3. SQL processing  
4. Dashboard deployment  

### Preliminary Data Assessment  
- Channel names need standardization  
- Mixed-language column headers present  
- Irrelevant columns requiring elimination  

### Data Optimization  
**Target Structure**  
| Column | Type | Requirements |  
|--------|-----|-------------|  
| channel_name | Text | Mandatory |  
| total_subscribers | Integer | Mandatory |  

### Query Execution  
```sql
/* Channel name standardization */
SELECT 
  SUBSTRING(NOMBRE, 1, CHARINDEX('@', NOMBRE)-1) AS channel_name,
  total_subscribers
FROM top_uk_youtubers_2024
