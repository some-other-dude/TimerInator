import clock

def test_make_a_new_clock():
    c = clock.Clock()
    assert type(c) == clock.Clock

def test_new_clock_with_no_params():
    c = clock.Clock()
    assert c.name == "New Clock"
    assert c.total_time == 0
    assert c.remaining_time == 0
    assert c.status == "stopped"
    assert c.pid == None

def test_new_clock_with_params():
        c = clock.Clock(name = "My Clock", total_time = 60, remaining_time = 30, status = "paused", pid = 1)
        assert c.name == "My Clock"
        assert c.total_time == 60
        assert c.remaining_time == 30
        assert c.status == "paused"
        assert c.pid == 1

def test_change_clock_name():
    c = clock.Clock()
    c.name = "Another Clock"
    assert c.name == "Another Clock"

def test_change_clock_total_time():
    c = clock.Clock()
    c.total_time = 99
    assert c.total_time == 99

def test_change_clock_current_time():
    c = clock.Clock()
    c.current_time = 99
    assert c.current_time == 99

def test_change_clock_remaining_time():
    c = clock.Clock()
    c.remaining_time = 99
    assert c.remaining_time == 99

def test_change_clock_status():
    c = clock.Clock()
    c.status = "purple"
    assert c.status == "purple"

def test_change_clock_pid():
    c = clock.Clock()
    c.pid = 99
    assert c.pid == 99
