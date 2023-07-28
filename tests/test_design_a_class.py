from lib.design_a_class import *

def test_add_task():
    diary = Diary()
    task_description = "walk the dog"
    diary.add_task(task_description)
    assert task_description in diary.tasks

def test_view_tasks():
    diary = Diary()
    diary.add_task("walk the dog")
    diary.add_task("wash hair")
    diary.view_tasks()
    assert diary.tasks

def test_complete_tasks():
    diary = Diary()
    diary.add_task("walk the dog")
    diary.add_task("wash hair")
    diary.complete_tasks(2)
    diary.view_tasks()
    assert diary