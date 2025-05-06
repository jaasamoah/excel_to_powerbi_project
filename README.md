# Analytics Pipeline: Spreadsheets to Interactive Insights  

![excel-powerbi-workflow](assets/images/kaggle_to_powerbi.gif)  

---

## Contents Quicknav  
- [Project Goal](#project-goal)  
- [Dataset Origin](#dataset-origin)  
- [Workflow Phases](#workflow-phases)  
- [Dashboard Architecture](#dashboard-architecture)  
  - [Interface Blueprint](#interface-blueprint)  
  - [Tech Stack](#tech-stack)  
- [Implementation Process](#implementation-process)  
  - [Logic Outline](#logic-outline)  
  - [Initial Dataset Review](#initial-dataset-review)  
  - [Data Refinement](#data-refinement)  
  - [Query Implementation](#query-implementation)  
- [Quality Assurance](#quality-assurance)  
  - [Validation Checks](#validation-checks)  
- [Interactive Reporting](#interactive-reporting)  
  - [Dashboard Output](#dashboard-output)  
  - [Key Metrics](#key-metrics)  
- [Insights Generation](#insights-generation)  
  - [Key Discoveries](#key-discoveries)  
  - [ROI Verification](#roi-verification)  
  - [Pattern Recognition](#pattern-recognition)  
- [Strategic Guidance](#strategic-guidance)  
  - [Expected Returns](#expected-returns)  
  - [Execution Roadmap](#execution-roadmap)  

---

## Project Goal  
**Core Challenge**  
The Marketing Lead seeks to identify leading UK YouTubers for 2024 campaign partnerships through quantifiable metrics analysis.  

**Solution Framework**  
Develop an analytics dashboard tracking:  
- Audience size metrics  
- Content volume statistics  
- Engagement performance indicators  

**User Perspective**  
> *As campaign strategist, I need to quickly identify high-impact channels based on measurable performance data to optimize partnership decisions.*  

---

## Dataset Origin  
**Required Information**  
- Channel identifiers  
- Subscriber metrics  
- Viewership statistics  
- Content volume data  

**Source**: [Kaggle dataset](https://www.kaggle.com/datasets/bhavyadhingra00020/top-100-social-media-influencers-2024-countrywise?resource=download) (Excel format)  

---

## Workflow Phases  
1. System Design  
2. Solution Build  
3. Output Validation  
4. Insight Extraction  

---

## Dashboard Architecture  
**Key Analytical Questions**  
1. Top 10 channels by subscriber count  
2. Most active content creators  
3. Highest viewership channels  
4. Best performing content ratio  
5. Optimal audience engagement  

**Visual Components**  
- Data tables  
- Comparison charts  
- Metric summaries  

![dashboard-prototype](assets/images/dashboard_mockup.png)  

### Tech Stack  
| Tool | Function |  
|------|----------|  
| Excel | Initial data inspection |  
| SQL Server | Data transformation |  
| Power BI | Visual analytics |  

---

## Implementation Process  
### Logic Outline  
1. Dataset acquisition  
2. Preliminary analysis  
3. SQL transformation  
4. Dashboard development  

### Initial Dataset Review  
- Channel identifiers require parsing  
- Multilingual headers present  
- Excess columns needing removal  

### Data Refinement  
**Target Schema**  
| Column | Type | Constraints |  
|--------|-----|------------|  
| channel_name | Text | Required |  
| total_subscribers | Integer | Required |  

### Query Implementation  
```sql
/* Channel name extraction */
SELECT 
  SUBSTRING(NOMBRE, 1, CHARINDEX('@', NOMBRE)-1) AS channel_name,
  total_subscribers
FROM top_uk_youtubers_2024
