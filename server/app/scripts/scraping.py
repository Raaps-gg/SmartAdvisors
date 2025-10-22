from bs4 import BeautifulSoup
import requests
import re
import sqlite3
def find_data(html_content):
    """
    Find the (Course_Num, Course_Name) and (Prerequisites, Corequisites)
    Returned as list_of_titles and list_of_reqs respectively
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    titles_of_courses = soup.find_all(class_="courseblocktitle")


    """
    Find the Course Numbers and Names of all Classes in the chosen department
    """
    list_of_titles = []

    for i in titles_of_courses:
        delimited_list = i.text.split(".")
        if int(re.findall(r'\d+', delimited_list[0])[0]) > 5000:
            break
        list_of_titles.append(delimited_list)



    list_of_titles = [list_of_titles[i][:2] for i in range(len(list_of_titles))]
    
    """
    Find the Pre-Requisites and Co-requisites of a Class
    """
    list_of_reqs = []
    list_of_desc = []
    # print(list_of_titles)
    desc_of_courses = soup.find_all(class_="courseblockdesc")[:len(list_of_titles)]
    for i in desc_of_courses:
        list_of_desc.append(i.text)
        preqs = [ f"{department} " + j for j in re.findall(r'\d+',i.text) if int(j)>1000]
        list_of_reqs.append(preqs)

    return list_of_titles, list_of_reqs, list_of_desc

            
        
       


    # print(len(list_of_titles), len(desc_of_courses), len(list_of_preqs))

    # TODO 
    # Check to see if the key words pre-requisites are in the list
    # if so save it as the pre-req 

    # same process for the co-req
    # Concurrent Enrollment in 
    # or Concurrent enrollment

    # can refine it later on to have only the numbers of courses


    
    # return list_of_reqs
def insert_courses(html_content,department):

    db = sqlite3.connect("SmartAdvisors/data/classes.db")
    # allows to execute SQL queries with cur.execute("")
    cur = db.cursor()
    list_of_titles,list_of_preqs, description = find_data(html_content)
    print(len(list_of_titles))
    print(len(list_of_preqs))
    print(len(description))

    # Creates the Classes Table if not already present
    try:
        cur.execute(f"""CREATE TABLE ClassesFor{department}(Course_Num VARCHAR(10) NOT NULL, 
                                                            Course_Name VARCHAR(100) NOT NULL, 
                                                            Pre_Co_Requisites VARCHAR(50),
                                                            Description VARCHAR(1000),
                                                            PRIMARY KEY(Course_Num))""")
    except Exception as e:
        print(str(e))
        exit(0)
    sql_insert = f"""
        INSERT INTO ClassesFor{department} 
        (Course_Num, Course_Name, Pre_Co_Requisites, Description)
        VALUES (?, ?, ?, ?)
    """
        
    # print(list_of_preqs[0], description[0])
    for i in range(len(list_of_titles)):
        data = (
            list_of_titles[i][0],  # Course_Num
            list_of_titles[i][1],  # Course_Name
            str(list_of_preqs[i]),   # Pre_Requisites (Assuming list_of_preqs stores (pre, co) tuples)
            str(description[i])    # Co_requisites 
        )
        cur.execute(sql_insert,data)

    db.commit()

    # desc_of_courses = soup.find_all(class_="courseblockdesc")
def get_html_content(department):
    department = department
    department = department.lower()
    website=f"https://catalog.uta.edu/coursedescriptions/{department}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(website,headers=headers)
    response.raise_for_status()
    return response.text

department = "CE"





"""
Insert the into the database for any department
"""
# Requirements for BeautifulSoup
insert_courses(get_html_content(department),department)


# find_data(get_html_content(department))


