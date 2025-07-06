import pytest
from io import StringIO
import sys

from undo_stack import Patient, Stack, Undo


@pytest.fixture
def setup_stack():
    patient_stack = Stack(5)
    undo_stack = Undo()
    return patient_stack, undo_stack


def test_add_patient(setup_stack):
    patient_stack, undo_stack = setup_stack
    p1 = Patient("Alice", 101, "Malaria")
    patient_stack.push(p1)
    assert len(patient_stack.stack) == 1
    assert patient_stack.stack[0].name == "Alice"


def test_update_patient(setup_stack):
    patient_stack, undo_stack = setup_stack
    p1 = Patient("Bob", 102, "Typhoid")
    patient_stack.push(p1)

    old_info, updated_patient = patient_stack.update_patient(102, new_illness="COVID-19")
    assert updated_patient.illness == "COVID-19"
    assert "Typhoid" in old_info


def test_delete_patient(setup_stack):
    patient_stack, undo_stack = setup_stack
    p1 = Patient("Eliud", 103, "Flu")
    patient_stack.push(p1)

    deleted = patient_stack.delete_patient(103)
    assert deleted.name == "Eliud"
    assert len(patient_stack.stack) == 0


def test_undo_delete(setup_stack):
    patient_stack, undo_stack = setup_stack
    p1 = Patient("John", 104, "Headache")
    patient_stack.push(p1)

    deleted = patient_stack.delete_patient(104)
    undo_stack.add_info("Deleted", deleted)
    undo_stack.undo_last_info(patient_stack)


    assert len(patient_stack.stack) == 1
    assert patient_stack.stack[0].name == "John"


def test_undo_log_display(capsys, setup_stack):
    patient_stack, undo_stack = setup_stack
    p1 = Patient("Lucy", 105, "Stomach ache")
    undo_stack.add_info("Added", p1)

    undo_stack.show_info()
    captured = capsys.readouterr()
    assert "Lucy" in captured.out
