"""
Виртуальные окружения.
"""
"""
pyhton3 -m venv venv 

venv/Scripts/activate
source venv/bin/activate

pip install ____
pip freeeze > requirements.txt
pip install -r requirements.txt
"""

"""
Регулярные выражения.
"""
import re
password ="zdsajk12231"
password2 = "1234wqewe5678"
password3 = "HHuu1345"
def chack_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$"
    if re.fullmatch(pattern, password):
        return True
    else:
        return False
    ewwedd
print(chack_password(password))
print(chack_password(password2))
print(chack_password(password3))