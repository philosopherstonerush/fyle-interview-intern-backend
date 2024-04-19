from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, Teacher

from .schema import AssignmentSchema, TeacherSchema
principal_assignments_resources = Blueprint('principal_assignments_resources', __name__)


@principal_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of assignments that are graded and submitted"""
    
    students_assignments = Assignment.filter(Assignment.state == 'SUBMITTED' or Assignment.state == 'GRADED')
    
    students_assignments_dump = AssignmentSchema().dump(students_assignments, many=True)
    
    return APIResponse.respond(data=students_assignments_dump)


@principal_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    
    """Grade an assignment"""    
    
    assignment = Assignment.filter_and_grade(incoming_payload)
    assignment_dump = AssignmentSchema().dump(assignment)
    
    db.session.commit()
    
    return APIResponse.respond(data=assignment_dump)


@principal_assignments_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def submit_assignment(p):
    """Submit an assignment"""
    
    teachers = Teacher.filter()

    teachers_dump = TeacherSchema().dump(teachers, many=True)
    
    return APIResponse.respond(data=teachers_dump)
