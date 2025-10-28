from bs4 import BeautifulSoup
import requests
import re
import sqlite3
import spacy

# --- New Code: Load spaCy Model Globally ---
# This loads the model once when the script starts, which is much more efficient.
# It will download the model if you don't have it installed.
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    print("Downloading spaCy model 'en_core_web_lg'...")
    print("This may take a minute and only needs to run once.")
    spacy.cli.download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# Regex to find course codes (e.g., CEE 1234, MATH 2425)
# This is often more reliable than just spaCy's POS tagging for this specific format
COURSE_RE = re.compile(r'([A-Z]{2,4})\s(\d{4})')

# --- New Code: Requisite Extraction Function ---
# --- New Code: Requisite Extraction Function (Modified) ---
# --- New Code: Requisite Extraction Function (State Machine) ---
def extract_requisites(description_text):
    """
    Uses spaCy to parse the *entire requisite block* (not just the last line)
    and uses a state machine to categorize courses.
    """
    prereqs = set()
    coreqs = set()

    # --- Step 1: Find the start of the entire requisite block ---
    lower_text = description_text.lower()
    
    # Find the first occurrence of any requisite keyword
    indices = [
        lower_text.find("prerequisite"),
        lower_text.find("corequisite"),
        lower_text.find("concurrent")
    ]
    
    # Filter out -1 (not found)
    valid_indices = [idx for idx in indices if idx != -1]
    
    if not valid_indices:
        # No requisite keywords found at all in the description
        return {"prereqs": prereqs, "coreqs": coreqs}
    
    # Get the index of the first keyword
    start_index = min(valid_indices)
    
    # Extract the entire block of text from that point forward
    req_block_text = description_text[start_index:]
    # --- End Step 1 ---

    # --- Step 2: Process this block with spaCy ---
    doc = nlp(req_block_text)
    
    # --- Step 3: Track the "state" as we read sentences ---
    # 0 = prerequisite mode (default)
    # 1 = corequisite mode
    current_mode = 0 
    
    # Set default mode based on the *first* keyword found
    first_keyword = lower_text[start_index:start_index+20]
    if "corequisite" in first_keyword or "concurrent" in first_keyword:
        current_mode = 1
    
    for sent in doc.sents:
        sent_text = sent.text.lower()
        
        # Check for keywords to *change* the state
        # (This handles "Prerequisite... Corequisite...")
        if "corequisite" in sent_text or "concurrent" in sent_text:
            current_mode = 1 # Now we are in coreq mode
        elif "prerequisite" in sent_text:
            current_mode = 0 # Now we are in prereq mode
            
        # Find all course codes in this sentence
        found_codes = COURSE_RE.findall(sent.text)
        if not found_codes:
            continue
            
        formatted_codes = {f"{dept} {num}" for dept, num in found_codes}

        # Apply codes based on the current_mode
        if current_mode == 1:
            coreqs.update(formatted_codes)
        else:
            prereqs.update(formatted_codes)

    return {"prereqs": prereqs, "coreqs": coreqs}

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
        # Split only on the first period
        delimited_list = i.text.split(".", 1)
        
        try:
            # Check for valid course num
            course_num_str = re.findall(r'\d+', delimited_list[0])[0]
            if int(course_num_str) > 5000:
                break  # Stop if we hit grad-level courses
                
            # [0] is "CSE 1320", [1] is "    Introduction to Programming    (3-2) 3"
            course_id = delimited_list[0].strip()
            
            # Clean the course name
            # "    Introduction to Programming    (3-2) 3"
            # Strip whitespace and remove the credit hours at the end
            course_name = re.sub(r'\s+\(.*\)\s*\d*$', '', delimited_list[1]).strip()
            
            list_of_titles.append([course_id, course_name])

        except (IndexError, ValueError):
            # Skip invalid formats (e.g., a title block without a period or number)
            continue

    """
    Find the Pre-Requisites and Co-requisites of a Class
    """
    list_of_reqs = []
    list_of_desc = []
    
    # Get descriptions, but only for the courses we've already processed
    desc_of_courses = soup.find_all(class_="courseblockdesc")[:len(list_of_titles)]
    
    for desc_html in desc_of_courses:
        desc_text = desc_html.text
        list_of_desc.append(desc_text)
        
        # --- Updated Code: Call the new spaCy function ---
        reqs = extract_requisites(desc_text)
        list_of_reqs.append(reqs)

    # TODO
    # IF THE Department from Prerequisite is not the same as the current department then grab the data for that department and add on the prerequisite
    # (This logic is complex and would require a recursive scraper)
    
    return list_of_titles, list_of_reqs, list_of_desc


def insert_courses(html_content, department):
   
    db_path = "SmartAdvisors/data/classes.db"
    
    db = sqlite3.connect(db_path)
    cur = db.cursor()
    
    list_of_titles, list_of_preqs, description = find_data(html_content)
    
    print(f"Found {len(list_of_titles)} titles.")
    print(f"Found {len(list_of_preqs)} requisite lists.")
    print(f"Found {len(description)} descriptions.")

    # Sanitize department name for table name (basic)
    safe_table_name = re.sub(r'[^a-zA-Z0-9_]', '', f"ClassesFor{department}")

    # Creates the Classes Table if not already present
    try:
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {safe_table_name}(
                                         Course_Num VARCHAR(10) NOT NULL PRIMARY KEY, 
                                         Course_Name VARCHAR(100) NOT NULL, 
                                         Pre_Requisites VARCHAR(200),
                                         Co_Requisites VARCHAR(200),
                                         Description VARCHAR(1000)
                                         )""")
    except Exception as e:
        print(f"Error creating table: {e}")
        db.close()
        return

    sql_insert = f"""
        INSERT OR REPLACE INTO {safe_table_name} 
        (Course_Num, Course_Name, Pre_Requisites,Co_Requisites, Description)
        VALUES (?, ?, ?, ?, ?)
    """
    
    for i in range(len(list_of_titles)):
        prereqs = ', '.join([str(item) for item in list_of_preqs[i]["prereqs"]])
        coreqs = ', '.join([str(item) for item in list_of_preqs[i]["coreqs"]])


        data = (
            list_of_titles[i][0],             # Course_Num
            list_of_titles[i][1],             # Course_Name
            str(prereqs), # Pre_Requisites 
            str(coreqs),  # Co_Requisites 
            str(description[i]).strip()       # Description
        )
        try:
            cur.execute(sql_insert, data)
        except Exception as e:
            print(f"Error inserting {data[0]}: {e}")

    db.commit()
    db.close()
    print(f"Successfully processed and saved data for {department} to {db_path}")

def get_html_content(department):
    department = department.lower()
    website = f"https://catalog.uta.edu/coursedescriptions/{department}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    print(f"Requesting data from {website}...")
    try:
        response = requests.get(website, headers=headers)
        response.raise_for_status()  # Will raise an error for bad responses (404, 500, etc.)
        print("Success.")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

# --- Main execution ---
department = "CE" # Example department

"""
Insert the into the database for any department
"""
html = get_html_content(department)
if html:
    insert_courses(html, department)