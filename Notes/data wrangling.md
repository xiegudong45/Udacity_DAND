## Assessing Data
### Unclean Data: Dirty vs. Messy
* Dirty data = low quality data = content issues.

* Messy data = untidy data = structural issues.

### Assessing vs. Exploring
* **Assessing**: gathering the right pieces of data, assess data's quality and structure, then modifying the data to make it clean. It won't make your visualization better.

* **Exploring**: exploring your data to later augment it, to maximize the potential of your analyses, visualizations and models. Simple visualizations will often used to summarize your data's main characteristics.

### Data Quality Dimensions
* **Completeness**: do we have all of the records that we should? Do we have missing records or not? Are there specific rows, columns, or cells missing?
* **Validity**: we have the records, but they're not valid, i.e., they don't conform to a defined schema. A schema is a defined set of rules for data. These rules can be real-world constraints (e.g. negative height is impossible) and table-specific constraints (e.g. unique key constraints in tables).
* **Accuracy**: inaccurate data is wrong data that is valid. It adheres to the defined schema, but it is still incorrect. Example: a patient's weight that is 5 lbs too heavy because the scale was faulty.
* **Consistency**: inconsistent data is both valid and accurate, but there are multiple correct ways of referring to the same thing. Consistency, i.e., a standard format, in columns that represent the same data across tables and/or within tables is desired.

## Cleaning Data
### Data Cleaning Process
1. Make a copy of each piece of data.
2. **Define**: define the issues.
3. **Code**
4. **Test**
