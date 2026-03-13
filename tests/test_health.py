from src.health_app.health import Health

def test_bmi_cal():
    person=Health("Mouhamaad",70,1.70)
    assert person.bmi==24.22
    assert person.get_category()=="Normal"
    assert person.get_idael_weight()==63.6
    assert person.get_health_advice()=="Maintain lifestyle"
