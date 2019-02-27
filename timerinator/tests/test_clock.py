import datetime as dt
import clock

time_1 = dt.datetime(year = 2019, month = 1, day = 1, hour = 1, minute = 10, second = 10)
time_2 = dt.datetime(year = 2019, month = 1, day = 1, hour = 1, minute = 10, second = 20)
time_3 = dt.datetime(year = 2019, month = 1, day = 1, hour = 1, minute = 10, second = 30)


def test_make_a_new_clock():
    c = clock.Clock()
    assert type(c) == clock.Clock

def test_new_clock_with_no_params():
    c = clock.Clock()
    assert c.name == "New Clock"
    assert c.total_time == 0
    assert c.remaining_time == 0
    assert c.start_time == None
    assert c.status == "stopped"
    assert c.pid == None

def test_new_clock_with_params():
        c = clock.Clock(name = "My Clock",
                        total_time = 60,
                        remaining_time = 30,
                        start_time = time_1,
                        status = "paused",
                        pid = 1)

        assert c.name == "My Clock"
        assert c.total_time == 60
        assert c.remaining_time == 30
        assert c.start_time == time_1
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

def test_change_clock_start_time():
    c = clock.Clock()
    c.start_time = time_2
    assert c.start_time == time_2

def test_change_clock_status():
    c = clock.Clock()
    c.status = "purple"
    assert c.status == "purple"

def test_change_clock_pid():
    c = clock.Clock()
    c.pid = 99
    assert c.pid == 99

def test_update_remaining_time_is_1():
    c = clock.Clock()
    c.current_time = 1
    c.update_remaining_time()
    assert c.remaining_time == 1

def test_update_remaining_time_is_0():
    c = clock.Clock()
    c.current_time = 0
    c.update_remaining_time()
    assert c.remaining_time == 0

def test_update_remaining_time_is_neg_1():
    c = clock.Clock()
    c.current_time = -1
    c.update_remaining_time()
    assert c.remaining_time == 0

def test_projected_end_time():
    c = clock.Clock()
    c.remaining_time = 30
    assert c.projected_end_time().strftime("%M:%S") == (dt.datetime.now() + dt.timedelta(seconds =c.remaining_time)).strftime("%M:%S")

def test_tick_clock():
    c = clock.Clock(start_time = dt.datetime.now() - dt.timedelta(seconds = 15),
                    total_time = 60,
                    current_time = 44,
                    remaining_time = 44)
    c.tick_clock()
    assert c.current_time == 15
    assert c.remaining_time == 15
