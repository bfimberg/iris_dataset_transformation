To get the data and view it:
    1. If you are on Windows, open command line in folder:
       iris_dataset_transformation and run command:
       pip install -r requirements.txt

       if you are on MacOS or Linux, open terminal in folder:
       iris_dataset_transformation and run command:
       pip3 install -r requirements.txt

    2. Run get_data.py

    3. Start app.py
    
    4. To see all of the data, open browser of choice and
       type: 127.0.0.1:5000/data

       To see average of a column, change the URL to:
       127.0.0.1:5000/average/column_name
       where column_name is the column of choice.

       To see the values of a column in a given range,
       change the URL to:
       127.0.0.1:5000/range/column_name/range_start/range_end
       where column_name is the choice of column, range start
       is the integer marking the beginning of range and
       range_end, an integer marking the end of the range.
