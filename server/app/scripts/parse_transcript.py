import pdfplumber
import re
import sys
from typing import List

def extract_all_courses(pdf_path: str) -> List[str]:
    """
    Parses a complete university transcript PDF to find all course codes,
    handling graded, in-progress, test credit, and transfer credit formats.
    """
    
    # Pattern 1: Finds courses at the start of a line (for regular semesters).
    semester_course_pattern = re.compile(r'^([A-Z]{2,4}(?:-[A-Z]{2})?)\s(\d{4})')
    
    # Pattern 2: For "Test Credits" where the course is on the same line as "as".
    test_credit_pattern = re.compile(r'Transferred to Term .*? as\s+([A-Z]{3,4}\s\d{4})')

    # Pattern 3: For "Transfer Credits" where the course is on the NEXT line after "as".
    transfer_credit_pattern = re.compile(r'Transferred to Term \d{4} \w+ as\s*\n\s*([A-Z]{3,4}\s\d{4})')

    found_courses_set = set()
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            print(f"Reading {len(pdf.pages)} pages from '{pdf_path}'...")
            
            for page in pdf.pages:
                text = page.extract_text(x_tolerance=2, y_tolerance=3)
                
                if not text:
                    continue
                
                # --- Search for all three patterns on each page ---
                test_credit_matches = test_credit_pattern.findall(text)
                for course_code in test_credit_matches:
                    found_courses_set.add(course_code)

                transfer_credit_matches = transfer_credit_pattern.findall(text)
                for course_code in transfer_credit_matches:
                    found_courses_set.add(course_code)
                
                lines = text.split('\n')
                for line in lines:
                    match = semester_course_pattern.match(line.strip())
                    if match:
                        course_code = f"{match.group(1)} {match.group(2)}"
                        found_courses_set.add(course_code)
                        
    except FileNotFoundError:
        print(f"Error: The file '{pdf_path}' was not found.")
        print("Please make sure the path on line 59 is correct.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    unique_courses = sorted(list(found_courses_set))
    return unique_courses

# --- Main execution block ---
if __name__ == "__main__":
    
    # ⬇️ IMPORTANT: THIS IS THE HARDCODED FILE PATH ⬇️
    # You must replace this placeholder with the full path to your PDF file.
    transcript_pdf_path = "/path/to/your/transcript.pdf"
    
    
    extracted_courses = extract_all_courses(transcript_pdf_path)
    
    if extracted_courses:
        print("\n--- Found Courses ---")
        for course in extracted_courses:
            print(course)
        print(f"\nTotal unique courses found: {len(extracted_courses)}")
    else:
        print("\nNo course codes could be extracted.")