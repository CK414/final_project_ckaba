# ACIT4420 Final Project - TarjanPlanner
 Final Project for ACIT 4420

 Contains two parts, TarjanPlanner, & FileOrganizer

## Part 1: TarjanPlanner
 Program must calculate the most efficient route through Seoul, S. Korea to reach the locations of Tarjan's 10 relatives.

 run from:
```
 PS C:\Users\Christopher Kaba\OneDrive - OsloMet\Python Files\ACIT 4420\final_project_ckaba>
 ```
 using the command:
 ```
 python -m tarjan_planner
 ```

 ## Project Directory Example

```
/final_project_ckaba
# Root directory
    /tarjan_planner 
    # Directory contains main python modules for project.
        filehandler.py
        interface.py
        logger.py
        optimizer.py
        relatives_manager.py
        transport_manager.py
        __init__.py
        __main__.py
    /data 
    # Directory stores all files written or read by program.
        relatives.csv
        transport_modes.csv
    /tests 
    # Directory contains test modules for program.
        test.py
        __init__.py
    setup.py
    README.md
    .gitattributes
    .gitignore
```