# #!/usr/bin/env python
# import sys
# import warnings
# from pathlib import Path

# from crew import CodeExecution

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """

#     file_path = 'C:\\Users\\PREETI MOTWANI\\Downloads\\GenAIPractice\\CrewAI-CodeExecution\\code_execution\\src\\code_execution\\County_Health_Rankings.csv'

#     inputs = {
#         'file_path': file_path
#     }
    
#     result=CodeExecution().crew().kickoff(inputs=inputs)
#     print(result)


# if __name__ == "__main__":
#     run()

#!/usr/bin/env python
import sys
import os
import warnings
from pathlib import Path

from crew import CodeExecution

# Suppress specific warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    # Use a raw string or correct file path formatting
    file_path = r'C:\Users\PREETI MOTWANI\Downloads\GenAIPractice\CrewAI-CodeExecution\code_execution\src\code_execution\County_Health_Rankings.csv'

    # Prepare input dictionary
    inputs = {
        'file_path': file_path
    }

    try:
        # Execute the crew and print the result
        result = CodeExecution().crew().kickoff(inputs=inputs)
        print(result)
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    # Add src directory to sys.path if needed
    sys.path.append(os.path.join(os.path.dirname(__file__), "src", "code_execution"))

    # Run the script
    run()

