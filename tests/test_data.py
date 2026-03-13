import os
import pytest
from src.health_app.health import Health
from src.health_app.data import save_records , load_records,get_statistics
test_file="test_health.json"

def test_save():
    person1=Health("Ahmad",70,1.75)
    person2=Health("sara",60,1.65)
    records=[person1,person2]
    
    save_records(records,filename=test_file)
    L= load_records(filename=test_file)# {name:Ahmad,w:70}
    assert len(L)==2
    assert L[0].name=='Ahmad'
    assert L[0].bmi==person1.bmi
    
    ST=get_statistics(filename=test_file)
    assert ST['total_records']==2
    assert ST["avg_bmi"]==round(((person1.bmi+person2.bmi)/2),2)
    assert ST["most_common_category"]=='normal'
    assert ST["category_distribution"]=={"normal:2"}
    
    if os.path.exists(test_file):
        os.remove