\# E-Commerce Sales \& Customer Analytics Dashboard



!\[Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)

!\[Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)

!\[NumPy](https://img.shields.io/badge/NumPy-Data%20Processing-013243?logo=numpy)

!\[MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql)

!\[Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)

!\[SQL](https://img.shields.io/badge/SQL-Analytics-orange)

!\[GitHub](https://img.shields.io/badge/GitHub-Version%20Control-181717?logo=github)



An end-to-end \*\*E-Commerce Sales and Customer Analytics Dashboard\*\* built using \*\*Python, MySQL, SQL, and Power BI\*\*.



This project analyzes e-commerce sales, customer behavior, product performance, regional performance, profitability, returns, and customer segments. It demonstrates the complete data analytics workflow, starting from raw data preparation and ending with an interactive business intelligence dashboard.



\---



\## Table of Contents



\- \[Project Overview](#project-overview)

\- \[Business Problem](#business-problem)

\- \[Project Objectives](#project-objectives)

\- \[Key Features](#key-features)

\- \[Technology Stack](#technology-stack)

\- \[Dataset Overview](#dataset-overview)

\- \[Dataset Structure](#dataset-structure)

\- \[Project Architecture](#project-architecture)

\- \[Project Folder Structure](#project-folder-structure)

\- \[Data Cleaning and Preparation](#data-cleaning-and-preparation)

\- \[MySQL Database Design](#mysql-database-design)

\- \[SQL Analysis](#sql-analysis)

\- \[RFM Customer Segmentation](#rfm-customer-segmentation)

\- \[Power BI Dashboard](#power-bi-dashboard)

\- \[Dashboard Pages](#dashboard-pages)

\- \[Key Performance Indicators](#key-performance-indicators)

\- \[Business Insights](#business-insights)

\- \[Power BI Measures](#power-bi-measures)

\- \[Example SQL Queries](#example-sql-queries)

\- \[Installation and Setup](#installation-and-setup)

\- \[How to Run the Project](#how-to-run-the-project)

\- \[Power BI Connection Setup](#power-bi-connection-setup)

\- \[Dashboard Screenshots](#dashboard-screenshots)

\- \[Data Quality Note](#data-quality-note)

\- \[Future Improvements](#future-improvements)

\- \[Project Outcomes](#project-outcomes)

\- \[Author](#author)

\- \[License](#license)



\---



\## Project Overview



The \*\*E-Commerce Sales \& Customer Analytics Dashboard\*\* is a business intelligence project created to understand how an e-commerce business is performing.



The project combines Python-based data preparation, MySQL database management, SQL business analysis, customer segmentation, and Power BI visualization.



The final dashboard allows users to analyze:



\- Revenue

\- Cost

\- Profit

\- Profit margin

\- Orders

\- Customers

\- Product performance

\- Category performance

\- Regional sales

\- Customer behavior

\- Customer segments

\- Payment methods

\- Product returns

\- Monthly sales trends



The project is suitable for demonstrating skills in:



\- Data Analytics

\- Business Intelligence

\- Python

\- SQL

\- MySQL

\- Power BI

\- Data Cleaning

\- Data Modeling

\- Customer Segmentation

\- Dashboard Development



\---



\## Business Problem



E-commerce businesses generate large amounts of data through customer transactions, product sales, payments, returns, and customer interactions.



Without proper analysis, it can be difficult to answer important business questions such as:



\- How much revenue is being generated?

\- Which products are performing well?

\- Which categories are most profitable?

\- Which regions generate the highest sales?

\- How many customers have placed orders?

\- Which customers contribute the most revenue?

\- Which customers may require retention campaigns?

\- What is the monthly sales trend?

\- Which products have high return rates?

\- How much profit is generated after cost?

\- Which customer segments are valuable to the business?



This project solves these problems by converting raw transactional data into an interactive analytics dashboard.



\---



\## Project Objectives



The main objectives of this project are:



1\. Clean and prepare raw e-commerce datasets.

2\. Store structured data in a MySQL database.

3\. Perform business analysis using SQL.

4\. Calculate important business KPIs.

5\. Analyze customer purchasing behavior.

6\. Segment customers using RFM analysis.

7\. Analyze product and category performance.

8\. Analyze sales by region and time period.

9\. Visualize insights using Power BI.

10\. Build a professional analytics portfolio project.



\---



\## Key Features



\### Sales Analysis



\- Total revenue analysis

\- Total cost analysis

\- Total profit analysis

\- Profit margin calculation

\- Monthly revenue trends

\- Category-wise sales

\- Region-wise sales

\- Payment method analysis

\- Order quantity analysis



\### Customer Analysis



\- Total registered customers

\- Customers with orders

\- Customers without orders

\- Customer revenue contribution

\- Top customers by revenue

\- Customer order frequency

\- Customer purchasing behavior

\- RFM customer segmentation



\### Product Analysis



\- Top products by revenue

\- Top products by profit

\- Most frequently purchased products

\- Category performance

\- Product quantity sold

\- Product profitability

\- Product return analysis



\### Dashboard Features



\- Interactive KPI cards

\- Monthly trend charts

\- Category charts

\- Regional charts

\- Customer segmentation charts

\- Product performance charts

\- Return analysis

\- Interactive slicers and filters

\- Multiple dashboard pages



\---



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Data generation, cleaning, preprocessing, and analysis |

| Pandas | Data manipulation and transformation |

| NumPy | Numerical calculations |

| MySQL 8.0 | Database storage and management |

| SQL | Business analysis and database queries |

| Power BI | Interactive dashboard development |

| DAX | Calculated measures and KPIs |

| Git | Version control |

| GitHub | Project hosting and portfolio |

| VS Code | Development environment |



\---



\## Dataset Overview



The project uses a simulated e-commerce dataset containing customer information, product information, and order transactions.



\### Dataset Statistics



| Dataset | Records | Description |

|---|---:|---|

| Customers | 10,000 | Customer details |

| Products | 500 | Product details and pricing |

| Orders | 50,000 | Order transaction records |

| Final Cleaned Dataset | 50,000 | Merged and cleaned order-level data |



\### Data Quality Result



\- Final cleaned dataset contains \*\*50,000 rows\*\*.

\- Missing values after cleaning: \*\*0\*\*.

\- Customer records: \*\*10,000\*\*.

\- Product records: \*\*500\*\*.

\- Order records: \*\*50,000\*\*.

\- Customers with orders: \*\*9,940\*\*.

\- Customers without orders: \*\*60\*\*.



\---



\## Dataset Structure



\### Customers Dataset



The customers dataset contains information about registered customers.



| Column | Description |

|---|---|

| `customer\_id` | Unique customer identifier |

| `customer\_name` | Customer name |

| `email` | Customer email address |

| `gender` | Customer gender |

| `city` | Customer city |

| `region` | Customer region |

| `registration\_date` | Customer registration date |



\### Products Dataset



The products dataset contains product and pricing information.



| Column | Description |

|---|---|

| `product\_id` | Unique product identifier |

| `product\_name` | Name of the product |

| `category` | Product category |

| `subcategory` | Product subcategory |

| `cost\_price` | Product cost price |

| `selling\_price` | Product selling price |



\### Orders Dataset



The orders dataset contains transactional information.



| Column | Description |

|---|---|

| `order\_id` | Unique order identifier |

| `customer\_id` | Customer who placed the order |

| `product\_id` | Product purchased |

| `order\_date` | Date of order |

| `quantity` | Quantity purchased |

| `revenue` | Revenue generated from the order |

| `cost` | Cost associated with the order |

| `profit` | Profit generated from the order |

| `region` | Region where the order was placed |

| `category` | Product category |

| `return\_status` | Return status of the order |

| `payment\_method` | Payment method used |



\---



\## Project Architecture



```text

Raw E-Commerce Data

&#x20;       |

&#x20;       v

Python Data Cleaning

&#x20;       |

&#x20;       v

Data Transformation and Validation

&#x20;       |

&#x20;       v

Cleaned CSV Files

&#x20;       |

&#x20;       v

MySQL Database

&#x20;       |

&#x20;       v

SQL Business Analysis

&#x20;       |

&#x20;       v

SQL Views for Power BI

&#x20;       |

&#x20;       v

Power BI Data Model

&#x20;       |

&#x20;       v

Interactive Dashboard

&#x20;       |

&#x20;       v

Business Insights

