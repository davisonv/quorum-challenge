# Quorum Code Challenge

## How to Run

To run this project, you need to set up a virtual environment and install the necessary 
packages. Follow the steps below:

1. **Create a virtual environment**

   Run the following command to create a virtual environment:

    ```bash
        python -m venv venv
    ```

2. **Activate the virtual environment**

    - On windows:
        ```bash
            venv\Scripts\activate
        ```
    
    - On macOS and Linux:
        ```bash
            source venv/bin/activate
        ```

3. **Install the required packages**

    Once the virtual environment is activated, install the required packages using pip:

    ```bash
        pip install -r requirements.txt
    ```

4. **Run the python file**
    ```bash
       python bills_insights.py
    ``` 

## How it works

After the code has been executed you should see the output files at the results folder.

## Challenge questions

**1. Discuss your solution’s time complexity. What tradeoffs did you make?**
I've tried to keep things as simple as they could be so i wouldn't spend more time 
than the suggested. To do so i created classes that need some assumptions, like 
well defined datasets. Also as in this challenge i had a specific scope i didn´t 
care alot about exceptions, what i would do in a production candidate code.

**2. How would you change your solution to account for future columns that might 
be requested, such as “Bill Voted On Date” or “Co-Sponsors”?**
I would have these columns as arguments in the methods and change the course of
the algorithm based in the arguments, like a filter by date if the date was provided 
or maybe the methods could receive all the columns that should be returned and 
filtered by.

**3. How would you change your solution if instead of receiving CSVs ofdata, 
you were given a list of legislators or bills that you should generate a CSV for?**
My aproach would basically be the same, turn any data source into a DataFrame.

**4. How long did you spend working on the assignment?**
I spent 2 to 2 and a half hours including writing this readme and doing minor improvements
in the code.

