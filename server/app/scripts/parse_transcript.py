import pdfplumber
import re
import sys
from typing import List

def extract_all_courses(pdf_path: str) -> List[str]:
    """
    Parses UTA unofficial transcript PDF to find all course codes,
    handling graded, in-progress, and test credit formats. WE ARE ONLY
    GETTING THE COURSE CODES, NOT THE GRADES.
    """
    
    # Pattern 1: Finds courses at the start of a line (for regular semesters)
    # e.g., "ART 1301..." or "ARCH 1301..."
    semester_course_pattern = re.compile(r'^[A-Z]{3,4}\s\d{4}')
    
    # Pattern 2: Specifically finds courses from the "Test Credits" section.
    # It looks for the "Transferred to Term...as" text and captures the course code that follows.
    test_credit_pattern = re.compile(r'Transferred to Term .*? as\s+([A-Z]{3,4}\s\d{4})')

    # Use a set to automatically handle any duplicates.
    found_courses_set = set()
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Reading {len(pdf.pages)} pages from '{pdf_path}'...")
            
            for page in pdf.pages:
                text = page.extract_text(x_tolerance=2, y_tolerance=2)
                
                if not text:
                    continue
                
                # --- Search for Test Credit courses first ---
                test_credit_matches = test_credit_pattern.findall(text)
                for course_code in test_credit_matches:
                    found_courses_set.add(course_code)
                
                # --- Search for regular and in-progress courses line by line ---
                lines = text.split('\n')
                for line in lines:
                    if semester_course_pattern.match(line.strip()):
                        # Extract the first two parts (e.g., "ARCH" and "1301")
                        parts = line.strip().split()
                        course_code = f"{parts[0]} {parts[1]}"
                        found_courses_set.add(course_code)
                        
    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
        print("Please make sure the path on line 58 is correct.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    # Return a unique, sorted list of the courses
    unique_courses = sorted(list(found_courses_set))
    return unique_courses

# --- Main execution block ---
if __name__ == "__main__":
    
    transcript_pdf_path = ""
    
    
    extracted_courses = extract_all_courses(transcript_pdf_path)
    
    if extracted_courses:
        print("\n--- Found Courses ---")
        for course in extracted_courses:
            print(course)
        print(f"\nTotal unique courses found: {len(extracted_courses)}")
    else:
        print("\nNo course codes could be extracted. Please check the file path and PDF content.")